from backend.pdf_reader import extract_text_from_pdf

pdf_path = "D:\\AI-Document-Assistent\\AI Document Intelligence Assistant.pdf"

text = extract_text_from_pdf(pdf_path)

print("=" * 50)
print("Extracted Text")
print("=" * 50)

print(text[:3000])