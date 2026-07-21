from backend.pdf_reader import extract_text_from_pdf
from backend.text_splitter import split_text

pdf_path = "D:\\AI-Document-Assistent\\AI Document Intelligence Assistant.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")

print(chunks[0])