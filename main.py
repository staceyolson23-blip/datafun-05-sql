import sqlite3
from pathlib import Path

# create or connect to database file
db_path = Path("datafun.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# insert sample data
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Ada", 20))
conn.commit()

# fetch and print rows
for row in cur.execute("SELECT * FROM students"):
    print(row)

conn.close()