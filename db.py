import sqlite3

def get_connection():
    conn = sqlite3.connect("/home/crow/Documents/CS_File/SEC_LABS/SQL_INJECTION/LAB1/users.db", check_same_thread=False)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            job TEXT,
            country TEXT,
            province TEXT,
            city TEXT,
            explanations TEXT
        );
    """)
    conn.commit()
    conn.close()
