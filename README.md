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
- Query and verify results with Python scripts  
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

## ▶️ How to Run

Build the database:
    python3 init_db.py

Verify results:
    python3 verify.py

This prints table counts, averages per assessment, and FA→SA growth.

---

## 🧠 Skills Practiced
- Using sqlite3 from the Python Standard Library  
- Writing SQL statements inside Python scripts  
- Managing environments and dependencies with venv and pip  
- Following a clean, professional project structure  
- Writing clear Markdown documentation  

---

## 📂 Project Structure
    datafun-05-sql/
    ├── data/
    │   ├── students.csv       # anonymized student list
    │   ├── assessments.csv    # FA_2–FA_5 and SA_1 Geometry assessments
    │   └── scores.csv         # student scores by assessment
    │
    ├── sql_create/
    │   └── 01_create_tables.sql   # defines students, assessments, scores
    │
    ├── .gitignore
    ├── init_db.py              # rebuilds DB and loads CSVs
    ├── verify.py               # checks table counts, averages, growth
    ├── requirements.txt
    ├── project.sqlite3         # local SQLite database (not committed)
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
- **PRIMARY KEY (student_id, assessment_id)**  

**Relationships:**  
- One student → many scores  
- One assessment → many scores  

### How to Load Data
    python3 init_db.py

### How to Verify
    python3 verify.py

---

## 🗂 Archived / Removed
- `sql_create/02_alter_tables.sql` — not used  
- `load_csv.py` — replaced by `init_db.py`  
- Old databases (`school_db.sqlite`, `datafun.db`) — archived  

---

## 🔗 References
- Python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html  
- SQLite docs: https://www.sqlite.org/docs.html  
- Python venv docs: https://docs.python.org/3/library/venv.html  
- pip user guide: https://pip.pypa.io/en/stable/user_guide/  
- Markdown guide: https://www.markdownguide.org/
