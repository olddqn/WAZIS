# WAZIS v0.1 — Implementation Plan

- Date: 2026-06-22
- Role: senior software architect (architecture is final — not redesigned here)
- Assumptions: **one developer · weekend build · optimize for simplicity and launch speed**
- Non-negotiable absences (the identity of WAZIS): **no voting, ranking, scoring, reputation, karma, trending, closure, resolve, priority, categories, assignment, moderation authority, maturity/claimability tracking.** These are enforced by *not building them* — confirmed at launch by the gate in §9.
- 一言: 単一 Entry の thread commons を、4 つの不在（vote/score/rank なし・closure なし・撤回は本人のみ・RF は外部 link で区別）とともに、1 開発者が週末で建てる。

---

## 1. Recommended tech stack

Server-rendered, SQLite-backed, minimal-to-zero client JS. The app is 3 screens / 3 actions / 1 table — an SPA would be pure overhead.

| Layer | Choice | Why |
|---|---|---|
| Language/web | **Python + Flask** | Smallest distance from idea to running CRUD; huge ecosystem; ~1 file possible |
| DB | **SQLite** (file) | Zero-ops, single file, perfect for a solo low-traffic launch; trivially backed up |
| Templates | **Jinja2** (server-rendered HTML) | Accessible, indexable, no build step; content is text |
| Client JS | **none required**; **HTMX optional** | Plain `<form>` + redirects work; HTMX only for inline reply/withdraw later |
| Auth | **Flask signed-cookie session** + a tiny `authors` table | Stateless sessions; passwordless pseudonyms (§4) |
| Backup | **Litestream → object storage** | Needs are held open — they must not be lost on disk failure |
| Deploy | **Fly.io / Render / Railway** (persistent volume) or a $5 VPS | One process + one SQLite file |

Strong alternative (single static binary, even simpler deploy): **Go + `net/http` + `html/template` + SQLite (`modernc.org/sqlite`)**. Same shape; pick whichever you type fastest in. **Do not** reach for React/Next/SvelteKit — it adds a build pipeline and state layer this app does not need.

---

## 2. Database schema

Two tables. The schema *cannot express* the forbidden concepts — that is the right-to-remain-open made structural.

```sql
CREATE TABLE authors (
  id          TEXT PRIMARY KEY,            -- UUID; this is identity (not reputation)
  handle      TEXT,                        -- display pseudonym, optional, non-unique-identity
  token_hash  TEXT NOT NULL,               -- hash of the recovery key (§4)
  created_at  TEXT NOT NULL                -- ISO-8601
);

CREATE TABLE entries (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  parent_id   INTEGER REFERENCES entries(id),   -- NULL = root (Need); else Reply
  author_id   TEXT NOT NULL REFERENCES authors(id),
  text        TEXT NOT NULL,
  link        TEXT,                              -- external reality link ⇒ Reality Feedback
  created_at  TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'open'
              CHECK (status IN ('open','withdrawn'))   -- NO 'closed' is even representable
);

CREATE INDEX idx_entries_parent  ON entries(parent_id);
CREATE INDEX idx_entries_created ON entries(created_at DESC);
CREATE INDEX idx_entries_author  ON entries(author_id);
```

Notes:
- **Roles are derived, never stored:** `parent_id IS NULL` ⇒ Need · has parent ⇒ Reply · has parent **and** non-null `link` ⇒ Reality Feedback. No `type` column.
- **No columns** for score/votes/rank/priority/category/reputation. Their absence is the design.
- **Ordering is `created_at DESC` only.** Newest-first. There is no other sort.
- **Withdrawal** is `UPDATE entries SET text='', link=NULL, status='withdrawn' WHERE id=? AND author_id=?` — content is genuinely removed; the row remains as a tombstone so children/thread structure survive (you cannot delete others' replies — no-governor).
- `created_at` as ISO-8601 text keeps SQLite simple; sort works lexicographically.

---

## 3. API endpoints

Server-rendered: pages are `GET`, mutations are `POST` + redirect (PRGiap pattern). No DELETE (withdrawal is the only removal). No endpoints exist for vote/close/etc. — they are simply absent.

| Method · Path | Purpose | Auth |
|---|---|---|
| `GET /` | Home — newest-first open roots; RF marker on threads containing a linked child | public |
| `GET /e/<id>` | Thread — root + descendants | public |
| `GET /new` | New Entry form | session (auto-created) |
| `POST /entries` | Create root (`text`) → redirect `/e/<new>` | session |
| `POST /entries/<id>/replies` | Reply (`text`, optional `link`) → redirect `/e/<root>` | session |
| `POST /entries/<id>/withdraw` | Withdraw **own** entry (server checks `session.author_id == entry.author_id`) | session + ownership |
| `GET /me` | Show your handle + one-time recovery key | session |
| `POST /me/handle` | Set/update display handle | session |
| `GET /recover` · `POST /recover` | Restore identity from a recovery key | public |
| `POST /logout` | Clear session cookie | session |

Hard rules in code:
- The withdraw handler **must** verify ownership server-side; never trust the client. This single check *is* no-governor.
- Reply/create accept only `text` (+ optional `link`); ignore/strip any other field. No `parent` spoofing beyond the path id.
- Auto-link bare URLs in `text` for display; store `text` verbatim.

---

## 4. Authentication design

Goal: a **pseudonymous, passwordless, PII-free** identity that is *just enough* to enforce author-only withdrawal. Identity is the one load-bearing prerequisite (final review §B) — without it, no-governor fails.

Flow:
1. **First write** (or visiting `/new`): server creates an `authors` row (`id` = UUID; `token` = random 32 bytes; store `token_hash`), sets a **signed session cookie** = `author_id` (HMAC-signed via Flask `SECRET_KEY`). No email, no password.
2. **Handle**: user may set a display pseudonym at `/me` (cosmetic; identity remains `author_id`).
3. **Recovery key**: `/me` shows the raw `token` **once** ("save this to use the same identity on another device / restore withdrawal rights"). `/recover` accepts a key → look up by `token_hash` → re-issue the signed cookie.
4. **Withdrawal authorization** = `session.author_id == entry.author_id`. That's the whole authority model.

Why this, not email/OAuth/passwords:
- Passwordless + no PII = aligns with pseudonymous/DID identity and avoids storing emails for sensitive needs.
- Stateless signed cookies = no sessions table.
- Recovery key = the holder never permanently loses the ability to withdraw (a dignity requirement) without an email dependency.

Out of scope for v0.1: DID/crypto identity, OAuth, email magic-links — all are clean **v0.2** upgrades on top of `author_id`.

---

## 5. Frontend routes (server-rendered pages)

| Route | Screen | Contents |
|---|---|---|
| `/` | **Home** | One-line identity + a small "what's *not* here" line (no votes / nothing closes / only you can take down your own); **[Share an open need]**; newest-first list of open roots (text · handle · time · `↩ Reality answered` if thread has a linked child); honest empty state |
| `/e/<id>` | **Thread** | Root entry; children in time order; linked children rendered as Reality Feedback (accent + label + clickable link); reply box (`text` + optional reality-link); **Withdraw** button only on your own entries |
| `/new` | **New Entry** | Gentle prompt; single `text` field; note "only you can take this down" |
| `/me`, `/recover` | identity | handle + recovery key; restore |

No nav bar with sections, no profile-with-stats page, no search-by-popularity. Navigation = a back link + the Share button. Mobile = single column; reply box pinned at the bottom of Thread.

Reality-Feedback rendering rule (the only "special" rendering, and it is property-based, not a type): a child with non-null `link` gets an accent border + "↩ what reality answered" + the link shown. It does **not** close the thread, get a badge, or sort above siblings.

---

## 6. MVP implementation order

Build in the order that yields a *running loop* fastest; each step is independently testable.

1. **Skeleton + DB:** Flask app, `schema.sql`, connection helper, `SECRET_KEY`.
2. **Identity:** signed-cookie session, auto-create author, recovery key, `/me`, `/recover`. *(Load-bearing — do it before any write so withdrawal works from day one.)*
3. **Create + New Entry:** `GET /new`, `POST /entries`. (You can now post a Need.)
4. **Home:** `GET /` newest-first list of open roots. (You can see Needs.)
5. **Thread:** `GET /e/<id>` root + children.
6. **Reply:** `POST /entries/<id>/replies` (+ optional link). (You can respond.)
7. **Withdraw:** `POST /entries/<id>/withdraw` with ownership check + content clear.
8. **Reality Feedback:** render linked children distinctly; compute `↩ Reality answered` marker for Home.
9. **Framing + empty state + mobile CSS** (single stylesheet, ~1 screen of CSS).
10. **Backup + deploy** (Litestream + Fly.io/Render).

---

## 7. Weekend-build roadmap

| Slot | Deliverable |
|---|---|
| **Fri eve (2–4h)** | Repo, Flask skeleton, schema, identity (steps 1–2). Posting impossible yet, but auth works. |
| **Sat AM** | Create + Home (steps 3–4). *You can post a need and see it listed.* |
| **Sat PM** | Thread + Reply (steps 5–6). *You can hold a conversation under a need.* |
| **Sat eve** | Withdraw + Reality-Feedback rendering (steps 7–8). *Core behavior complete.* |
| **Sun AM** | Framing line, empty state, mobile CSS (step 9) + run the §9 launch gate. |
| **Sun PM** | Litestream backup, deploy, smoke-test the **manual first loop** (post the Musubie need → reply with a Dan-Go Claim URL = Reality Feedback) → **launch.** |

End state Sunday night: a live public WAZIS holding open needs, where reality's answers appear as linked replies, and only authors can withdraw.

---

## 8. What can safely wait until v0.2

All deferrable, none forbidden (every v0.2 item stays consistent with the absences):
- **Dan-Go API integration** — v0.1 uses a pasted link; v0.2 can add a one-click "send to Dan-Go" helper that returns a Claim URL.
- **Additional bindings** (NPO / OSS / research) — in v0.1 they are simply *other links*; no schema change needed.
- **Pagination / "load more"** — v0.1 shows recent N; add when volume grows.
- **Notifications** ("someone replied to your need") — v0.2.
- **Plain-text → light Markdown / safe rich text** — v0.1 is plain text + autolinked URLs.
- **i18n (JA/EN)** — v0.2; a good first community contribution.
- **DID / cryptographic identity, OAuth, email recovery** — upgrades on `author_id`.
- **Spam/abuse handling** — v0.1 launch is *curated and low-volume*, so minimal (basic per-IP/session rate limiting only). **When it scales, the answer must be non-governance** (rate limits, transparency, objection-replies, the holder's withdrawal) — **not** moderation authority or content-removal-by-admin (that would break no-governor; this is the open U1 question, deliberately not pre-solved).
- **Accessibility polish, dark mode, RSS** — v0.2.

Explicitly **never** (any version): votes, likes, scores, ranking, trending, close/resolve, priority, categories, reputation/karma, assignees, moderator/admin authority over others' entries.

---

## 9. Launch gate — the four-absence audit (run before deploy)

WAZIS is defined by what it refuses. Before launch, grep the schema, endpoints, templates, and CSS and confirm **all four hold**:

1. **No measurement** — no `score/votes/rank/priority/reputation/karma/like` column, field, endpoint, button, or per-user count anywhere.
2. **No closure** — `status` admits only `open|withdrawn`; no `closed/resolved/done`; no close/resolve button; reply and RF never change a parent's status.
3. **Author-only withdrawal (no-governor)** — the *only* state-changing action on an entry is withdrawal by its own author; no edit/delete/lock/hide/close of others'; no admin/mod role exists.
4. **Reality by provenance** — "Reality answered" is rendered *only* from a non-null external `link` (property, not type); nothing else is dressed as Reality Feedback.

If any one fails, it is a forum, not WAZIS. If all four hold → **ship.**

---

## Summary

Flask + SQLite + Jinja, two tables (`authors`, `entries`), ~9 endpoints, signed-cookie pseudonymous auth with a recovery key, three server-rendered screens, no client framework. Buildable by one developer in a weekend; the hard part is **discipline (adding nothing)**, not engineering. The single load-bearing prerequisite is minimal authenticatable identity (so author-only withdrawal holds); the single deferred hard problem is dignity-at-scale (U1), to be answered without governance when a real case arrives. Build steps 1–10, run the §9 gate, deploy, and run the manual Musubie loop.

**Reduction is complete. Build.**

---

*This is an implementation plan, not application code. Architecture and philosophy are taken as final and were not redesigned. No forbidden concept (voting/ranking/moderation/closure/reputation/governance/categories/maturity/claimability/scoring) is introduced in v0.1 or v0.2. Stack and schema choices optimize for one-developer weekend launch and may be revised by the first real Reality Feedback.*
