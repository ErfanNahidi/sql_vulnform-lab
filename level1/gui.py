import streamlit as st
import backend
import db

db.create_table()
db.insert_default_users()

st.title("User Management (SQL Injection Vulnerable)")

st.header("Add New User")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
job = st.text_input("Job")
country = st.text_input("Country")
province = st.text_input("Province")
city = st.text_input("City")
explanations = st.text_area("Explanations")

if st.button("Save User"):
    try:
        backend.save_to_db(first_name, last_name, job, country, province, city, explanations)
        st.success("User saved successfully.")
    except Exception as e:
        st.error(f"Error saving user: {e}")

st.header("Search Users by City")
search_city = st.text_input("City to search")

if st.button("Search"):
    results = backend.search_by_city(search_city)
    if results:
        for r in results:
            st.write(f"{r[1]} {r[2]}, Job: {r[3]}, Country: {r[4]}, Province: {r[5]}, City: {r[6]}, Notes: {r[7]}")
    else:
        st.write("No users found.")
