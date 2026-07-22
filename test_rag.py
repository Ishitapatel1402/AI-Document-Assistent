from backend.pdf_reader import extract_text_from_pdf
from backend.text_splitter import split_text
from backend.embeddings import load_embedding_model
from backend.vector_store import create_vector_store
from backend.rag import generate_rag_prompt

# Read PDF
text = extract_text_from_pdf(
    "D:\\AI-Document-Assistent\\AI Document Intelligence Assistant.pdf"
)

# Chunk
chunks = split_text(text)

# Embeddings
embedding_model = load_embedding_model()

# FAISS
vector_store = create_vector_store(
    chunks,
    embedding_model
)

query = input("Ask: ")

prompt = generate_rag_prompt(
    vector_store,
    query
)

print(prompt)