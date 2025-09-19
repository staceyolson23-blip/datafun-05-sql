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
```
datafun-05-sql/
├── .gitignore
├── .venv/                  # local virtual environment (not committed)
├── main.py                 # starter script
├── requirements.txt
└── README.md
```

---

## 🔗 References
- Python sqlite3 docs: https://docs.python.org/3/library/sqlite3.html  
- SQLite docs: https://www.sqlite.org/docs.html  
- Python venv docs: https://docs.python.org/3/library/venv.html  
- pip user guide: https://pip.pypa.io/en/stable/user_guide/  
- Markdown guide: https://www.markdownguide.org/