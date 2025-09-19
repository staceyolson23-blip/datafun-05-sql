PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS standards (
  standard_id TEXT PRIMARY KEY,
  code        TEXT NOT NULL,
  domain      TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS assessments (
  assessment_id TEXT PRIMARY KEY,
  title         TEXT NOT NULL,
  date_given    TEXT,            -- e.g., 'YYYYMMDD' as text
  standard_id   TEXT NOT NULL,
  FOREIGN KEY (standard_id) REFERENCES standards(standard_id)
);
