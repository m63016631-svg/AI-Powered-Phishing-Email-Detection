import os
import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "data.csv"
)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print(f"Number of emails: {len(df)}")
print("\nFirst five records:")
print(df.head())


# --------------------------------------------------
# 2. Remove missing values
# --------------------------------------------------

df = df.dropna(subset=["text", "label"])

X = df["text"]
y = df["label"]


# --------------------------------------------------
# 3. Split dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------------------------
# 4. Create ML pipeline
# --------------------------------------------------

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            max_features=10000
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            random_state=42
        )
    )
])


# --------------------------------------------------
# 5. Train model
# --------------------------------------------------

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed.")


# --------------------------------------------------
# 6. Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 7. Evaluate model
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n========== MODEL RESULTS ==========")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# --------------------------------------------------
# 8. Save model
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "phishing_model.pkl"
)

joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")


# --------------------------------------------------
# 9. Save metrics
# --------------------------------------------------

metrics = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1
}

METRICS_PATH = os.path.join(
    os.path.dirname(__file__),
    "model_metrics.json"
)

with open(METRICS_PATH, "w") as file:
    json.dump(metrics, file, indent=4)

print(f"Metrics saved to: {METRICS_PATH}")