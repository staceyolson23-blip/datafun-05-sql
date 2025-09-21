# db03_queries.py
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"
QDIR = ROOT / "sql_queries"

FILES = [
    "query_aggregation.sql",
    "query_filter.sql",
    "query_sorting.sql",
    "query_group_by.sql",
    "query_join.sql",
]

def run_sql_file(conn: sqlite3.Connection, path: Path):
    sql_text = path.read_text(encoding="utf-8")
    # Split on semicolons while keeping simple (SQLite-friendly)
    statements = [s.strip() for s in sql_text.split(";") if s.strip()]
    cur = conn.cursor()
    for stmt in statements:
        print(f"\n--- {path.name} ---")
        # Show a shortened preview of the statement
        preview = " ".join(stmt.split())
        print(f"> {preview[:120]}{'...' if len(preview) > 120 else ''}")
        try:
            cur.execute(stmt)
            rows = cur.fetchall()
            if cur.description:  # query returned a resultset
                headers = [d[0] for d in cur.description]
                print(" | ".join(headers))
                for r in rows[:25]:  # cap preview at 25 rows
                    print(" | ".join("" if v is None else str(v) for v in r))
                if len(rows) > 25:
                    print(f"... ({len(rows) - 25} more rows)")
            else:
                print("(no result set)")
        except sqlite3.Error as e:
            print(f"! ERROR: {e}")

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        for name in FILES:
            path = QDIR / name
            if not path.exists():
                print(f"\n--- {name} ---")
                print(f"! Skipped: {name} not found")
                continue
            run_sql_file(conn, path)

if __name__ == "__main__":
    main()
