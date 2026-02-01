
import sqlite3
from contextlib import contextmanager
from pathlib import Path


DB_PATH = (Path(__file__).resolve().parent.parent / "northwind.sqlite").as_posix()

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # access columns by name
    try:
        yield conn
    finally:
        conn.close()