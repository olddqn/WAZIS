"""
WAZIS v0.1 — an open-needs commons.

A single object (Entry) in a tree. Root = Need. Child = Reply.
A child with an external link = Reality Feedback (distinguished by provenance, not type).

The identity of WAZIS lives in what it REFUSES to build. There is intentionally:
  - no vote / like / score / rank / trending      (no measurement of 想い)
  - no close / resolve / 'closed' status          (a need never closes — right of openness)
  - no moderator / admin authority over entries   (no-governor)
  - only the author may withdraw their own entry  (the whole authority model)
Do not add any of the above. The launch gate is: confirm all four absences hold.
"""

import json
import os
import re
import sqlite3
import secrets
import hashlib
import unicodedata
import uuid
from datetime import datetime, timezone

from flask import (
    Flask, g, request, redirect, url_for, render_template,
    session, abort, flash, jsonify,
)

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("WAZIS_DB", os.path.join(APP_DIR, "wazis.db"))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("WAZIS_SECRET_KEY")
if not app.config["SECRET_KEY"]:
    # Dev fallback only. In production set a STABLE WAZIS_SECRET_KEY env var —
    # if it changes, every signed session cookie (and thus identity/withdrawal) is lost.
    app.config["SECRET_KEY"] = "dev-insecure-change-me"
    app.logger.warning("WAZIS_SECRET_KEY not set; using an insecure development key.")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=(os.environ.get("WAZIS_HTTPS") == "1"),  # set WAZIS_HTTPS=1 behind TLS
)


# --------------------------------------------------------------------------- DB
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DB_PATH) as db, open(
        os.path.join(APP_DIR, "schema.sql"), encoding="utf-8"
    ) as f:
        db.executescript(f.read())


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------- identity (auth)
# Passwordless, PII-free pseudonyms. The session cookie (signed) carries author_id.
# A recovery key (shown once) restores the identity — and the right to withdraw —
# on another device, without any email or password.
def current_author_id():
    return session.get("author_id")


def get_author(aid):
    if not aid:
        return None
    return get_db().execute("SELECT * FROM authors WHERE id = ?", (aid,)).fetchone()


def ensure_author():
    """Return the current author_id, creating a pseudonymous identity on first write."""
    aid = session.get("author_id")
    if aid and get_author(aid):
        return aid
    aid = uuid.uuid4().hex
    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    db = get_db()
    db.execute(
        "INSERT INTO authors (id, handle, token_hash, created_at) VALUES (?,?,?,?)",
        (aid, None, token_hash, now_iso()),
    )
    db.commit()
    session["author_id"] = aid
    session["recovery_key"] = token  # surfaced at /me so the holder can save it
    flash("A private identity was created for you — no email, no password. "
          "Save your recovery key under “Identity” to keep the ability to withdraw your entries.")
    return aid


# ------------------------------------------------------------------------- CSRF
def csrf_token():
    tok = session.get("csrf")
    if not tok:
        tok = secrets.token_urlsafe(32)
        session["csrf"] = tok
    return tok


@app.before_request
def csrf_protect():
    if request.method == "POST":
        if (request.form.get("csrf") or "") != session.get("csrf"):
            abort(400, "Invalid or missing CSRF token.")


app.jinja_env.globals["csrf_token"] = csrf_token


@app.template_filter("when")
def when_filter(iso):
    try:
        return datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M UTC")
    except Exception:
        return iso


# ----------------------------------------------------------------------- helpers
def valid_link(link):
    return link.startswith("http://") or link.startswith("https://")


def find_root_id(entry_id):
    """v0.1: replies are direct children of the root, so the root is at most one hop up."""
    e = get_db().execute(
        "SELECT id, parent_id FROM entries WHERE id = ?", (entry_id,)
    ).fetchone()
    if e is None:
        return None
    return e["id"] if e["parent_id"] is None else e["parent_id"]


# ------------------------------------------------- what responses are welcome
# The author of a Need may say what kinds of response they welcome. This is not
# a category of the Need: nothing sorts, filters or ranks by it. It is not
# consent either. It says "I am open to hearing this kind of response", never
# "I agree to what you propose".
WELCOMES = ("information", "mutual_aid", "arranged_work")
WELCOMES_LABEL = {
    "information": "Information or pointers",
    "mutual_aid": "A hand from someone, with no payment",
    "arranged_work": "Someone proposing organised work",
}


def current_intent(entry_id):
    """The author's newest statement for a Need: (stated, welcomes, set_at)."""
    row = get_db().execute(
        "SELECT welcomes, set_at FROM need_intents WHERE entry_id = ? "
        "ORDER BY id DESC LIMIT 1", (entry_id,)
    ).fetchone()
    if row is None or row["welcomes"] is None:
        return {"stated": False, "welcomes": [], "set_at": None}
    return {"stated": True, "welcomes": json.loads(row["welcomes"]),
            "set_at": row["set_at"]}


# ------------------------------------------------- the Need document, contract 1
# A small, stable description of one Need for another system to read. It is the
# whole of what WAZIS promises about its shape; nothing outside WAZIS should read
# the database or scrape a page. See docs/contract/need-document-v1.md.
#
# It never names the author and never includes replies.
NEED_DOCUMENT_KIND = "wazis.need-document"
NEED_DOCUMENT_CONTRACT = 1
NEED_DIGEST_KIND = "wazis.need"
NEED_DIGEST_SCHEMA = 1

_ORIGIN = re.compile(
    r"^(https?)://"
    r"((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*)"
    r"(?::([0-9]{1,5}))?$"
)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_of(value):
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def clean_origin(value):
    """An origin in its plain form, or None if it is not one."""
    text = (value or "").strip().lower()
    if text.endswith("/"):
        text = text[:-1]
    match = _ORIGIN.match(text)
    if match is None:
        return None
    scheme, host, port = match.groups()
    if port is not None:
        number = int(port)
        if not 1 <= number <= 65535:
            return None
        if number != {"http": 80, "https": 443}[scheme]:
            return f"{scheme}://{host}:{number}"
    return f"{scheme}://{host}"


def normalise_need_text(text):
    """The words of a Need in the one form that is hashed: NFC, LF, trimmed."""
    text = unicodedata.normalize("NFC", text)
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def need_digest(instance, need_id, text):
    return sha256_of({"kind": NEED_DIGEST_KIND, "schema": NEED_DIGEST_SCHEMA,
                      "instance": instance, "need_id": need_id, "text": text})


def need_document(*, instance, entry, intent, issued_at):
    """One Need as contract 1 describes it. Pure: the same inputs, the same bytes.

    `entry` needs id, status, text and created_at; `intent` is what
    `current_intent` returns. A withdrawn Need has no words, so its document
    carries none, no digest of them, and no statement of what was welcome.
    """
    document = {
        "kind": NEED_DOCUMENT_KIND,
        "contract": NEED_DOCUMENT_CONTRACT,
        "instance": instance,
        "need_id": entry["id"],
        "status": entry["status"],
        "created_at": entry["created_at"],
        "issued_at": issued_at,
    }
    if entry["status"] == "open":
        text = normalise_need_text(entry["text"])
        document["text"] = text
        document["need_digest"] = need_digest(instance, entry["id"], text)
        document["need_digest_schema"] = NEED_DIGEST_SCHEMA
        document["intent"] = (
            {"stated": True, "welcomes": sorted(intent["welcomes"]),
             "set_at": intent["set_at"]}
            if intent["stated"] else {"stated": False})
    document["document_digest"] = sha256_of(document)
    return document


# ------------------------------------------------------------------------ routes
@app.route("/")
def home():
    db = get_db()
    roots = db.execute(
        "SELECT e.*, a.handle AS author_handle "
        "FROM entries e JOIN authors a ON e.author_id = a.id "
        "WHERE e.parent_id IS NULL AND e.status = 'open' "
        "ORDER BY e.created_at DESC LIMIT 200"
    ).fetchall()
    # Root ids whose thread carries a Reality Feedback (an open child with a real link).
    rf_roots = {
        r["parent_id"]
        for r in db.execute(
            "SELECT DISTINCT parent_id FROM entries "
            "WHERE parent_id IS NOT NULL AND status='open' "
            "AND link IS NOT NULL AND link != ''"
        ).fetchall()
    }
    return render_template("home.html", roots=roots, rf_roots=rf_roots)


@app.route("/e/<int:entry_id>")
def thread(entry_id):
    db = get_db()
    root_id = find_root_id(entry_id)
    if root_id is None:
        abort(404)
    root = db.execute(
        "SELECT e.*, a.handle AS author_handle "
        "FROM entries e JOIN authors a ON e.author_id = a.id WHERE e.id = ?",
        (root_id,),
    ).fetchone()
    if root is None:
        abort(404)
    replies = db.execute(
        "SELECT e.*, a.handle AS author_handle "
        "FROM entries e JOIN authors a ON e.author_id = a.id "
        "WHERE e.parent_id = ? ORDER BY e.created_at ASC",
        (root_id,),
    ).fetchall()
    return render_template("thread.html", root=root, replies=replies,
                           me=current_author_id(),
                           intent=current_intent(root_id),
                           welcomes_label=WELCOMES_LABEL)


@app.route("/entries/<int:entry_id>/intent", methods=["POST"])
def set_intent(entry_id):
    """The author says what kinds of response they welcome, or takes it back.

    Only the author, only on their own open Need. Each change is appended; the
    Need itself is not edited, and nothing else about it changes.
    """
    aid = current_author_id()
    db = get_db()
    e = db.execute("SELECT * FROM entries WHERE id = ?", (entry_id,)).fetchone()
    if e is None or e["parent_id"] is not None:
        abort(404)
    if not aid or e["author_id"] != aid:
        abort(403)
    if e["status"] != "open":
        abort(409, "This need was withdrawn.")
    if request.form.get("say_nothing"):
        stored = None
    else:
        chosen = request.form.getlist("welcomes")
        if any(value not in WELCOMES for value in chosen):
            abort(400, "Unknown kind of response.")
        stored = canonical_json(sorted(set(chosen)))
    db.execute(
        "INSERT INTO need_intents (entry_id, welcomes, set_at) VALUES (?,?,?)",
        (entry_id, stored, now_iso()))
    db.commit()
    return redirect(url_for("thread", entry_id=entry_id))


@app.route("/e/<int:entry_id>/need.json")
def need_json(entry_id):
    """The Need document for one Need (contract 1). Read-only.

    Served only when this instance knows its own public address: a document
    that names the wrong instance would be worse than none.
    """
    instance = clean_origin(os.environ.get("WAZIS_PUBLIC_ORIGIN"))
    if instance is None:
        return jsonify({"error": "this instance has no public origin configured "
                                 "(WAZIS_PUBLIC_ORIGIN), so it serves no Need "
                                 "documents"}), 503
    e = get_db().execute(
        "SELECT id, parent_id, text, status, created_at FROM entries WHERE id = ?",
        (entry_id,)).fetchone()
    if e is None or e["parent_id"] is not None:
        abort(404)
    document = need_document(instance=instance, entry=e,
                             intent=current_intent(entry_id), issued_at=now_iso())
    response = app.response_class(canonical_json(document) + "\n",
                                  mimetype="application/json")
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/new")
def new_entry():
    return render_template("new.html")


@app.route("/entries", methods=["POST"])
def create_entry():
    text = (request.form.get("text") or "").strip()
    if not text:
        flash("Please write something.")
        return redirect(url_for("new_entry"))
    aid = ensure_author()
    db = get_db()
    cur = db.execute(
        "INSERT INTO entries (parent_id, author_id, text, link, created_at, status) "
        "VALUES (NULL, ?, ?, NULL, ?, 'open')",
        (aid, text, now_iso()),
    )
    db.commit()
    return redirect(url_for("thread", entry_id=cur.lastrowid))


@app.route("/entries/<int:entry_id>/replies", methods=["POST"])
def reply(entry_id):
    db = get_db()
    root_id = find_root_id(entry_id)
    if root_id is None:
        abort(404)
    text = (request.form.get("text") or "").strip()
    link = (request.form.get("link") or "").strip() or None
    if not text and not link:
        flash("Add a few words, or a link to where reality answered.")
        return redirect(url_for("thread", entry_id=root_id))
    if link and not valid_link(link):
        flash("A reality link must start with http:// or https://")
        return redirect(url_for("thread", entry_id=root_id))
    aid = ensure_author()
    db.execute(
        "INSERT INTO entries (parent_id, author_id, text, link, created_at, status) "
        "VALUES (?, ?, ?, ?, ?, 'open')",
        (root_id, aid, text or "", link, now_iso()),
    )
    db.commit()
    return redirect(url_for("thread", entry_id=root_id))


@app.route("/entries/<int:entry_id>/withdraw", methods=["POST"])
def withdraw(entry_id):
    aid = current_author_id()
    db = get_db()
    e = db.execute("SELECT * FROM entries WHERE id = ?", (entry_id,)).fetchone()
    if e is None:
        abort(404)
    # no-governor: ONLY the author may withdraw their own entry. This check is the
    # entire authority model — there is no moderator or admin path.
    if not aid or e["author_id"] != aid:
        abort(403)
    db.execute(
        "UPDATE entries SET text='', link=NULL, status='withdrawn' "
        "WHERE id = ? AND author_id = ?",
        (entry_id, aid),
    )
    db.commit()
    return redirect(url_for("thread", entry_id=find_root_id(entry_id) or entry_id))


@app.route("/me")
def me():
    aid = current_author_id()
    author = get_author(aid) if aid else None
    name = None
    if author:
        name = author["handle"] or ("anon-" + author["id"][:6])
    return render_template("me.html", author=author, name=name,
                           recovery_key=session.get("recovery_key"))


@app.route("/me/handle", methods=["POST"])
def set_handle():
    aid = ensure_author()
    handle = (request.form.get("handle") or "").strip()[:40] or None
    db = get_db()
    db.execute("UPDATE authors SET handle = ? WHERE id = ?", (handle, aid))
    db.commit()
    flash("Handle updated.")
    return redirect(url_for("me"))


@app.route("/recover", methods=["GET", "POST"])
def recover():
    if request.method == "POST":
        key = (request.form.get("key") or "").strip()
        token_hash = hashlib.sha256(key.encode()).hexdigest()
        row = get_db().execute(
            "SELECT id FROM authors WHERE token_hash = ?", (token_hash,)
        ).fetchone()
        if row:
            session["author_id"] = row["id"]
            session.pop("recovery_key", None)
            flash("Identity restored.")
            return redirect(url_for("me"))
        flash("That recovery key did not match anything.")
        return redirect(url_for("recover"))
    return render_template("recover.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Signed out on this device. Use your recovery key to return.")
    return redirect(url_for("home"))


# Idempotent: create tables on import if missing (CREATE TABLE IF NOT EXISTS).
init_db()

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
