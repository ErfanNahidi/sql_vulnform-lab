import sqlite3

def get_connection():
    return sqlite3.connect("level1.db", check_same_thread=False)

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

def insert_default_users():
    conn = get_connection()
    cursor = conn.cursor()
    users = [
        ("Erfan", "Nahidi", "Student", "Iran", "Alborz", "Karaj", "No explanation"),
        ("Ali", "Ahmadi", "Engineer", "Iran", "Tehran", "Tehran", "Works at company X"),
        ("Sara", "Mohammadi", "Doctor", "Iran", "Isfahan", "Isfahan", "Specialist in Y")
    ]
    for user in users:
        cursor.execute("""
            INSERT OR IGNORE INTO users (first_name, last_name, job, country, province, city, explanations)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, user)
    conn.commit()
    conn.close()
