import sqlite3, csv
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"
SCHEMA = ROOT / "sql_create" / "01_create_tables.sql"
DATA_DIR = ROOT / "data"

def run_sql(conn, path: Path):
    with path.open("r", encoding="utf-8") as f:
        conn.executescript(f.read())

def load_csv(conn, table, csv_path, cols):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows = [tuple((row[c] if row[c] != "" else None) for c in cols) for row in rdr]
    placeholders = ",".join("?" * len(cols))
    sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
    conn.executemany(sql, rows)

def main():
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON;")
    run_sql(conn, SCHEMA)

    load_csv(conn, "students",    DATA_DIR / "students.csv",    ["student_id","grade_level"])
    load_csv(conn, "assessments", DATA_DIR / "assessments.csv", ["assessment_id","title","date_given","type"])
    load_csv(conn, "scores",      DATA_DIR / "scores.csv",      ["student_id","assessment_id","score","status"])

    # sanity print: what tables exist now?
    print(conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall())

    # Debug: print tables
    print(conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall())

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB.resolve()}")

    
if __name__ == "__main__":
    main()
