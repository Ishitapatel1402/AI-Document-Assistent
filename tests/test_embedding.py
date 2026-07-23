from backend.embeddings import load_embedding_model

embedding_model = load_embedding_model()

vector = embedding_model.embed_query(
    "Artificial Intelligence"
)

print(f"Vector Length: {len(vector)}")

print(vector[:10])