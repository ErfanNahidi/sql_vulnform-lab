import streamlit as st
import backend

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if backend.authenticate(username, password):
        st.success("Login successful!")
        st.subheader("Dashboard")
        st.write("Welcome to the secure area.")
    else:
        st.error("Invalid username or password.")