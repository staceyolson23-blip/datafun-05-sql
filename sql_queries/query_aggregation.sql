-- 1) Total rows in each table
SELECT 'students'   AS table_name, COUNT(*) AS row_count FROM students
UNION ALL
SELECT 'assessments', COUNT(*) FROM assessments
UNION ALL
SELECT 'scores',      COUNT(*) FROM scores;

-- 2) Overall average, min, max score
SELECT
  ROUND(AVG(score), 2) AS avg_score,
  MIN(score)           AS min_score,
  MAX(score)           AS max_score,
  COUNT(*)             AS num_scores
FROM scores
WHERE score IS NOT NULL;

-- 3) Average score per assessment (includes FA_X)
SELECT
  assessment_id,
  ROUND(AVG(score), 2) AS avg_score,
  COUNT(*)             AS num_scores
FROM scores
WHERE score IS NOT NULL
GROUP BY assessment_id
ORDER BY assessment_id;

-- 4) Sum of scores by student (illustrative)
SELECT
  student_id,
  ROUND(SUM(score), 2) AS total_points,
  COUNT(*)             AS assessments_taken
FROM scores
WHERE score IS NOT NULL
GROUP BY student_id
ORDER BY total_points DESC
LIMIT 10;
