from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(pages):
    """
    Splits each page into chunks while preserving page numbers.

    Input:
    [
        {
            "page": 1,
            "text": "..."
        }
    ]

    Output:
    [
        {
            "page": 1,
            "text": "Chunk 1..."
        },
        {
            "page": 1,
            "text": "Chunk 2..."
        },
        {
            "page": 2,
            "text": "Chunk 3..."
        }
    ]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    all_chunks = []

    for page in pages:

        chunks = splitter.split_text(page["text"])

        for chunk in chunks:

            all_chunks.append(
                {
                    "page": page["page"],
                    "text": chunk
                }
            )

    return all_chunks