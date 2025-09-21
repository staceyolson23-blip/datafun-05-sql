import sqlite3

DB = "project.sqlite3"

with sqlite3.connect(DB) as conn:
    conn.execute("PRAGMA foreign_keys = ON;")
    
    print("\n--- Table counts ---")
    for row in conn.execute("""
        SELECT 'students' AS table_name, COUNT(*) FROM students
        UNION ALL
        SELECT 'assessments', COUNT(*) FROM assessments
        UNION ALL
        SELECT 'scores', COUNT(*) FROM scores;
    """):
        print(row)
    
    print("\n--- Assessment averages + NA ---")
    for row in conn.execute("""
        SELECT a.assessment_id, a.title, a.type, a.date_given,
               ROUND(AVG(s.score),2) AS avg_score,
               SUM(CASE WHEN s.status='NA' OR s.score IS NULL THEN 1 ELSE 0 END) AS na_count
        FROM assessments a
        LEFT JOIN scores s USING (assessment_id)
        GROUP BY a.assessment_id
        ORDER BY a.date_given;
    """):
        print(row)
