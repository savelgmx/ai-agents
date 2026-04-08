import streamlit as st
import requests

st.title("🚀 AI Dev PR System")

feature = st.text_input("Feature")

if st.button("Create PR"):

    res = requests.post(
        "http://localhost:8000/run",
        json={"feature": feature}
    )

    data = res.json()

    st.session_state["changes"] = data["changes"]
    st.session_state["logs"] = data.get("logs", [])


# --- DIFF VIEW ---
if "changes" in st.session_state:

    st.subheader("📦 Proposed Changes")

    for idx, c in enumerate(st.session_state["changes"]):

        st.markdown(f"### 📄 {c['file']}")

        tabs = st.tabs(["📊 Diff", "🆚 Side-by-side"])

        # ---------- TAB 1: NORMAL DIFF ----------
        with tabs[0]:
            if c["diff_type"] == "text":
                st.code(c["diff"], language="diff")
            else:
                st.code(c["diff"])

        # ---------- TAB 2: SIDE BY SIDE ----------
        with tabs[1]:

            try:
                with open(c["file"], "r", encoding="utf-8") as f:
                    old_code = f.read()
            except:
                old_code = ""

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🟥 OLD")
                st.code(old_code, language="kotlin")

            with col2:
                st.markdown("#### 🟩 NEW")
                st.code(c["code"], language="kotlin")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve PR"):
            requests.post("http://localhost:8000/approve")
            st.success("Merged!")

    with col2:
        if st.button("❌ Reject"):
            st.warning("Rejected")

# --- LOGS ---
if "logs" in st.session_state:

    st.subheader("📜 Logs")

    for l in st.session_state["logs"]:
        st.text(l)
