import sqlite3
from pathlib import Path
import pandas as pd

DB = Path("school_db.sqlite")
DATA = Path("data")

def load_table(csv_name: str, table_name: str):
    df = pd.read_csv(DATA / csv_name)
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        df.to_sql(table_name, conn, if_exists="append", index=False)

if __name__ == "__main__":
    load_table("standards.csv", "standards")
    load_table("assessments.csv", "assessments")
    print("✅ CSV data loaded into database.")
