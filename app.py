
import os
import streamlit as st

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

st.set_page_config(
    page_title="Chat with Gemini-Pro!!",
    page_icon=":brain:",
    layout="centered",
)

def translate(user_role):
    if user_role=="model":
        return "assistant"
    return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 Gemini Pro - ChatBot")

for messages in st.session_state.chat_session.history:
    with st.chat_message(translate(messages.role)):
        st.markdown(messages.parts[0].text)

user_prompt = st.chat_input("Chat with Gemini-Pro...")

if user_prompt:
    st.chat_message('user').markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message('assistant'):
        st.markdown(gemini_response.text)

