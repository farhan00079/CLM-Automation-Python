import streamlit as st

st.set_page_config(
    page_title="Login | MyKart",
    page_icon="🛒",
    layout="centered"
)

# ------------------ DUMMY LOGIN DATA ------------------
EMAIL = "admin@gmail.com"
PASSWORD = "1234"

# ------------------ SESSION INIT ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------ IF ALREADY LOGGED IN ------------------
if st.session_state.logged_in:
    st.switch_page("pages/1_Home.py")

# ------------------ LOGIN UI ------------------
st.markdown("## 🛒 MyKart Login")
st.write("Please login to continue")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):
    if email == EMAIL and password == PASSWORD:
        st.session_state.logged_in = True
        st.success("Login Successful ✅")
        st.switch_page("pages/1_Home.py")
    else:
        st.error("Invalid Email or Password ❌")
