def retrieve_chunks(vector_store, query, k=1):
    """
    Retrieve top-k relevant chunks.
    """

    docs = vector_store.similarity_search(
        query=query,
        k=k
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context