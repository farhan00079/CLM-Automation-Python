import streamlit as st

st.set_page_config(page_title="Login | MyKart", page_icon="🛒")

EMAIL = "admin@gmail.com"
PASSWORD = "123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("<h2 style='text-align:center'>🛒 MyKart Login</h2>", unsafe_allow_html=True)
st.write("")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):
    if email == EMAIL and password == PASSWORD:
        st.session_state.logged_in = True
        st.switch_page("pages/1_Home.py")
    else:
        st.error("Invalid Email or Password ❌")
