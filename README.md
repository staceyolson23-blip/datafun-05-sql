# datafun-05-sql
**Author:** Stacey Olson  
**Date:** September 18, 2025  

---

## 📌 Overview
This project is part of **CC5.1–CC5.4: Python + SQL**.  
It demonstrates how to use Python and SQL together to:

- Create and connect to a local SQLite database  
- Define tables for students, assessments, and scores  
- Insert anonymized classroom data from CSV files  
- Run update and delete operations with SQL scripts  
- Query, filter, sort, group, and join data  
- Execute SQL from Python and summarize results  
- Manage project dependencies and virtual environments  

The goal is to practice building clean, repeatable Python data projects.

---

## ⚙️ Setup Instructions
Follow these steps to run this project on your local machine.

### 1) Clone this repository
    cd ~/Repos
    git clone https://github.com/staceyolson23-blip/datafun-05-sql.git
    cd datafun-05-sql

### 2) Create and activate a virtual environment
Mac or Linux:
    python3 -m venv .venv
    source .venv/bin/activate

Windows PowerShell:
    python3 -m venv .venv
    .venv\Scripts\Activate

### 3) Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

---

## ▶️ How to Run (order matters)

Rebuild schema (drops/recreates tables and adds any static inserts):
    python3 db01_setup.py

Load real CSV data:
    python3 init_db.py

Clean & feature engineering (updates, deletes, derived columns, summary table):
    python3 db02_features.py

Run example queries (aggregation, filter, sort, group, joins) and preview results:
    python3 db03_queries.py

(Optional) Quick verification script:
    python3 verify.py

---

## 🧠 Skills Practiced
- Using `sqlite3` from the Python Standard Library  
- Writing and executing SQL from Python  
- Aggregation (COUNT, AVG, SUM, MIN, MAX)  
- Filtering (WHERE), Sorting (ORDER BY), Grouping (GROUP BY), Joining (INNER/LEFT JOIN)  
- Updates and deletes via standalone SQL scripts  
- Clean project structure, virtual environments, and documentation  

---

## 📂 Project Structure
    datafun-05-sql/
    ├── data/
    │   ├── students.csv         # anonymized student list
    │   ├── assessments.csv      # FA_2–FA_5 and SA_1 Geometry assessments
    │   └── scores.csv           # student scores by assessment
    │
    ├── sql_create/
    │   ├── 00_drop_tables.sql
    │   ├── 01_create_tables.sql
    │   ├── 02_alter_tables.sql
    │   └── 03_insert_records.sql    # adds a fictional assessment FA_X (no scores)
    │
    ├── sql_features/
    │   ├── update_records.sql       # example UPDATEs (status fixes, floor low formative scores)
    │   └── delete_records.sql       # example DELETEs (remove truly missing scores)
    │
    ├── sql_queries/
    │   ├── query_aggregation.sql
    │   ├── query_filter.sql
    │   ├── query_sorting.sql
    │   ├── query_group_by.sql
    │   └── query_join.sql
    │
    ├── archive/                     # old or unused files
    ├── db01_setup.py
    ├── db02_features.py
    ├── db03_queries.py
    ├── generate_fake_scores.py
    ├── init_db.py
    ├── main.py
    ├── verify.py
    ├── requirements.txt
    ├── .gitignore
    ├── project.sqlite3              # local SQLite DB (ignored by git)
    └── README.md

---

## 🗃️ Database Overview

This project uses a **3-table schema**:

### students
- `student_id` (INTEGER, PK)  
- `grade_level` (INTEGER)  

### assessments
- `assessment_id` (TEXT, PK, like FA_2, SA_1)  
- `title` (TEXT)  
- `date_given` (TEXT, YYYY-MM-DD)  
- `type` (TEXT: Formative / Summative)  

### scores
- `student_id` (FK → students.student_id)  
- `assessment_id` (FK → assessments.assessment_id)  
- `score` (REAL, 0–4 scale)  
- `status` (TEXT: Recorded / Missing, etc.)  
- **PRIMARY KEY (student_id, assessment_id)**  

**Relationships:**  
- One student → many scores  
- One assessment → many scores  

---

## 📖 Narrative of the Data

The dataset models a simplified middle school classroom:

- **Students** are anonymized with numeric IDs (1–22), all in grade level 7.  
- **Assessments** include four *Formative Assessments* (FA_2–FA_5) and one *Summative Assessment* (SA_1) from a geometry unit. Each record includes a type and administration date.  
- **Scores** capture performance on a 0–4 proficiency scale (standards-based rubric):
  - 4.0 = Advanced mastery  
  - 3.0 = Proficient  
  - 2.0 = Developing  
  - 0 or NULL = Missing/No evidence  

For demonstration, `03_insert_records.sql` adds a **fictional formative assessment** `FA_X` so you can show how to insert new records. (Scores for `FA_X` are *not* preloaded; see `db02_features.py` for feature operations.)

This structure supports questions like:
- How do formative averages compare to summative averages?  
- Which students are below proficiency and need support?  
- Which assessments have the most variability?  
- What is each student’s overall average across assessments?

---

## 📊 Example Findings (after `db02_features.py`)
These will vary with data, but typical outputs include:

- **Row counts:** ~22 students, 6 assessments (incl. FA_X), and 107 scores after cleaning  
- **Averages:** Formative ≈ 3.19, Summative ≈ 3.41  
- **Engineered buckets (`score_bucket`):** Below Basic, Basic, Proficient, Advanced  
- **Top student by average:** e.g., ID 19 with 4.0 (from sample run)

---

## ✅ Notes
- Ensure `project.sqlite3` is ignored by git (see `.gitignore`).  
- Re-run in order (`db01_setup.py` → `init_db.py` → `db02_features.py` → `db03_queries.py`) whenever you change schema or data.  
- SQLite has **no RIGHT JOIN**; use a LEFT JOIN with tables swapped.

---

## 🔗 References
- Python sqlite3: https://docs.python.org/3/library/sqlite3.html  
- SQLite: https://www.sqlite.org/docs.html  
- Python venv: https://docs.python.org/3/library/venv.html  
- pip user guide: https://pip.pypa.io/en/stable/user_guide/  
- Markdown guide: https://www.markdownguide.org/
