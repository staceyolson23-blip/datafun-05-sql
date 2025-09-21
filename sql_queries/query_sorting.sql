-- 1) Top 10 highest scores on SA_1
SELECT student_id, score
FROM scores
WHERE assessment_id = 'SA_1'
ORDER BY score DESC, student_id ASC
LIMIT 10;

-- 2) Bottom 10 scores across all assessments
SELECT student_id, assessment_id, score
FROM scores
WHERE score IS NOT NULL
ORDER BY score ASC, student_id ASC
LIMIT 10;

-- 3) Students sorted by average score (desc)
SELECT
  student_id,
  ROUND(AVG(score), 2) AS avg_score,
  COUNT(*)             AS assessments_taken
FROM scores
WHERE score IS NOT NULL
GROUP BY student_id
ORDER BY avg_score DESC, assessments_taken DESC, student_id ASC
LIMIT 10;
