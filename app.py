import streamlit as st
from backend.chatbot import get_response
from backend.pdf_reader import extract_text_from_pdf
from backend.text_splitter import split_text
from backend.embeddings import load_embedding_model
from backend.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
)
from backend.rag import generate_rag_prompt

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
if "vector_store" not in st.session_state:

    embedding_model = load_embedding_model()

    st.session_state.vector_store = load_vector_store(
        embedding_model
    )

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:

    st.title("📄 AI Document Assistant")

    uploaded_file = st.file_uploader(
        "📂 Upload Document",
        type=["pdf"]
    )

    process_button = st.button("🚀 Process Document")

    st.markdown("---")

    if st.session_state.vector_store is not None:
        st.success("🟢 Document Ready")
    else:
        st.warning("🟡 No document processed")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------
# Process Uploaded PDF
# ---------------------------

if process_button:

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    else:

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Step 1 - Read PDF
        with st.spinner("📄 Reading PDF..."):
            text = extract_text_from_pdf("temp.pdf")


        # Step 2 - Split Text
        with st.spinner("✂ Splitting document into chunks..."):
            chunks = split_text(text)


        # Step 3 - Load Embedding Model
        with st.spinner("🧠 Loading embedding model..."):
            embedding_model = load_embedding_model()


        # Step 4 - Create Vector Store
        with st.spinner("📚 Creating vector database..."):
            vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        # Save FAISS index to disk
        save_vector_store(vector_store)

        # Save in session
        st.session_state.vector_store = vector_store


        st.success("✅ Document processed successfully!")

        import os

        if os.path.exists("temp.pdf"):
            os.remove("temp.pdf")

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

        with st.spinner("🔍 Searching document..."):

            try:

                if st.session_state.vector_store is not None:

                    rag_prompt = generate_rag_prompt(
                        st.session_state.vector_store,
                        prompt
                    )

                    response = get_response(rag_prompt)

                else:

                    response = (
                        "⚠ Please upload and process a document first."
                    )

            except Exception as e:

                error_message = str(e)

                if "503" in error_message:
                    response = (
                        "⚠️ Gemini servers are currently busy.\n\n"
                        "Please wait a few seconds and try again."
                    )

                elif "400" in error_message:
                    response = (
                        "⚠️ Invalid request. Please try asking your question again."
                    )

                else:
                    response = (
                        "⚠️ Something went wrong.\n\n"
                        "Please try again."
                    )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )