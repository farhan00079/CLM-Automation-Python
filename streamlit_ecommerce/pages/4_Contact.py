import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="Contact | MyKart", layout="wide")

st.title("📞 Contact Us")

st.text_input("Your Name")
st.text_input("Email")
st.text_area("Message")

st.text_input("Your age")

if st.button("Send Message"):
    st.success("Message sent successfully ✅")
    # st.error("Message not sent")

if st.button("⬅ Back to Home"):
    st.switch_page("pages/1_Home.py")