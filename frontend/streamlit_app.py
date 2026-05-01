import streamlit as st
import requests

st.title("🤖 AI Customer Support Bot")

user_input = st.text_input("Enter your query")

if st.button("Send"):
    res = requests.post(
        "http://localhost:8000/chat",
        json={"message": user_input}
    )

    data = res.json()

    st.write("### Intent:", data["intent"])
    st.write("### Response:")
    st.success(data["response"])