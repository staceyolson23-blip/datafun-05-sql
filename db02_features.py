# db02_features.py
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"
FEATURES_DIR = ROOT / "sql_features"

def run_sql_file(conn: sqlite3.Connection, path: Path):
    with path.open("r", encoding="utf-8") as f:
        conn.executescript(f.read())

def column_exists(conn: sqlite3.Connection, table: str, column: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table});").fetchall()
    return any(r[1] == column for r in rows)  # r[1] is column name

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        # --- Before stats
        total_before = conn.execute("SELECT COUNT(*) FROM scores;").fetchone()[0]
        null_scores_before = conn.execute("SELECT COUNT(*) FROM scores WHERE score IS NULL;").fetchone()[0]
        print(f"Before updates  | scores: {total_before}  | NULL scores: {null_scores_before}")

        # --- Run feature SQL scripts (update + delete)
        run_sql_file(conn, FEATURES_DIR / "update_records.sql")
        run_sql_file(conn, FEATURES_DIR / "delete_records.sql")
        conn.commit()

        # --- After update/delete stats
        total_after = conn.execute("SELECT COUNT(*) FROM scores;").fetchone()[0]
        null_scores_after = conn.execute("SELECT COUNT(*) FROM scores WHERE score IS NULL;").fetchone()[0]
        print(f"After updates   | scores: {total_after}  | NULL scores: {null_scores_after}")

        # --- Feature engineering 1: add a derived column if missing
        if not column_exists(conn, "scores", "score_bucket"):
            conn.execute("ALTER TABLE scores ADD COLUMN score_bucket TEXT;")
        conn.execute("""
            UPDATE scores
            SET score_bucket = CASE
                WHEN score IS NULL         THEN 'Missing'
                WHEN score < 2.5           THEN 'Below Basic'
                WHEN score < 3.0           THEN 'Basic'
                WHEN score < 3.5           THEN 'Proficient'
                ELSE 'Advanced'
            END;
        """)

        # --- Feature engineering 2: create a fresh summary table
        conn.execute("DROP TABLE IF EXISTS student_summary;")
        conn.execute("""
            CREATE TABLE student_summary AS
            SELECT
                s.student_id,
                ROUND(AVG(sc.score), 2) AS avg_score,
                COUNT(sc.assessment_id) AS assessments_taken
            FROM students s
            JOIN scores sc ON sc.student_id = s.student_id
            WHERE sc.score IS NOT NULL
            GROUP BY s.student_id;
        """)
        conn.commit()

        # --- Small preview
        sample = conn.execute("SELECT * FROM student_summary ORDER BY avg_score DESC, student_id LIMIT 5;").fetchall()
        print("Top 5 by avg_score:", sample)

if __name__ == "__main__":
    main()
