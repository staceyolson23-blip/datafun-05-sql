# verify.py — quick checks for the FA/SA database
import sqlite3
from pathlib import Path

DB = Path("project.sqlite3")

def run_query(conn, sql, params=()):
    cur = conn.execute(sql, params)
    return cur.fetchall()

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        # 1) Show tables (sanity)
        tables = run_query(conn, "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        print("Tables:", [t[0] for t in tables])

        # 2) Row counts
        counts = run_query(conn, """
            SELECT 'students' AS t, COUNT(*) FROM students
            UNION ALL SELECT 'assessments', COUNT(*) FROM assessments
            UNION ALL SELECT 'scores', COUNT(*) FROM scores;
        """)
        print("Row counts:", counts)

        # 3) List assessments
        assessments = run_query(conn, """
            SELECT assessment_id, title, date_given, type
            FROM assessments
            ORDER BY date_given;
        """)
        print("\nAssessments:")
        for r in assessments:
            print(" ", r)

        # 4) Class average per assessment (+ NA count)
        averages = run_query(conn, """
            SELECT a.assessment_id,
                   ROUND(AVG(s.score),2) AS avg_score,
                   SUM(CASE WHEN s.status='NA' OR s.score IS NULL THEN 1 ELSE 0 END) AS na_count
            FROM assessments a
            LEFT JOIN scores s USING (assessment_id)
            GROUP BY a.assessment_id
            ORDER BY a.date_given;
        """)
        print("\nAverages & NA by assessment:")
        for r in averages:
            print(" ", r)

        # 5) Student growth: avg FA (FA_*) -> SA_1
        growth = run_query(conn, """
            WITH fa AS (
              SELECT student_id, AVG(score) AS avg_fa
              FROM scores
              WHERE assessment_id LIKE 'FA_%' AND status='Recorded'
              GROUP BY student_id
            ),
            sa AS (
              SELECT student_id, score AS sa1
              FROM scores
              WHERE assessment_id='SA_1' AND status='Recorded'
            )
            SELECT s.student_id,
                   ROUND(fa.avg_fa,2) AS avg_fa,
                   sa.sa1 AS sa1,
                   ROUND(sa.sa1 - fa.avg_fa,2) AS delta
            FROM students s
            LEFT JOIN fa USING(student_id)
            LEFT JOIN sa USING(student_id)
            ORDER BY delta DESC;
        """)
        print("\nGrowth (FA avg -> SA_1):")
        for r in growth:
            print(" ", r)

if __name__ == "__main__":
    main()
