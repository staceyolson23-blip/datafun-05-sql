# main.py  — sanity checks for the FA/SA database
from pathlib import Path
import sqlite3

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"
SQL_DIR = ROOT / "sql_create"

def run_sql_file(conn, path: Path):
    with path.open("r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        # (Re)create tables if needed. Safe to run.
        run_sql_file(conn, SQL_DIR / "01_create_tables.sql")

        # --- Quick sanity checks ---
        print("\nTables present:")
        for (name,) in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ):
            print("  •", name)

        print("\nRow counts:")
        for (label, cnt) in conn.execute("""
            SELECT 'students' AS t, COUNT(*) FROM students
            UNION ALL
            SELECT 'assessments', COUNT(*) FROM assessments
            UNION ALL
            SELECT 'scores', COUNT(*) FROM scores
        """):
            print(f"  {label:11} {cnt}")

        print("\nClass average per assessment:")
        for row in conn.execute("""
            SELECT a.assessment_id, a.title,
                   ROUND(AVG(s.score),2) AS avg_score,
                   SUM(CASE WHEN s.status='NA' OR s.score IS NULL THEN 1 ELSE 0 END) AS na_count
            FROM assessments a
            LEFT JOIN scores s USING (assessment_id)
            GROUP BY a.assessment_id
            ORDER BY a.date_given;
        """):
            print("  ", row)

if __name__ == "__main__":
    main()
