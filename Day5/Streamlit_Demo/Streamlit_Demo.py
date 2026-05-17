import streamlit as st

st.title("Streamlit Demo : My first streamlit App")

name = st.text_input("Enter your name")

if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}! Welcome to my page.")
    else:
        st.warning("Please enter your name to get a greeting.")