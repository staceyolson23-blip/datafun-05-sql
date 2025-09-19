# datafun-05-sql
**Author:** Stacey Olson  
**Date:** September 18, 2025

---

## 📌 Overview
This project is part of **CC5.1: Start a Python/SQL Project**.  
It demonstrates how to use Python and SQL together to:

- Create and connect to a local SQLite database  
- Create tables and insert data using SQL  
- Query and display results  
- Manage project dependencies and virtual environments  

The goal is to practice building clean, repeatable Python data projects.

---

## ⚙️ Setup Instructions
Follow these steps to run this project on your local machine.

### 1) Clone this repository
```bash
cd ~/Repos
git clone https://github.com/staceyolson23-blip/datafun-05-sql.git
cd datafun-05-sql
```

### 2) Create and activate a virtual environment
**Mac or Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate
```

### 3) Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ How to Run
Run the main script to create the database, add records, and print them.
```bash
python main.py
```

**Expected output:**
```
(1, 'Ada', 20)
(2, 'Grace', 22)
(3, 'Lin', 19)
```

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
│   ├── standards.csv          # sample standards data
│   └── assessments.csv         # sample assessments data
│
├── sql_create/
│   ├── 01_create_tables.sql    # creates standards & assessments tables
│   └── 02_alter_tables.sql     # adds is_mastery column to assessments
│
├── .gitignore
├── .venv/                      # local virtual environment (not committed)
├── main.py                     # creates tables and runs SQL files
├── load_csv.py                 # loads CSV data into the database
├── verify.py                   # runs a JOIN query to verify relationships
├── requirements.txt
├── school_db.sqlite            # local SQLite database (not committed)
└── README.md

---

## 🗃️ Database Overview (CC5.2)

This project now includes a **school database** (`school_db.sqlite`) with two related tables:

### standards
- `standard_id` (TEXT, primary key — GUID)
- `code` (TEXT — like 8.EE.5)
- `domain` (TEXT — category of the standard)
- `description` (TEXT — full explanation)

### assessments
- `assessment_id` (TEXT, primary key — GUID)
- `title` (TEXT — name of the assessment)
- `date_given` (TEXT — stored as YYYYMMDD)
- `standard_id` (TEXT, foreign key → standards.standard_id)
- `is_mastery` (INTEGER — added later with ALTER TABLE, default 0)

This creates a **one-to-many (1:M)** relationship:  
- Each **standard** can have many **assessments**  
- Each **assessment** is linked to exactly one **standard**

### Data Sources
- CSV files in `/data/` folder  
  - `standards.csv` — list of three sample math standards  
  - `assessments.csv` — three assessments linked to those standards

### How to Load Data
Run this in the terminal:

    python3 load_csv.py

### How to Verify
Run this in the terminal:

    python3 verify.py

This prints a joined table of assessments and their related standards.

---

## 🔗 References
- Python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html  
- SQLite docs: https://www.sqlite.org/docs.html  
- Python venv docs: https://docs.python.org/3/library/venv.html  
- pip user guide: https://pip.pypa.io/en/stable/user_guide/  
- Markdown guide: https://www.markdownguide.org/