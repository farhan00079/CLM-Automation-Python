import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="Shopping | MyKart", layout="wide")

st.title("🛍️ Shopping")
st.write("Browse all categories and products here.")

st.button("📱 Mobiles")
st.button("💻 Laptops")
st.button("👕 Fashion")
st.button("🎧 Electronics")

if st.button("⬅ Back to Home"):
    st.switch_page("pages/1_Home.py")
