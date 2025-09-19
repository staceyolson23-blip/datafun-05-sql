-- Run later (or now) to add a new column to assessments
ALTER TABLE assessments ADD COLUMN is_mastery INTEGER DEFAULT 0;
