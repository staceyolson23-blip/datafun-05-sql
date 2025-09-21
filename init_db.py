import sqlite3, csv
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"
DATA_DIR = ROOT / "data"

def load_csv(conn, table, csv_path, cols):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows = [tuple((row[c] if row[c] != "" else None) for c in cols) for row in rdr]
    placeholders = ",".join("?" * len(cols))
    sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
    conn.executemany(sql, rows)

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        # Load CSV data
        load_csv(conn, "students",    DATA_DIR / "students.csv",    ["student_id","grade_level"])
        load_csv(conn, "assessments", DATA_DIR / "assessments.csv", ["assessment_id","title","date_given","type"])
        load_csv(conn, "scores",      DATA_DIR / "scores.csv",      ["student_id","assessment_id","score","status"])
        conn.commit()

        # NEW: print row counts
        for table in ["students","assessments","scores"]:
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"{table:12} rows: {count}")

if __name__ == "__main__":
    main()
