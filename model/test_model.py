import os
import joblib


MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "phishing_model.pkl"
)

model = joblib.load(MODEL_PATH)


emails = [
    "URGENT! Your account has been suspended. Click this link immediately to verify your password.",
    "Hi Sarah, just confirming that our meeting is tomorrow at 3 PM."
]


for email in emails:

    prediction = model.predict([email])[0]

    probability = model.predict_proba([email])[0][1]

    print("\nEmail:")
    print(email)

    if prediction == 1:
        print("Prediction: PHISHING")
    else:
        print("Prediction: LEGITIMATE")

    print(f"Phishing probability: {probability * 100:.2f}%")