import sqlite3
from pathlib import Path

DB_PATH = Path("database.sqlite")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
