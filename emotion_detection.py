# emotion_detection.py
# Detects the user's emotion from input text using TextBlob sentiment analysis.

from textblob import TextBlob


def detect_emotion(text: str) -> str:
    """
    Analyze the sentiment of the input text and return an emotion label.

    Uses TextBlob's polarity score (-1.0 to 1.0) and subjectivity (0.0 to 1.0)
    to classify the user's emotional state into one of five categories:
        - Happy
        - Sad
        - Neutral
        - Stressed
        - Anxious

    Parameters:
        text (str): The user's typed message describing how they feel.

    Returns:
        str: One of 'Happy', 'Sad', 'Neutral', 'Stressed', or 'Anxious'
    """
    if not text or not text.strip():
        return "Neutral"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity          # Range: -1.0 (negative) to 1.0 (positive)
    subjectivity = blob.sentiment.subjectivity  # Range: 0.0 (objective) to 1.0 (subjective)

    # Keyword-based overrides for stress and anxiety detection
    stress_keywords = [
        "stressed", "stress", "overwhelmed", "burnout", "exhausted",
        "deadline", "pressure", "overloaded", "tired", "can't cope",
        "too much", "no time", "behind", "failing"
    ]
    anxiety_keywords = [
        "anxious", "anxiety", "nervous", "panic", "panicking", "scared",
        "fear", "fearful", "worried", "worry", "restless", "on edge",
        "heart racing", "can't breathe", "overthinking", "what if", "die",
        "suicide", "dying", "death"
    ]

    text_lower = text.lower()

    # Check for stress/anxiety keywords first (higher priority)
    if any(word in text_lower for word in stress_keywords):
        return "Stressed"
    if any(word in text_lower for word in anxiety_keywords):
        return "Anxious"

    # Polarity-based classification
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    elif -0.1 <= polarity <= 0.1 and subjectivity < 0.4:
        return "Neutral"
    elif polarity < -0.1 and subjectivity > 0.5:
        # Highly subjective and somewhat negative → likely stressed
        return "Stressed"
    else:
        return "Neutral"