-- 1) Formative scores below 2.5
SELECT sc.student_id, sc.assessment_id, sc.score
FROM scores sc
JOIN assessments a ON a.assessment_id = sc.assessment_id
WHERE a.type = 'Formative'
  AND sc.score IS NOT NULL
  AND sc.score < 2.5
ORDER BY sc.student_id, sc.assessment_id;

-- 2) Missing or zero scores (data quality check)
SELECT student_id, assessment_id, score, status
FROM scores
WHERE score IS NULL OR score = 0
ORDER BY student_id, assessment_id;

-- 3) Only the fictional FA_X rows (quick filter demo)
SELECT student_id, score
FROM scores
WHERE assessment_id = 'FA_X'
ORDER BY student_id;
