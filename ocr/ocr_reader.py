import pytesseract

from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def scan_pdf(file_path):

    images = convert_from_path(file_path,
poppler_path=r"C:\poppler-26.02.0\Library\bin")

    text = ""

    for img in images:

        text += pytesseract.image_to_string(img)

    return text