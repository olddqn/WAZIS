-- WAZIS v0.1 schema. Three tables. The forbidden concepts are not even representable.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS authors (
  id          TEXT PRIMARY KEY,          -- UUID; this is identity, NOT reputation
  handle      TEXT,                       -- optional display pseudonym (non-identifying)
  token_hash  TEXT NOT NULL,              -- sha256 of the recovery key (no email, no password)
  created_at  TEXT NOT NULL               -- ISO-8601 UTC
);

CREATE TABLE IF NOT EXISTS entries (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  parent_id   INTEGER REFERENCES entries(id),       -- NULL = root (Need); else Reply
  author_id   TEXT NOT NULL REFERENCES authors(id),
  text        TEXT NOT NULL,
  link        TEXT,                                  -- external reality link => Reality Feedback
  created_at  TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'open'
              CHECK (status IN ('open','withdrawn'))  -- 'closed' is impossible by design
);

-- Note: there are deliberately NO columns for votes, score, rank, priority,
-- category, reputation, or karma. Their absence is the design.

-- What kinds of response the author of a Need currently welcomes.
--
-- This is NOT a category of the Need and is never used to sort, filter or rank
-- Needs. It says what the author is open to hearing; it is not agreement to any
-- particular response, and it binds nobody to anything.
--
-- Append-only: each change is a new row, and the newest row is the current
-- statement. `welcomes` is a JSON list, sorted, drawn from three values
-- (information, mutual_aid, arranged_work), or NULL when the author has chosen
-- to say nothing. A Need with no row at all has simply never been asked.
CREATE TABLE IF NOT EXISTS need_intents (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  entry_id  INTEGER NOT NULL REFERENCES entries(id),
  welcomes  TEXT,
  set_at    TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_need_intents_entry ON need_intents(entry_id, id);
CREATE INDEX IF NOT EXISTS idx_entries_parent  ON entries(parent_id);
CREATE INDEX IF NOT EXISTS idx_entries_created ON entries(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_entries_author  ON entries(author_id);
