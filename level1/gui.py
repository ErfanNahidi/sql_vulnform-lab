import streamlit as st
import backend

st.title("User Information Form")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
job = st.text_input("Job")

country = st.selectbox("Country", ["Iran"])

province_city_map = {
    "Tehran": ["Tehran", "Rey", "Shemiranat", "Eslamshahr"],
    "Isfahan": ["Isfahan", "Kashan", "Najafabad", "Shahreza"],
    "Fars": ["Shiraz", "Marvdasht", "Jahrom", "Fasa"],
    "Khorasan Razavi": ["Mashhad", "Neyshabur", "Sabzevar", "Bojnurd"],
    "East Azerbaijan": ["Tabriz", "Maragheh", "Mianeh", "Ahar"],
}

province = st.selectbox("Province", list(province_city_map.keys()))
city = st.selectbox("City", province_city_map[province])

explanations = st.text_area("Explanations", height=150)

if st.button("Submit"):
    backend.save_to_db(first_name, last_name, job, country, province, city, explanations)
    st.success("Information saved successfully!")