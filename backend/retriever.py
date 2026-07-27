def retrieve_chunks(vector_store, query, k=3):
    """
    Retrieve the top-k relevant chunks and their page numbers.
    """

    docs = vector_store.similarity_search(
        query=query,
        k=k
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    pages = sorted(
        list(
            set(
                doc.metadata["page"]
                for doc in docs
            )
        )
    )

    return context, pages