from ocr.pdf_reader import load_pdf
from ocr.ocr_reader import scan_pdf

def extract_resume(file_path):

    text = load_pdf(file_path)

    if len(text.strip()) < 50:
        text = scan_pdf(file_path)

    return text