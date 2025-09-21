# load_csv.py  — loads the NEW CSVs into project.sqlite3
import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
DB = ROOT / "project.sqlite3"          # ✅ new DB
DATA = ROOT / "data"                   # students.csv, assessments.csv, scores.csv

def load_df(df: pd.DataFrame, table: str):
    with sqlite3.connect(DB) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        df.to_sql(table, conn, if_exists="append", index=False)

def main():
    # --- students ---
    students = pd.read_csv(DATA / "students.csv", dtype={"student_id": "int64", "grade_level": "int64"})
    # --- assessments ---
    assessments = pd.read_csv(DATA / "assessments.csv", dtype={"assessment_id": "string", "title": "string", "date_given": "string", "type": "string"})
    # --- scores ---
    # Blank score => NaN -> becomes NULL in SQLite (good for NA)
    scores = pd.read_csv(DATA / "scores.csv", dtype={"student_id": "int64", "assessment_id": "string", "status": "string"})
    # ensure numeric (coerce blanks to NaN)
    scores["score"] = pd.to_numeric(scores["score"], errors="coerce")

    load_df(students, "students")
    load_df(assessments, "assessments")
    load_df(scores, "scores")

    print("✅ CSV data loaded into project.sqlite3")

if __name__ == "__main__":
    main()
