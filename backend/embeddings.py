from sentence_transformers import SentenceTransformer


class SentenceTransformerEmbeddings:

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False,
        ).tolist()

    def embed_query(self, text):
        return self.model.encode(
            text,
            convert_to_numpy=True,
            show_progress_bar=False,
        ).tolist()


def load_embedding_model():

    embedding_model = SentenceTransformerEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model