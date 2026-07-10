from ocr.pdf_reader import load_pdf
from ocr.ocr_reader import scan_pdf

#text = load_pdf("data/resumes/Gomathi.pdf")
text = scan_pdf("data/resumes/Gomathi.pdf")

print(text)