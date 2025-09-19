import sqlite3

with sqlite3.connect("school_db.sqlite") as conn:
    conn.execute("PRAGMA foreign_keys = ON;")
    rows = conn.execute("""
        SELECT a.assessment_id,
               a.title,
               a.date_given,
               s.code AS standard_code,
               s.domain
        FROM assessments a
        JOIN standards s
          ON a.standard_id = s.standard_id
        ORDER BY a.date_given;
    """).fetchall()

for r in rows:
    print(r)
