from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extracts text page by page from a PDF.

    Returns:
        List of dictionaries:
        [
            {
                "page": 1,
                "text": "..."
            },
            ...
        ]
    """

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text:

            pages.append(
                {
                    "page": page_number,
                    "text": page_text
                }
            )

    return pages