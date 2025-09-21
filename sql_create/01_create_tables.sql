PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  grade_level INTEGER NOT NULL
);

CREATE TABLE assessments (
  assessment_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  date_given TEXT NOT NULL,
  type TEXT NOT NULL
);

CREATE TABLE scores (
  student_id INTEGER NOT NULL,
  assessment_id TEXT NOT NULL,
  score REAL,
  status TEXT NOT NULL,
  PRIMARY KEY (student_id, assessment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id) ON DELETE CASCADE
);
