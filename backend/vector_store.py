from langchain_community.vectorstores import FAISS
import os


def create_vector_store(chunks, embedding_model):
    """
    Creates a FAISS vector database while storing page numbers
    as metadata.
    """

    texts = []
    metadatas = []

    for chunk in chunks:

        texts.append(chunk["text"])

        metadatas.append(
            {
                "page": chunk["page"]
            }
        )

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    return vector_store


def save_vector_store(vector_store):

    os.makedirs("vectorstore", exist_ok=True)

    vector_store.save_local("vectorstore")


def load_vector_store(embedding_model):

    if os.path.exists("vectorstore"):

        return FAISS.load_local(
            "vectorstore",
            embedding_model,
            allow_dangerous_deserialization=True
        )

    return None