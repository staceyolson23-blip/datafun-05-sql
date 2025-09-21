-- query_join.sql

-- 1) INNER JOIN: student, assessment info, and score
-- Only returns rows where matches exist in all three tables
SELECT st.student_id,
       a.assessment_id,
       a.title,
       a.type,
       a.date_given,
       sc.score,
       sc.status
FROM scores sc
JOIN students st ON st.student_id = sc.student_id
JOIN assessments a ON a.assessment_id = sc.assessment_id
ORDER BY st.student_id, a.assessment_id;

-- 2) LEFT JOIN: all students, even if they have no scores
-- Useful to see who is missing assessments
SELECT st.student_id,
       COUNT(sc.assessment_id) AS assessments_taken,
       ROUND(AVG(sc.score), 2) AS avg_score
FROM students st
LEFT JOIN scores sc ON st.student_id = sc.student_id
GROUP BY st.student_id
ORDER BY st.student_id;

-- 3) LEFT JOIN: all assessments, even if no one has a score yet
-- Useful to detect assessments without submissions (like FA_X)
SELECT a.assessment_id,
       a.title,
       a.type,
       COUNT(sc.student_id) AS num_scores,
       ROUND(AVG(sc.score), 2) AS avg_score
FROM assessments a
LEFT JOIN scores sc ON a.assessment_id = sc.assessment_id
GROUP BY a.assessment_id
ORDER BY a.assessment_id;

-- 4) RIGHT JOIN (not supported in SQLite)
-- NOTE: SQLite does not support RIGHT JOIN. 
-- If you need it, swap the table order in a LEFT JOIN.
