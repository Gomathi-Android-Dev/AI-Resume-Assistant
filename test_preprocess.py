from ocr.extract_text import extract_resume
from nlp.preprocess import preprocess_text
from nlp.ner import extract_entities

text = extract_resume("data/Gomathi.pdf")

print("Original Text")
print(text)

clean_text = preprocess_text(text)

print("\nClean Text")
print(clean_text)


entities = extract_entities(clean_text)

for entity in entities:
    print(entity)