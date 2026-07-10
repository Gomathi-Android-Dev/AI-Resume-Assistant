import joblib

from ocr.extract_text import extract_resume
from nlp.preprocess import preprocess_text

# Load saved model
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")
encoder = joblib.load("models/encoder.pkl")

# Resume path
resume_path = "data/resumes/07_HR_Manager.pdf"

# Extract text
text = extract_resume(resume_path)

# Clean text
clean_text = preprocess_text(text)

# Convert into TF-IDF
vector = vectorizer.transform([clean_text])

# Predict
prediction = model.predict(vector)

# Convert number back to category
category = encoder.inverse_transform(prediction)

print("=" * 40)
print("Predicted Category :", category[0])
print("=" * 40)