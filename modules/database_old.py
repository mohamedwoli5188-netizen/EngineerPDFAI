import sqlite3

DB_FILE = "projects.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        contract_number TEXT,
        employer TEXT,
        contractor TEXT,
        contract_amount REAL,
        base_date TEXT,
        created_at TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS coefficients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        A REAL,
        b REAL,
        c REAL,
        d REAL,
        e REAL
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material TEXT,
        base_value REAL,
        current_value REAL,
        base_date TEXT,
        current_date TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ipc_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        ipc_no TEXT,
        ipc_amount REAL,
        pn REAL,
        escalation REAL,
        date TEXT
    )
    """)


    conn.commit()
    conn.close()
