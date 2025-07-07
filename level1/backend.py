import db

def save_to_db(first_name, last_name, job, country, province, city, explanations):
    db.create_table()  # Ensures table exists
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (first_name, last_name, job, country, province, city, explanations)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (first_name, last_name, job, country, province, city, explanations))
    conn.commit()
    conn.close()
