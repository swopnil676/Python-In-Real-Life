from pypdf import PdfReader

file_path = r"C:\Users\swopn\Documents\machine learning.pdf"

print("__EXTRACTING DATA__\n")

with open(file_path, "rb") as pdf_file:
    reader = PdfReader(pdf_file)
    print(reader.pages[0].extract_text())

print("\nPDF File Decorded")