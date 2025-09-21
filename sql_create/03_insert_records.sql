-- 03_insert_records.sql
-- Adds: 10 new students, 10 new assessments (FA_6..FA_14, SA_2),
-- and scores for every (new student × new assessment) pair.

-- 1) 10 fictional students (IDs chosen to avoid CSV IDs 1..22)
INSERT INTO students (student_id, grade_level) VALUES
  (2001,7),(2002,7),(2003,7),(2004,7),(2005,7),
  (2006,7),(2007,7),(2008,7),(2009,7),(2010,7);

-- 2) 10 fictional assessments:
--    9 formative FA_6..FA_14 and 1 summative SA_2
INSERT INTO assessments (assessment_id, title, date_given, type) VALUES
  ('FA_6',  'Formative Assessment 6',  '2025-10-01', 'Formative'),
  ('FA_7',  'Formative Assessment 7',  '2025-10-02', 'Formative'),
  ('FA_8',  'Formative Assessment 8',  '2025-10-03', 'Formative'),
  ('FA_9',  'Formative Assessment 9',  '2025-10-04', 'Formative'),
  ('FA_10', 'Formative Assessment 10', '2025-10-05', 'Formative'),
  ('FA_11', 'Formative Assessment 11', '2025-10-06', 'Formative'),
  ('FA_12', 'Formative Assessment 12', '2025-10-07', 'Formative'),
  ('FA_13', 'Formative Assessment 13', '2025-10-08', 'Formative'),
  ('FA_14', 'Formative Assessment 14', '2025-10-09', 'Formative'),
  ('SA_2',  'Summative Assessment 2',  '2025-10-15', 'Summative');

-- 3) Scores for every new student on every new assessment (10 × 10 = 100 rows)
--    Uses CTE + CROSS JOIN to generate all combinations with reasonable scores.
INSERT INTO scores (student_id, assessment_id, score, status)
WITH new_students(sid) AS (
  VALUES (2001),(2002),(2003),(2004),(2005),
         (2006),(2007),(2008),(2009),(2010)
),
new_assessments(aid) AS (
  VALUES ('FA_6'),('FA_7'),('FA_8'),('FA_9'),('FA_10'),
         ('FA_11'),('FA_12'),('FA_13'),('FA_14'),('SA_2')
)
SELECT
  sid AS student_id,
  aid AS assessment_id,
  CASE
    WHEN substr(aid,1,2) = 'FA'
      THEN 2.5 + ((sid - 2000) % 4) * 0.5    -- 2.5, 3.0, 3.5, 4.0 pattern for formatives
    ELSE 3.0 + ((sid - 2000) % 3) * 0.3      -- 3.0, 3.3, 3.6 pattern for SA_2
  END AS score,
  'Recorded' AS status
FROM new_students
CROSS JOIN new_assessments;
