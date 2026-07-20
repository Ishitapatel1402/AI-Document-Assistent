import streamlit as st
from backend.chatbot import get_response

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Document Intelligence Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Session State
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.title("📄 AI Document Assistant")

    st.success("✅ Gemini Connected")

    st.markdown("---")

    st.subheader("Upcoming Features")

    st.write("📄 PDF Upload")

    st.write("🧠 RAG Search")

    st.write("💾 Vector Database")

    st.write("🔍 Semantic Search")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------
# Main Title
# ---------------------------
st.title("🤖 AI Document Intelligence Assistant")

st.caption("Powered by Google Gemini")

# ---------------------------
# Display Previous Messages
# ---------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# User Input
# ---------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Get AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking... 🤔"):

            response = get_response(prompt)

            st.markdown(response)

            try:
                response = get_response(prompt)

            except Exception as e:
                response = f"❌ Error: {str(e)}"

                st.markdown(response)
        

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )