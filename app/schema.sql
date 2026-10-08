-- WAZIS v0.1 schema. Two tables. The forbidden concepts are not even representable.
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

CREATE INDEX IF NOT EXISTS idx_entries_parent  ON entries(parent_id);
CREATE INDEX IF NOT EXISTS idx_entries_created ON entries(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_entries_author  ON entries(author_id);
