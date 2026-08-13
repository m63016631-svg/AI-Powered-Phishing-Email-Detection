## AI-Powered Phishing Email Detection System
✯ Project Overview ✯

The AI-Powered Phishing Email Detection System is a machine learning-based web application designed to identify potentially malicious phishing emails.
The system analyzes email content using a trained machine learning model and additional rule-based security checks. It provides a phishing probability, overall risk score, risk level, detected phishing indicators, URLs found in the email, and a security recommendation.
The system can analyze email text entered manually or email files uploaded by the user.

## Main Features

•	AI-based phishing email classification
•	Manual email text analysis
•	Email file upload support
•	Supports `.eml` and `.txt` files
•	TF-IDF text feature extraction
•	Phishing probability calculation
•	Rule-based phishing indicator detection
•	Suspicious URL analysis
•	Combined risk score from 0 to 100
•	High, Medium, and Safe risk levels
•	Security recommendations
•	Simple web-based interface

## Technologies Used

•	Python
•	Flask
•	Scikit-learn
•	Pandas
•	Joblib
•	HTML
•	CSS
•	Jupyter Notebook
•	TF-IDF Vectorization
•	Machine Learning

## Machine Learning

The system uses a trained machine learning classification model to classify emails as:
•	Safe Email
•	Phishing Email
Email text is converted into numerical features using a TF-IDF vectorizer before being passed to the trained model.
The trained model and vectorizer are stored in the `model` directory.

## Rule-Based Security Analysis

In addition to machine learning, the system performs rule-based security checks.
It looks for:
•	Urgent or threatening language
•	Requests for passwords or login information
•	Financial or payment-related language
•	Prize and reward-related language
•	Suspicious URLs
•	IP addresses used instead of domain names
•	URL shortening services
•	Punycode domains
•	Excessive subdomains
•	Suspicious words in URLs
The rule-based analysis contributes up to 30 points to the overall risk score.

## Risk Score

The final risk score is calculated by combining the machine learning phishing probability with the rule-based security score.

### Risk Levels

|------------|-------------|
| Risk Score | Risk Level  |
|------------|-------------|
| 70–100     | High Risk   |
|------------|-------------|
| 40–69      | Medium Risk |
|------------|-------------|
| 0–39       | Safe        |
|------------|-------------|

The machine learning probability contributes up to 70 points, while rule-based security checks contribute up to 30 points.

## Email Input Methods

The system supports two methods of analysis:
✯ 1. Paste Email Text ✯
Users can paste the contents of an email directly into the text area and click:
✯ 2. Upload Email File ✯
Users can upload email files in the following formats:
•	`.eml`
•	`.txt`
The uploaded email content is then analyzed by the same machine learning and rule-based detection system.

## Model Performance

The trained model was evaluated using a separate test dataset.
The evaluation results were:
•	Accuracy: 98.03%
•	Precision: 97.55%
•	Recall: 97.18%
•	F1-Score: 97.37%
These results indicate that the trained model performs well on the evaluation dataset.

## How to Run

1. Activate the virtual environment
   On Windows PowerShell:
   venv\Scripts\Activate.ps1
2. Start the Flask application
   python app.py
3. Open the application
   Open a web browser and visit:
   http://127.0.0.1:5000

## How to Use

The user can either:
•	Paste an email message into the text area and click Analyze Email, or 
•	Upload an .eml or .txt email file. 
The system then analyzes the email and displays:
•	Machine learning classification 
•	Phishing probability 
•	Overall risk score 
•	Risk level 
•	Detected phishing indicators 
•	URLs found 
•	Security recommendation 

## Limitations

The system is designed as a phishing detection aid and should not be considered a complete security solution.
The rule-based URL analysis does not visit or execute URLs. It only examines their structure for suspicious characteristics.
The machine learning model's performance may vary when it encounters email types or writing styles that were not well represented in the training dataset.

## Future Improvements

Possible future improvements include:
•	More advanced email header analysis 
•	Improved URL reputation checking 
•	Real-time threat intelligence integration 
•	Detection of malicious attachments 
•	Deep learning-based classification 
•	Improved handling of HTML email content 
•	Larger and more diverse training datasets 

## Conclusion

The AI-Powered Phishing Email Detection System combines machine learning and rule-based security analysis to provide a practical approach to identifying potentially malicious emails.
The system provides users with an understandable risk assessment instead of only returning a simple phishing or safe classification.