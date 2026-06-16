import streamlit as st

st.title("Claude Nonprofit Assistant")

question = st.text_input("Ask a question about the nonprofit:")

if question:
    st.write("This is where Claude's response will appear.")
