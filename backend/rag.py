from backend.retriever import retrieve_chunks


def generate_rag_prompt(vector_store, query):
    """
    Builds the prompt using retrieved document context.
    """

    context = retrieve_chunks(
        vector_store,
        query
    )

    prompt = f"""
You are an AI Document Intelligence Assistant.

Answer ONLY using the provided document context.

If the answer cannot be found in the document,
reply exactly:

"I could not find this information in the uploaded document."

======================
DOCUMENT
======================

{context}

======================
QUESTION
======================

{query}

======================
ANSWER
======================
"""

    return prompt