import streamlit as st

st.title("My Forge 26 AI Project")

st.write("Welcome! My first GenAI project starts here.")

question = st.text_input("Ask a question")

if question:
    st.write("Your question:", question)
