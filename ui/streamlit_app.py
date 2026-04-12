import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🚀 AI Dev PR System")

feature = st.text_input("Feature")

# -----------------------------
# RUN PIPELINE
# -----------------------------
if st.button("Create PR"):

    try:
        res = requests.post(
            "http://localhost:8000/run",
            json={"feature": feature}
        )

        if res.status_code != 200:
            st.error(f"Backend error:\n{res.text}")
            st.stop()

        data = res.json()

        st.session_state["changes"] = data.get("changes", [])
        st.session_state["logs"] = data.get("logs", [])

    except Exception as e:
        st.error(f"Request failed: {str(e)}")
        st.stop()


# -----------------------------
# DIFF VIEW
# -----------------------------
if "changes" in st.session_state:

    st.subheader("📦 Proposed Changes")

    for idx, c in enumerate(st.session_state["changes"]):

        st.markdown(f"### 📄 {c['file']}")

        tabs = st.tabs(["📊 Diff", "🆚 Side-by-side"])

        # ---------- TAB 1: NORMAL DIFF ----------
        with tabs[0]:
            if c.get("diff_type") == "text":
                st.code(c.get("diff", ""), language="diff")
            else:
                st.code(c.get("diff", ""))

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
                st.code(c.get("code", ""), language="kotlin")

    # -----------------------------
    # ACTION BUTTONS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve PR"):
            try:
                res = requests.post("http://localhost:8000/approve")

                if res.status_code != 200:
                    st.error(res.text)
                else:
                    st.success("Merged!")

            except Exception as e:
                st.error(str(e))

    with col2:
        if st.button("❌ Reject"):
            st.warning("Rejected")


# -----------------------------
# LOGS
# -----------------------------
if "logs" in st.session_state:

    st.subheader("📜 Logs")

    for l in st.session_state["logs"]:
        st.text(l)
