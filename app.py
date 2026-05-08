import streamlit as st
import uuid

from agent.agent import (
    run_agent,
    create_memory,
    trim_memory
)

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Multi Tool AI Assistant")

# ------------------ SESSION ID ------------------

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# ------------------ MEMORY ------------------

if "messages" not in st.session_state:
    st.session_state.messages = create_memory()

# ------------------ CHAT HISTORY ------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ USER INPUT ------------------

user_input = st.chat_input("Ask something...")

# ------------------ HANDLE INPUT ------------------

if user_input:

    # Save user message
    st.session_state.chat_history.append(
        ("user", user_input)
    )

    with st.spinner("Thinking... 🤖"):

        try:

            # Run AI agent directly
            response, updated_messages = run_agent(
                user_input,
                st.session_state.messages
            )

            # Trim memory
            updated_messages = trim_memory(updated_messages)

            # Save updated memory
            st.session_state.messages = updated_messages

            bot_reply = response

        except Exception as e:

            bot_reply = f"⚠️ Error: {str(e)}"

    # Save assistant response
    st.session_state.chat_history.append(
        ("assistant", bot_reply)
    )

# ------------------ DISPLAY CHAT ------------------

for role, message in st.session_state.chat_history:

    with st.chat_message(role):
        st.write(message)

# ------------------ RESET BUTTON ------------------

if st.button("🔄 Reset Conversation"):

    st.session_state.messages = create_memory()

    st.session_state.chat_history = []

    st.success("Conversation reset!")