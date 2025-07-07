import streamlit as st
import db
import sqlite3

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

def vulnerable_authenticate(username, password):
    conn = db.get_connection()
    cursor = conn.cursor()

    query = f"""
        SELECT * FROM users
        WHERE username = '{username}' AND password = '{password}';
    """

    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user 

if st.button("Login"):
    user = vulnerable_authenticate(username, password)
    if user:
        st.success("Login successful!")
        st.subheader("Dashboard")
        st.write(user)  # نمایش رکورد دریافتی
    else:
        st.error("Invalid username or password.")


