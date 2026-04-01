import streamlit as st
import requests

st.title("🤖 AI Android Dev Factory")

feature = st.text_input("Enter feature or task")

if st.button("Run"):

    response = requests.post(
        "http://localhost:8000/run",
        json={"feature": feature}
    )

    data = response.json()

    st.subheader("Changes")

    for change in data.get("changes", []):
        st.code(change["code"], language="kotlin")
