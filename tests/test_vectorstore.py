from backend.pdf_reader import extract_text_from_pdf
from backend.text_splitter import split_text
from backend.embeddings import load_embedding_model
from backend.vector_store import create_vector_store

# Read PDF
text = extract_text_from_pdf(
    "D:\\AI-Document-Assistent\\AI Document Intelligence Assistant.pdf"
)

# Split into chunks
chunks = split_text(text)

# Load embedding model
embedding_model = load_embedding_model()

# Create vector database
vector_store = create_vector_store(
    chunks,
    embedding_model
)

print("✅ FAISS Vector Store Created Successfully!")

print(f"Total Chunks Stored: {len(chunks)}")