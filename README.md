<!-- SPDX-License-Identifier: Apache-2.0 -->

# WAZIS — 和智達

**WAZIS is an open-needs commons.**

It is a place to express a real-world need, keep it open, and record how reality answered
it. The long-term aim is to connect needs to people, capabilities and useful work. The
purpose is useful human work and helping people.

- Status: **v0.1, runs locally. Not deployed. There is no public instance.**
- Code: [`app/`](app/) — Python, Flask, SQLite, server-rendered HTML.
- Only law: do not violate the dignity of others ([WAZIS_CONSTITUTION.md](WAZIS_CONSTITUTION.md)).
- License: Apache-2.0 (see [License](#license)).

This README is the canonical description of WAZIS. Where an older document in this
repository disagrees with it, this README and the code in `app/` are correct.

---

## Concepts

**Need.** A Need is something open in the real world that a person wants to put into words:
a difficulty, a lack, a question that matters to them. In WAZIS it is a root entry of free
text. It has no title, category, priority or score.

**Who can create one.** Anyone who can reach a running instance. There is no sign-up, email
or password. A private pseudonymous identity is created on the first post, and a recovery
key is shown once so the author can return on another device.

**Reply.** Any entry written under a Need. Replies are one level deep.

**Reality Feedback.** A reply that carries an external `http(s)` link to where something
happened in the world in response to the Need. The link is its provenance. It is what
separates "reality answered" from discussion. WAZIS shows the link; it does not verify it.

**Withdrawal.** Only the author of an entry can withdraw it. The text and link are cleared
and a "withdrawn" marker stays so the thread remains intact. No one else can remove, close,
hide or edit an entry. A Need has no "closed" state.

## Public, private and release boundary

- **Everything posted is public** to anyone who can reach the instance. There are no private
  Needs, no drafts and no access control. Do not post anything you would not publish.
- **No instance is published today.** Running one on the open internet is a deliberate human
  step, not something the code does.
- **There is no release workflow.** WAZIS has no review or approval gate before an entry
  appears.
- **Planned rule for integrations:** anything that enters WAZIS from another system, or
  leaves WAZIS for one, is released only after explicit human approval.

---

## Implemented now

| Capability | State |
|---|---|
| Post a Need | Works |
| Reply to a Need, with or without a link | Works |
| Reality Feedback shown by its link, and marked on the home list | Works |
| Withdraw your own entry | Works; anyone else gets HTTP 403 |
| Pseudonymous identity with signed cookie and recovery key | Works |
| CSRF protection on every POST | Works |
| Home list of open Needs, newest first, no ranking | Works (latest 200) |
| Schema that cannot store a "closed" status | Works (SQLite `CHECK` constraint) |

Two tables hold everything: `authors` and `entries` ([`app/schema.sql`](app/schema.sql)).

## Current limitations

- Tests are a small offline suite ([`tests/`](tests/)). There is no linter, type checker or
  continuous integration configured.
- No JSON API, no migrations, no command-line tool, no packaging, no deployment setup.
- Links are checked only for an `http://` or `https://` prefix. Nothing confirms that a link
  shows what the reply says it shows.
- If `WAZIS_SECRET_KEY` is not set, the app falls back to an insecure development key. Set a
  stable secret before any real use.
- No rate limiting or spam control.
- No pagination beyond the latest 200 Needs. No search. No notifications.
- There is no moderator by design. How to respond to an entry that harms someone's dignity,
  without creating a governing authority, is an unresolved question.
- No real Need has been posted and no loop from Need to Reality Feedback has been run.

## Design constraints: the four absences

WAZIS is defined as much by what it refuses to build as by what it builds:

1. **No measurement** — no vote, like, score, rank or trending.
2. **No closure** — status is only `open` or `withdrawn`.
3. **No governor** — no moderator or admin authority over entries.
4. **Reality by provenance** — Reality Feedback is recognised by its external link, not by a
   type or a verdict.

Any change to `app/` should be checked against these four.

---

## Direction

The intended long-term flow is approximately:

```
NEED → DISCOVERY → MATCH → HUMAN DECISION → MISSION / JOB → CONTRIBUTION / WORK
     → ASSET / RESULT → REVIEW → RELEASE → REALITY FEEDBACK
```

**WAZIS implements the two ends of this flow today: NEED and REALITY FEEDBACK.** Every step
between them is done by hand, outside WAZIS, and returns as a link.

An open design question follows from the four absences: matching usually means scoring and
ranking, which WAZIS does not do. How discovery and matching can serve a Need without
ranking Needs or people inside WAZIS is not yet decided. The fixed points are that matching
informs a human decision and never replaces it.

## Planned and future integration

**None of the following exists in code.** WAZIS has no dependency on any other system, and
no other system depends on WAZIS.

| Area | Relationship today | Planned direction |
|---|---|---|
| **Mac Fleet OS** | Separate system. Mac Fleet OS lists WAZIS in its interface as "not implemented". | To be defined in an integration contract. Local first stays the default. |
| **Mission / Job** | WAZIS has no missions, jobs, tasks, deliverables or payments. | After a human decision, a Need may lead to a mission or job in another system. WAZIS would hold a link to it, not a copy of it. |
| **YUJO / matching** | None. WAZIS has no profiles, capabilities or matching. | Another system may suggest people or capabilities for a Need. See the open question above. |
| **Asset / provenance** | A Reality Feedback link may point at a published result. WAZIS does not check it. | Optional verification of results. See [docs/future-verification-layer.md](docs/future-verification-layer.md). |
| **Dan-Go** | A written mapping only ([bindings/dan-go/BINDING.md](bindings/dan-go/BINDING.md)). | The first hand-run loop is described in [app/README.md](app/README.md). |

Fixed rules for any future integration:

- **NFT is optional and never required.** An NFT public reference is one possible form of
  provenance among others.
- **Wallet ownership is not identity.** WAZIS identity is a pseudonym with a recovery key.
  There is no wallet code in WAZIS.
- **Blockchain is not required for WAZIS.**
- **Public release requires explicit human approval.**
- **Automated or AI assistance does not bypass a human decision**, and does not write
  Reality Feedback on reality's behalf.

---

## Run locally

See [app/README.md](app/README.md). In short:

```bash
cd app
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export WAZIS_SECRET_KEY="$(python3 -c 'import secrets;print(secrets.token_urlsafe(48))')"
python app.py            # http://127.0.0.1:5000
```

The SQLite database is created on first run and is not tracked in Git.

## Run the tests

From the repository root, with the application's environment active:

```bash
python -m unittest discover -s tests -v
```

The tests need only Flask and the Python standard library. They run offline, and each test
uses its own temporary database.

## Repository layout

```
README.md               this file: the canonical description
LICENSE                 Apache-2.0
WAZIS_CONSTITUTION.md   the only law and the inviolable clauses
CONTRIBUTING.md         how to take part (written for the earlier model)
CODE_OF_CONDUCT.md      conduct based on dignity
app/                    the v0.1 application: the canonical implementation
tests/                  offline tests for the application
docs/                   design records, reviews and history (start at docs/README.md)
bindings/               written mappings to external implementers (specification only)
questions/ candidates/ feedback/ schemas/   placeholders from the earlier model
.github/                issue and pull request templates from the earlier model
```

## Documentation

[docs/README.md](docs/README.md) is the index. In brief:

- [docs/design/](docs/design/) — how the implemented application was designed. The closest
  written match to the code is
  [WAZIS_V01_IMPLEMENTATION_PLAN.md](docs/design/WAZIS_V01_IMPLEMENTATION_PLAN.md).
- [docs/reviews/](docs/reviews/) — the reasoning that reduced the design to its current form.
- [docs/first-loop/](docs/first-loop/) — the search for a first real Need to carry through.
- [docs/history/](docs/history/) — the earlier specification, plan and README.
- [docs/future-verification-layer.md](docs/future-verification-layer.md) — a preserved
  concept that is not implemented.

These records were written between June and August 2026. They are kept as history and are
not rewritten.

Several describe an earlier model — Question → Discussion → Refinement → Implementation
Candidate — that was reduced, step by step, to the single-entry model the application
implements. [WAZIS_SPEC.md](docs/history/WAZIS_SPEC.md),
[WAZIS_MVP_PLAN.md](docs/history/WAZIS_MVP_PLAN.md), [CONTRIBUTING.md](CONTRIBUTING.md), the
`.github/` templates and the `questions/`, `candidates/`, `feedback/` and `schemas/` folders
still use that earlier vocabulary.

## License

- **Apache License 2.0** ([LICENSE](LICENSE)) for code, schemas and bindings.
- Prose documents may additionally be used under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- SPDX: `Apache-2.0 AND CC-BY-4.0`.
