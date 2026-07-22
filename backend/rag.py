from backend.retriever import retrieve_chunks


def generate_rag_prompt(vector_store, query):
    """
    Creates a RAG prompt using retrieved document context.
    """

    context = retrieve_chunks(
        vector_store,
        query
    )

    prompt = f"""
You are an AI Document Intelligence Assistant.

Answer ONLY using the document context below.

If the answer is not present,
reply:

"I could not find this information in the uploaded document."

-------------------------
DOCUMENT
-------------------------

{context}

-------------------------
QUESTION
-------------------------

{query}

-------------------------
ANSWER
-------------------------
"""

    return prompt