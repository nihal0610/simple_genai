import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Groq AI Chatbot")
st.write("Ask me anything!")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your question:", "")

if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"question": user_input})
            if response.status_code == 200:
                answer = response.json().get("answer", "No response")
                st.session_state.history.append(("You", user_input))
                st.session_state.history.append(("Groq", answer))
            else:
                st.error("Error: Could not reach backend")

# Display chat
for role, msg in st.session_state.history:
    st.markdown(f"**{role}:** {msg}")
