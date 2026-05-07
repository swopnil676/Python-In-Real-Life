    # <-- midium version -->
# import PyPDF2
# import os

# merge = PyPDF2.PdfMerger()

# for file in os.listdir(os.getcwd()):
#     if file.endswith(".pdf"):
#         merge.append(file)

# merge.write("combinedPDF.pdf")



    # <-- optimized version -->
import PyPDF2
import os

merge = PyPDF2.PdfMerger()

pdf_files = sorted([f for f in os.listdir(os.getcwd()) if f.endswith(".pdf")])

if not pdf_files:
    print("No PDF files found!")
else:
    for file in pdf_files:
        merge.append(file)
        print(f"Added: {file}")

    output = "combinedPDF.pdf"
    merge.write(output)
    merge.close()
    print(f"\n✅ Done! Merged {len(pdf_files)} files into '{output}'")


    # ===== OUTPUT =====

# Added: Data Science & Analytics.pdf
# Added: Effective Leadership.pdf
# Added: c lab.pdf
# Added: machine learning.pdf
# Added: programming with python.pdf

# ✅ Done! Merged 5 files into 'combinedPDF.pdf'