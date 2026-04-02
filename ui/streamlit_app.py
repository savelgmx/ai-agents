import streamlit as st
import requests

st.title("🚀 AI Dev PR System")

feature = st.text_input("Feature")

if st.button("Create PR"):

    res = requests.post(
        "http://localhost:8000/run",
        json={"feature": feature}
    )

    st.session_state["changes"] = res.json()["changes"]


# --- DIFF VIEW ---
if "changes" in st.session_state:

    st.subheader("📦 Proposed Changes")

for c in st.session_state["changes"]:

    st.markdown(f"### 📄 {c['file']}")

    if c["diff_type"] == "text":
        st.code(c["diff"], language="diff")
    else:
        st.code(c["diff"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve PR"):
            requests.post("http://localhost:8000/approve")
            st.success("Merged!")

    with col2:
        if st.button("❌ Reject"):
            st.warning("Rejected")
