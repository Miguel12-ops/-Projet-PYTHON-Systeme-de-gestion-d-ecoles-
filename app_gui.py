
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Gestion de l'école")

menu = ["Classes", "Étudiants", "Notes", "Statistiques"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Classes":
    st.subheader("Créer une classe")
    class_id = st.text_input("ID de la classe")
    class_name = st.text_input("Nom de la classe")
    if st.button("Créer"):
        res = requests.post(f"{API_URL}/classes", params={"id": class_id}, json={"name": class_name})
        st.write(res.json())

    st.subheader("Liste des classes")
    res = requests.get(f"{API_URL}/classes")
    st.write(res.json())

elif choice == "Étudiants":
    st.subheader("Créer un étudiant")
    student_id = st.text_input("ID étudiant")
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom")
    email = st.text_input("Email")
    if st.button("Créer étudiant"):
        res = requests.post(f"{API_URL}/students", params={"id": student_id}, json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        })
        st.write(res.json())
