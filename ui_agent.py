# ui.py
import streamlit as st
from orchestrator import run_full_pipeline

st.title("AI Android Dev")

feature = st.text_input("Feature")

if st.button("Run"):
    run_full_pipeline(feature)

    with open("logs/agent.log") as f:
        st.text(f.read())

def get_user_request():

    feature = input("Enter feature:\n")

    return {
        "feature": feature

    }
@app.post("/run")
def run(data: dict):

    return run_full_pipeline(data["feature"])
