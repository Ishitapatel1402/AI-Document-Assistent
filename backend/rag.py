from backend.retriever import retrieve_chunks


def generate_rag_prompt(vector_store, query):
    """
    Creates a RAG prompt and returns the source pages.
    """

    context, pages = retrieve_chunks(
        vector_store,
        query
    )

    prompt = f"""
You are an AI Document Intelligence Assistant.

Answer ONLY using the provided document context.

If the answer is not present in the document,
reply exactly:

"I could not find this information in the uploaded document."

=========================
DOCUMENT
=========================

{context}

=========================
QUESTION
=========================

{query}

=========================
ANSWER
=========================
"""

    return prompt, pages