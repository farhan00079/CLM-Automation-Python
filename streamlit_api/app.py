# import streamlit as st

# st.title("use my secret keyword with streamlit")
# st.text("example text")
# st.text(st.secrets["MY_API_KEY"])

import streamlit as st
import requests

# st.title("Easy API Integration – Streamlit")

# url = "https://api.agify.io?name=farhan"
# response = requests.get(url)
# data = response.json()

# st.json(data)
# st.write("Name:", data["name"])
# st.write("Predicted Age:", data["age"])

name = st.text_input("Enter your name")

if name:
    url = f"https://api.agify.io?name={name}"
    data = requests.get(url).json()
    st.success(f"Predicted Age: {data['age']}")
