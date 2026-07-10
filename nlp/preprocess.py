import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    doc = nlp(text)

    clean_words = []

    for token in doc:

        # Remove stopwords and punctuation
        if not token.is_stop and not token.is_punct:

            clean_words.append(token.lemma_)

    return " ".join(clean_words)