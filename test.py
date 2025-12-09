import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, Streamlit users!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}!")

number = st.slider("Select a number", 0, 100)
st.write(f"You selected: {number}")
