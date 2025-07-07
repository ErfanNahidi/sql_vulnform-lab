import db

# Ensure table and default users exist
db.create_user_table()
db.insert_default_users()

def authenticate(username, password):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
