import sqlite3

def get_connection():
    return sqlite3.connect("level2.db", check_same_thread=False)

def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def insert_default_users():
    conn = get_connection()
    cursor = conn.cursor()
    
    users = [
        ("admin", "admin123"),
        ("erfan", "123456"),
        ("test", "pass")
    ]
    
    for user in users:
        username, password = user
        query = f"""
            INSERT OR IGNORE INTO users (username, password)
            VALUES ('{username}', '{password}');
        """
        cursor.execute(query)
    
    conn.commit()
    conn.close()
