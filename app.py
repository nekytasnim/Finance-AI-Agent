import streamlit as st
from main import ask_agent  

st.set_page_config(page_title="Finance AI Agent 💼", layout="wide")
st.title("📊 Finance AI Agent")

user_query = st.text_input("Ask your question:")

if user_query:
    with st.spinner("Processing..."):
        answer = ask_agent(user_query)
else:
    answer = "Please enter a question to get started."

st.subheader("💡 Agent's Answer")
st.write(answer)



