from backend.pdf_reader import extract_text_from_pdf
from backend.text_splitter import split_text
from backend.embeddings import load_embedding_model
from backend.vector_store import create_vector_store
from backend.retriever import retrieve_chunks

# Read PDF
text = extract_text_from_pdf(
    "D:\\AI-Document-Assistent\\AI Document Intelligence Assistant.pdf"
)

# Split
chunks = split_text(text)

# Embeddings
embedding_model = load_embedding_model()

# FAISS
vector_store = create_vector_store(
    chunks,
    embedding_model
)

# User Query
query = input("Ask a question: ")

# Retrieve
results = retrieve_chunks(
    vector_store,
    query
)

print("\nTop Matching Chunks:\n")

for i, doc in enumerate(results, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print("=" * 50)
    print(doc.page_content)