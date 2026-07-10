import re

def extract_phone(text):

    pattern = r'\b\d{10}\b'

    phones = re.findall(pattern, text)

    return phones