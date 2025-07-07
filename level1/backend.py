import db

def save_to_db(first_name, last_name, job, country, province, city, explanations):
    conn = db.get_connection()
    cursor = conn.cursor()

    # ناامن: رشته SQL با جایگذاری مستقیم (SQL Injection)
    query = f"""
        INSERT INTO users (first_name, last_name, job, country, province, city, explanations)
        VALUES ('{first_name}', '{last_name}', '{job}', '{country}', '{province}', '{city}', '{explanations}');
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

def search_by_city(city):
    conn = db.get_connection()
    cursor = conn.cursor()

    # ناامن: جستجو با جایگذاری مستقیم رشته
    query = f"SELECT * FROM users WHERE city = '{city}';"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
