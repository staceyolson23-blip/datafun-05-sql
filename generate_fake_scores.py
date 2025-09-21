import csv
from pathlib import Path
import random

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
OUTPUT = ROOT / "sql_create" / "03_insert_records.sql"

# Path to your students.csv
students_csv = DATA_DIR / "students.csv"

rows = []
with students_csv.open(newline="", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        sid = row["student_id"]
        # Random score between 2.0 and 4.0
        score = round(random.uniform(2.0, 4.0), 1)
        rows.append((sid, score))

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("-- Add fictional assessment\n")
    f.write(
        "INSERT INTO assessments (assessment_id, title, date_given, type) VALUES\n"
        "  ('FA_X','Fictional Formative','2025-09-30','Formative');\n\n"
    )
    f.write("-- Add fictional scores for each student\n")
    f.write("INSERT INTO scores (student_id, assessment_id, score, status) VALUES\n")
    values = [
        f"  ({sid}, 'FA_X', {score}, 'Recorded')" for sid, score in rows
    ]
    f.write(",\n".join(values))
    f.write(";\n")

print(f"Wrote {len(rows)} fake scores to {OUTPUT}")
