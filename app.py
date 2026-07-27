import os

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
from backend.metadata import save_metadata, load_metadata
from backend.hash_utils import generate_file_hash

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

if "metadata" not in st.session_state:
    st.session_state.metadata = load_metadata()

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

    st.markdown("---")

    if (
        st.session_state.vector_store is not None
        and st.session_state.metadata is not None
    ):

        metadata = st.session_state.metadata

        st.success("🟢 Document Ready")

        st.info(
            f"""
    📄 **Document:** {metadata['document_name']}

    📑 **Chunks:** {metadata['chunk_count']}
    """
        )

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

        # Save uploaded PDF temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Generate hash of uploaded file
        current_hash = generate_file_hash("temp.pdf")

        # Load previous metadata
        metadata = load_metadata()

        # -----------------------------
        # Same document? Load FAISS
        # -----------------------------
        if (
            metadata is not None
            and metadata["file_hash"] == current_hash
        ):

            embedding_model = load_embedding_model()

            st.session_state.vector_store = load_vector_store(
                embedding_model
            )

            st.session_state.metadata = metadata

            st.success("✅ Existing document detected. Loaded saved vector database.")

        # -----------------------------
        # New document? Process it
        # -----------------------------
        else:

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

            # Save FAISS
            save_vector_store(vector_store)

            # Save Metadata
            save_metadata(
                uploaded_file.name,
                len(chunks),
                current_hash
            )

            # Update Session
            st.session_state.vector_store = vector_store
            st.session_state.metadata = load_metadata()

            st.success("✅ Document processed successfully!")

        # Delete temporary file
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
if st.session_state.vector_store is None:
    prompt = st.chat_input(
        "Upload and process a PDF first...",
        disabled=True
    )
else:
    prompt = st.chat_input(
        "Ask a question about your document..."
    )

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

                    rag_prompt, pages = generate_rag_prompt(
                        st.session_state.vector_store,
                        prompt
                    )

                    response = get_response(rag_prompt)

                    if pages:

                        if len(pages) == 1:

                            response += f"\n\n📄 Source: Page {pages[0]}"

                        else:

                            page_list = ", ".join(str(page) for page in pages)

                            response += f"\n\n📄 Sources: Pages {page_list}"

            except Exception as e:

                import traceback

                st.error(traceback.format_exc())

                response = f"⚠ {type(e).__name__}: {e}"

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )