import streamlit as st

st.title("use my secret keyword with streamlit")
st.text("example text")
st.text(st.secrets["MY_API_KEY"])