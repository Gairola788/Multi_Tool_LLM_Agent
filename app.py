import streamlit as st
import requests
import uuid

# ------------------ CONFIG ------------------

API_URL = "http://127.0.0.1:8000/chat"
RESET_URL = "http://127.0.0.1:8000/reset"

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Assistant with Tools")

# ------------------ SESSION ID ------------------

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# ------------------ CHAT HISTORY ------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ INPUT ------------------

user_input = st.chat_input("Ask something...")

# ------------------ HANDLE INPUT ------------------

if user_input:
    # Show user message
    st.session_state.chat_history.append(("user", user_input))

    # Send request to FastAPI
    with st.spinner("Thinking... 🤖"):
        try:
            response = requests.post(
                API_URL,
                json={
                    "question": user_input,
                    "session_id": st.session_state.session_id
                }
            )
            bot_reply = response.json().get("response", "Error in response")

        except Exception as e:
            bot_reply = f"Error: {str(e)}"

    st.session_state.chat_history.append(("bot", bot_reply))
# ------------------ DISPLAY CHAT ------------------

for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)

# ------------------ RESET BUTTON ------------------

if st.button("🔄 Reset Conversation"):
    # Clear backend memory
    requests.post(
        RESET_URL,
        params={"session_id": st.session_state.session_id}
    )

    # Clear frontend memory
    st.session_state.chat_history = []
    st.success("Conversation reset!")