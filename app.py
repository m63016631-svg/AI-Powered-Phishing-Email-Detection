from flask import Flask, render_template, request
import joblib
import os

from security_checks import analyze_email_rules


app = Flask(__name__)


# ---------------------------------------------------------
# Upload configuration
# ---------------------------------------------------------

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "eml"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check whether the uploaded file has an allowed extension."""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ---------------------------------------------------------
# Load trained ML model and TF-IDF vectorizer
# ---------------------------------------------------------

model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")


# ---------------------------------------------------------
# Home page
# ---------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    email_text = ""

    phishing_probability = None
    risk_score = None
    risk_level = None

    indicators = []
    recommendation = None
    urls_found = []

    upload_error = None

    if request.method == "POST":

        # -------------------------------------------------
        # 1. Check for uploaded email file
        # -------------------------------------------------

        uploaded_file = request.files.get("email_file")

        if uploaded_file and uploaded_file.filename:

            if allowed_file(uploaded_file.filename):

                email_text = uploaded_file.read().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

            else:

                upload_error = (
                    "Invalid file type. Please upload a .txt or .eml file."
                )

        # -------------------------------------------------
        # 2. If no file was uploaded, use pasted email text
        # -------------------------------------------------

        if not email_text:

            email_text = request.form.get(
                "email_text",
                ""
            ).strip()

        # -------------------------------------------------
        # 3. Analyze email
        # -------------------------------------------------

        if email_text:

            # -------------------------------------------------
            # Convert email into TF-IDF features
            # -------------------------------------------------

            email_features = vectorizer.transform(
                [email_text]
            )

            # -------------------------------------------------
            # ML prediction
            # -------------------------------------------------

            result = model.predict(
                email_features
            )[0]

            # -------------------------------------------------
            # Get phishing probability
            # -------------------------------------------------

            probabilities = model.predict_proba(
                email_features
            )[0]

            # Find probability corresponding to class 1
            class_index = list(model.classes_).index(1)

            phishing_probability = (
                probabilities[class_index] * 100
            )

            # -------------------------------------------------
            # Basic prediction
            # -------------------------------------------------

            if result == 1:
                prediction = "Phishing Email"
            else:
                prediction = "Safe Email"

            # -------------------------------------------------
            # Rule-based security analysis
            # -------------------------------------------------

            security_analysis = analyze_email_rules(
                email_text
            )

            indicators = security_analysis["indicators"]

            rule_score = security_analysis["rule_score"]

            urls_found = security_analysis["urls_found"]

            # -------------------------------------------------
            # Calculate combined risk score
            # -------------------------------------------------

            # ML probability contributes up to 70 points.
            # Rule-based checks contribute up to 30 points.

            risk_score = (
                phishing_probability * 0.70
            ) + rule_score

            risk_score = min(
                round(risk_score),
                100
            )

            # -------------------------------------------------
            # Determine risk level
            # -------------------------------------------------

            if risk_score >= 70:

                risk_level = "High Risk"

                recommendation = (
                    "Do not click links or provide sensitive "
                    "information. Verify the sender using an "
                    "independent trusted source."
                )

            elif risk_score >= 40:

                risk_level = "Medium Risk"

                recommendation = (
                    "Exercise caution. Avoid clicking links "
                    "or sharing sensitive information until "
                    "the sender and message are verified."
                )

            else:

                risk_level = "Safe"

                recommendation = (
                    "No major phishing indicators were detected. "
                    "Continue to verify unexpected requests before "
                    "taking action."
                )

    # ---------------------------------------------------------
    # Send results to HTML page
    # ---------------------------------------------------------

    return render_template(
        "index.html",
        prediction=prediction,
        email_text=email_text,
        phishing_probability=phishing_probability,
        risk_score=risk_score,
        risk_level=risk_level,
        indicators=indicators,
        recommendation=recommendation,
        urls_found=urls_found,
        upload_error=upload_error
    )


# ---------------------------------------------------------
# Run application
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)