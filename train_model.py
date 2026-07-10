import pandas as pd
import joblib

from nlp.preprocess import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Read dataset
df = pd.read_csv("data/Resume.csv")

print(df.head())
print(df.columns.tolist())

# Remove missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clean resume text
df["Resume_str"] = df["Resume_str"].apply(preprocess_text)

# Convert text into vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["Resume_str"])

# Encode labels
encoder = LabelEncoder()

y = encoder.fit_transform(df["Category"])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))


# Accuracy
accuracy = model.score(X_test, y_test)

print(f"Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(encoder, "models/encoder.pkl")

print("Model saved successfully!")