import streamlit as st

# Login guard
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="About | MyKart", layout="wide")

st.title("ℹ️ About MyKart")
st.write("""
MyKart is an ecommerce platform inspired by Flipkart.
We provide best deals on electronics, fashion and more.
""")

if st.button("⬅ Back to Home"):
    st.switch_page("pages/1_Home.py")
