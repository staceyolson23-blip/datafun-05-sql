from pathlib import Path
import sqlite3

DB = Path("school_db.sqlite")
SQL_DIR = Path("sql_create")

def run_sql_file(conn, path: Path):
    with open(path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        # Create the tables
        run_sql_file(conn, SQL_DIR / "01_create_tables.sql")
        # Add the extra column (safe to run even if already added)
        run_sql_file(conn, SQL_DIR / "02_alter_tables.sql")

        # Quick sanity check: list tables
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        print("Tables:", [t[0] for t in tables])

if __name__ == "__main__":
    main()
