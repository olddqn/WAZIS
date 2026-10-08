# WAZIS v0.1

An open-needs commons. A single object (`Entry`) in a tree:

- **Root entry** = a Need (something open).
- **Child entry** = a Reply.
- **Child entry with an external link** = Reality Feedback (reality answering, not discussion).

Roles come from **position + provenance**, never from a `type` column.

## The four absences (this is the identity of WAZIS)

There is intentionally **no** vote / like / score / rank / trending, **no** close / resolve
(`status` is only `open | withdrawn`), **no** moderator or admin authority over entries, and
**only the author may withdraw their own entry**. These are enforced by *not building them*.
Do not add any of them — that is the whole discipline.

## Run locally

```bash
cd app
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export WAZIS_SECRET_KEY="$(python3 -c 'import secrets;print(secrets.token_urlsafe(48))')"
python app.py            # http://127.0.0.1:5000
```

The SQLite database (`wazis.db`) is created automatically on first run.

## Configuration (env vars)

| Var | Purpose |
|---|---|
| `WAZIS_SECRET_KEY` | **Required in production.** Signs session cookies. Must be **stable** — if it changes, all identities/sessions (and the right to withdraw) are lost. |
| `WAZIS_DB` | Path to the SQLite file (default `app/wazis.db`). |
| `WAZIS_HTTPS` | Set to `1` behind TLS to mark the session cookie `Secure`. |
| `PORT` | Dev server port (default 5000). |

## Identity

Passwordless, PII-free pseudonyms. On your first share/reply, a private identity is created and
a **recovery key** is shown under **Identity** (`/me`). Save it — it's the only way to restore
your identity (and your ability to withdraw your entries) on another device, via `/recover`.

## Deploy (suggested)

- Any single-process host (Fly.io / Render / Railway / a small VPS) with a **persistent volume**
  for `wazis.db`.
- Run behind a real WSGI server, e.g. `gunicorn -w 2 app:app`, with `WAZIS_HTTPS=1`.
- Back up the SQLite file with **Litestream** (replicate to object storage) — held-open needs
  must not be lost.

## The first real loop (manual, no Dan-Go integration code needed)

1. Post the real need as a root entry.
2. Off-platform: turn a gapable aspect into a Dan-Go Claim and let it run.
3. When reality answers, **reply with a link** to the Dan-Go Claim / result — that reply *is*
   the Reality Feedback (the link is its provenance).

## Launch gate

Before deploying, confirm all four absences hold across schema, routes, templates, and CSS:
**no measurement · no closure · author-only withdrawal · reality-by-provenance.**
If any one fails, it's a forum, not WAZIS.
