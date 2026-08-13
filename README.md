## AI-Powered Phishing Email Detection System
✯ Project Overview ✯

The **AI-Powered Phishing Email Detection System** is a machine learning-based web application designed to identify potentially malicious phishing emails.
The system analyzes email content using a trained machine learning model and additional rule-based security checks. It provides a phishing probability, overall risk score, risk level, detected phishing indicators, URLs found in the email, and a security recommendation.
The system can analyze email text entered manually or email files uploaded by the user.

## Objectives

The main objectives of this project are:
- To develop a machine-learning-based phishing email detection system.
- To classify emails as Safe or Phishing.
- To use TF-IDF for converting email text into numerical features.
- To calculate the probability of an email being phishing-related.
- To identify suspicious patterns using rule-based security checks.
- To detect potentially suspicious URLs.
- To generate an understandable risk score and risk level.
- To provide security recommendations to users.
- To develop a simple web interface for practical email analysis.

## Main Features

- AI-based phishing email classification
- Manual email text analysis
- `.eml` file upload support
- `.txt` file upload support
- TF-IDF text feature extraction
- Phishing probability calculation
- Rule-based phishing indicator detection
- Suspicious URL analysis
- Combined risk score from 0 to 100
- Safe, Medium Risk, and High Risk classification
- Security recommendations
- Web-based analysis interface

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib

### Data Processing

- Pandas
- NumPy

### Development and Analysis

- Jupyter Notebook
- VS Code

## System Architecture

The system follows the following processing flow:

	User Email
	Email Text / File Upload
	Flask Backend
	TF-IDF Feature Extraction
	Machine Learning Classification
	Phishing Probability
	Rule-Based Security Analysis
	URL Analysis
	Combined Risk Score
	Risk Level
	Security Recommendation
	Results Displayed to User

## Machine Learning

The system uses a trained machine learning classification model to classify emails as:

- Safe Email
- Phishing Email

Email text is converted into numerical features using a TF-IDF vectorizer before being passed to the trained model.
The trained model and vectorizer are stored in the `model` directory.

## Rule-Based Security Analysis

In addition to machine learning, the system performs rule-based security checks.
It looks for:
- 	Urgent or threatening language
- 	Requests for passwords or login information
- 	Financial or payment-related language
- 	Prize and reward-related language
- 	Suspicious URLs
- 	IP addresses used instead of domain names
- 	URL shortening services
- 	Punycode domains
- 	Excessive subdomains
- 	Suspicious words in URLs

The rule-based analysis contributes up to 30 points to the overall risk score.

## Risk Score

The final risk score is calculated by combining the machine learning phishing probability with the rule-based security score.

### Risk Levels

| Risk Score | Risk Level  |

| 70–100     | High Risk   |

| 40–69      | Medium Risk |

| 0–39       | Safe        |
|------------|-------------|

The machine learning probability contributes up to 70 points, while rule-based security checks contribute up to 30 points.

## Email Input Methods

The system supports two methods of analysis:
 ✯ 1. Paste Email Text ✯ 
Users can paste the contents of an email directly into the text area and click:
 ✯ 2. Upload Email File ✯ 
Users can upload email files in the following formats:
- `.eml`
- `.txt`
The uploaded content is processed through the same detection pipeline.

## Model Performance

The trained model was evaluated using a separate test dataset.
The evaluation results were:
- Accuracy: 98.03%
- Precision: 97.55%
- Recall: 97.18%
- F1-Score: 97.37%
These results indicate that the trained model performs well on the evaluation dataset.

## Backend Implementation

The backend is implemented using **Python and Flask**.

The Flask backend:
1.	Receives email content from the web interface. 
2.	Processes the submitted email. 
3.	Loads the trained machine learning model. 
4.	Loads the TF-IDF vectorizer. 
5.	Converts the email into TF-IDF features. 
6.	Performs machine learning classification. 
7.	Calculates phishing probability. 
8.	Performs rule-based security analysis. 
9.	Extracts URLs from the email. 
10.	Calculates the combined risk score. 
11.	Determines the risk level. 
12.	Generates a security recommendation. 
13.	Returns the analysis results to the web interface. 
The rule-based analysis is implemented in:
security_checks.py

## Installation

Clone or download the repository and install the required Python packages:
 pip install -r requirements.txt
A virtual environment can be used to isolate the project dependencies.

## How to Run

1. Activate the virtual environment on Windows PowerShell:
venv\Scripts\Activate.ps1
2. Start the Flask application:
python app.py
3. Open a web browser and visit:
http://127.0.0.1:5000

## How to Use

1.	Open the web application. 
2.	Paste an email or upload a supported email file. 
3.	Select the analysis option. 
4.	The system processes the email. 
5.	The machine learning model generates a classification and phishing probability. 
6.	Rule-based checks identify suspicious indicators. 
7.	URLs are extracted and analyzed. 
8.	The system calculates the overall risk score. 
9.	The final risk level and security recommendation are displayed.

## Testing

The system was tested using different types of email input:

1. Safe email
2. Phishing email
3. EML file
4. TXT file

The tests were performed to verify the classification, risk assessment, file processing, indicator detection, and result display.

## Limitations

The system is designed as a phishing detection aid and should not be considered a complete enterprise security solution.
The rule-based URL analysis does not visit or execute URLs. It only examines URL structures for potentially suspicious characteristics.
The machine learning model's performance may vary when it encounters email types, topics, or writing styles that are not well represented in the training dataset.
The system does not guarantee that every phishing email will be detected.

## Future Improvements

Possible future improvements include:
- More advanced email header analysis
- Improved URL reputation checking
- Real-time threat intelligence integration
- Detection of malicious attachments
- Deep learning-based classification
- Improved handling of HTML email content
- Larger and more diverse training datasets 

## Deployment

The application is currently deployed locally using the Flask development server.
It can be started using:
python app.py
The application is then accessible through:
http://127.0.0.1:5000
The trained model and TF-IDF vectorizer are loaded from the project's model directory when the Flask application starts.

## Conclusion

The AI-Powered Phishing Email Detection System combines machine learning and rule-based security analysis to provide a practical approach to identifying potentially malicious emails.

Instead of providing only a Safe or Phishing classification, the system provides phishing probability, risk score, risk level, detected indicators, URL information, and security recommendations.

The project demonstrates how machine learning and security rules can be combined to create an understandable and practical phishing email analysis tool.

## Author

Maryam Mushtaq
Department of Information Technology
The University of Haripur
