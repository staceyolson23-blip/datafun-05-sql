-- 1) Average score by assessment (classic GROUP BY)
SELECT
  assessment_id,
  ROUND(AVG(score), 2) AS avg_score,
  COUNT(*)             AS num_scores
FROM scores
WHERE score IS NOT NULL
GROUP BY assessment_id
ORDER BY assessment_id;

-- 2) Average score by assessment *type* (Formative vs Summative)
SELECT
  a.type,
  ROUND(AVG(sc.score), 2) AS avg_score,
  COUNT(*)                AS num_scores
FROM scores sc
JOIN assessments a ON a.assessment_id = sc.assessment_id
WHERE sc.score IS NOT NULL
GROUP BY a.type
ORDER BY a.type;

-- 3) Average SA_1 by grade level (multi-table GROUP BY)
SELECT
  st.grade_level,
  ROUND(AVG(sc.score), 2) AS sa1_avg,
  COUNT(*)                AS num_scores
FROM scores sc
JOIN students st    ON st.student_id = sc.student_id
WHERE sc.assessment_id = 'SA_1' AND sc.score IS NOT NULL
GROUP BY st.grade_level
ORDER BY st.grade_level;

-- 4) Counts by status (Recorded/Missing/etc.)
SELECT status, COUNT(*) AS rows_per_status
FROM scores
GROUP BY status
ORDER BY rows_per_status DESC;

-- 5) (If you've run db02_features.py) counts by engineered bucket
-- Safe to run even if the column isn't present — it will just fail this one query.
SELECT score_bucket, COUNT(*) AS rows_per_bucket
FROM scores
GROUP BY score_bucket
ORDER BY rows_per_bucket DESC;
