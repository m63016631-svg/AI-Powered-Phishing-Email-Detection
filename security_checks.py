import re
from urllib.parse import urlparse


# =========================================================
# Suspicious words/phrases commonly associated with phishing
# =========================================================

URGENT_KEYWORDS = [
    "urgent",
    "immediately",
    "act now",
    "action required",
    "account suspended",
    "account will be closed",
    "verify now",
    "verify immediately",
    "final warning",
    "limited time"
]


CREDENTIAL_KEYWORDS = [
    "password",
    "username",
    "login",
    "sign in",
    "verify your account",
    "confirm your identity",
    "security code",
    "verification code",
    "otp"
]


FINANCIAL_KEYWORDS = [
    "bank account",
    "credit card",
    "debit card",
    "banking details",
    "payment",
    "wire transfer",
    "refund",
    "invoice",
    "billing"
]


REWARD_KEYWORDS = [
    "you have won",
    "winner",
    "prize",
    "reward",
    "lottery",
    "claim your prize",
    "free gift"
]


# =========================================================
# URL Extraction
# =========================================================

def extract_urls(text):
    """
    Extract HTTP/HTTPS URLs from email text.
    """

    pattern = r"""https?://[^\s<>"']+"""

    return re.findall(pattern, text, re.IGNORECASE)


# =========================================================
# URL Security Analysis
# =========================================================

def check_url(url):
    """
    Check a URL for common suspicious characteristics.

    This function does NOT visit the URL.
    """

    indicators = []
    score = 0

    try:

        parsed = urlparse(url)

        hostname = parsed.hostname or ""

        # -------------------------------------------------
        # IP address instead of normal domain
        # -------------------------------------------------

        if re.match(
            r'^(?:\d{1,3}\.){3}\d{1,3}$',
            hostname
        ):

            indicators.append(
                "URL uses an IP address instead of a domain name"
            )

            score += 10


        # -------------------------------------------------
        # @ symbol in URL
        # -------------------------------------------------

        if "@" in url:

            indicators.append(
                "URL contains an @ symbol"
            )

            score += 10


        # -------------------------------------------------
        # Punycode domain
        # -------------------------------------------------

        if "xn--" in hostname.lower():

            indicators.append(
                "URL contains a potentially deceptive punycode domain"
            )

            score += 10


        # -------------------------------------------------
        # URL shorteners
        # -------------------------------------------------

        shorteners = [
            "bit.ly",
            "tinyurl.com",
            "t.co",
            "goo.gl",
            "is.gd",
            "ow.ly"
        ]

        if hostname.lower() in shorteners:

            indicators.append(
                "URL uses a URL shortening service"
            )

            score += 8


        # -------------------------------------------------
        # Excessive subdomains
        # -------------------------------------------------

        if hostname.count(".") >= 3:

            indicators.append(
                "URL contains an unusually large number of subdomains"
            )

            score += 5


        # -------------------------------------------------
        # Suspicious words in URL
        # -------------------------------------------------

        suspicious_url_words = [
            "login",
            "verify",
            "account",
            "secure",
            "update",
            "password",
            "confirm"
        ]

        url_lower = url.lower()

        if any(
            word in url_lower
            for word in suspicious_url_words
        ):

            indicators.append(
                "URL contains account or verification-related terms"
            )

            score += 5


    except Exception:

        indicators.append(
            "URL could not be safely analyzed"
        )

        score += 5


    return indicators, score


# =========================================================
# Complete Email Rule-Based Analysis
# =========================================================

def analyze_email_rules(email_text):
    """
    Perform rule-based security analysis of the email.
    """

    text = email_text.lower()

    indicators = []

    score = 0


    # -----------------------------------------------------
    # 1. Urgent language
    # -----------------------------------------------------

    found_urgent = []

    for keyword in URGENT_KEYWORDS:

        if keyword in text:

            found_urgent.append(keyword)


    if found_urgent:

        indicators.append(
            "Urgent or threatening language detected"
        )

        score += 8


    # -----------------------------------------------------
    # 2. Credential requests
    # -----------------------------------------------------

    found_credentials = []

    for keyword in CREDENTIAL_KEYWORDS:

        if keyword in text:

            found_credentials.append(keyword)


    if found_credentials:

        indicators.append(
            "Possible request for login or authentication information"
        )

        score += 10


    # -----------------------------------------------------
    # 3. Financial requests
    # -----------------------------------------------------

    found_financial = []

    for keyword in FINANCIAL_KEYWORDS:

        if keyword in text:

            found_financial.append(keyword)


    if found_financial:

        indicators.append(
            "Financial or payment-related language detected"
        )

        score += 8


    # -----------------------------------------------------
    # 4. Rewards/scams
    # -----------------------------------------------------

    found_rewards = []

    for keyword in REWARD_KEYWORDS:

        if keyword in text:

            found_rewards.append(keyword)


    if found_rewards:

        indicators.append(
            "Prize, reward, or unexpected-benefit language detected"
        )

        score += 8


    # -----------------------------------------------------
    # 5. URL analysis
    # -----------------------------------------------------

    urls = extract_urls(email_text)

    suspicious_urls = []


    for url in urls:

        url_indicators, url_score = check_url(url)

        if url_indicators:

            suspicious_urls.extend(
                url_indicators
            )

        score += url_score


    if suspicious_urls:

        indicators.extend(
            suspicious_urls
        )


    # -----------------------------------------------------
    # Remove duplicate indicators
    # -----------------------------------------------------

    indicators = list(
        dict.fromkeys(indicators)
    )


    # -----------------------------------------------------
    # Maximum rule-based contribution = 30
    # -----------------------------------------------------

    score = min(score, 30)


    return {
        "indicators": indicators,
        "rule_score": score,
        "urls_found": urls
    }