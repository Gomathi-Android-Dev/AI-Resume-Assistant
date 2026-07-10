import os
import joblib
import streamlit as st

from ocr.extract_text import extract_resume
from nlp.preprocess import preprocess_text
from llm.gemini import analyze_resume


# Load ML models
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")
encoder = joblib.load("models/encoder.pkl")

# Create temp folder
os.makedirs("temp", exist_ok=True)

st.set_page_config(
    page_title="AI Resume Classifier",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Classifier")

st.write("Upload a resume (PDF) and predict its category.")

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    temp_path = os.path.join("temp", uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    if st.button("Predict Category"):

        with st.spinner("Analyzing Resume..."):

            # Extract text
            text = extract_resume(temp_path)

            # NLP preprocessing
            clean_text = preprocess_text(text)

            # Convert to TF-IDF
            vector = vectorizer.transform([clean_text])

            # Predict
            prediction = model.predict(vector)

            # Decode label
            category = encoder.inverse_transform(prediction)[0]
            analysis = analyze_resume(text, category)

        st.success(f"🎯 Predicted Category: {category}")

        st.markdown("---")

        st.subheader("🤖 AI Resume Analysis")

        st.write(analysis)