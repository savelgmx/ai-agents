import streamlit as st
import requests

st.title("AI Dev")

feature = st.text_input("Feature")

if st.button("Generate"):

    response = requests.post(
        "http://localhost:8000/run",
        json={"feature": feature}
    )

    data = response.json()

    st.session_state["changes"] = data["changes"]


if "changes" in st.session_state:

    for change in st.session_state["changes"]:
        st.subheader(change["file"])
        st.code(change["code"], language="kotlin")

    if st.button("Approve"):

        requests.post("http://localhost:8000/approve")

        st.success("Applied!")
