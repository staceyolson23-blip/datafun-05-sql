print("RUNNING:", __file__)

# db01_setup.py
import sqlite3, pathlib, sys
from datetime import datetime

ROOT = pathlib.Path(__file__).parent
DB = ROOT / "project.sqlite3"
DIR = ROOT / "sql_create"
ORDER = [
    "00_drop_tables.sql",
    "01_create_tables.sql",
    # "02_alter_tables.sql",
    "03_insert_records.sql",
]

def run_sql_file(conn: sqlite3.Connection, path: pathlib.Path):
    print(f"→ Running {path.name}")
    with path.open("r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    start = datetime.now()
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("BEGIN;")
        try:
            for name in ORDER:
                p = DIR / name
                if not p.exists():
                    print(f"∙ (skip) {name} not found")
                    continue
                run_sql_file(conn, p)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("! Setup failed, rolled back.", file=sys.stderr)
            raise

        # sanity check
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()]
        print("\nTables:", tables)
        for t in tables:
            # skip sqlite internal tables that error on COUNT(*)
            if t.startswith("sqlite_"): 
                continue
            cnt = conn.execute(f"SELECT COUNT(*) FROM {t};").fetchone()[0]
            print(f"  {t:<12} rows: {cnt}")

    elapsed = (datetime.now() - start).total_seconds()
    print(f"\nRebuilt schema & seed in {DB} ({elapsed:.2f}s)")

if __name__ == "__main__":
    main()
