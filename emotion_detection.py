# emotion_detection.py
# Detects the user's emotion from input text using TextBlob + keyword matching.

from textblob import TextBlob


def detect_emotion(text: str) -> str:
    """
    Analyze the sentiment of the input text and return an emotion label.

    Priority order (highest to lowest):
        1. Crisis keywords  → "Crisis"   (self-harm, suicide, death wishes)
        2. Stress keywords  → "Stressed"
        3. Anxiety keywords → "Anxious"
        4. TextBlob polarity:
             > 0.3  → "Happy"
             < -0.3 → "Sad"
             else   → "Neutral"

    Parameters:
        text (str): The user's typed message.

    Returns:
        str: One of 'Happy', 'Sad', 'Neutral', 'Stressed', 'Anxious', 'Crisis'
    """
    if not text or not text.strip():
        return "Neutral"

    text_lower = text.lower()
    blob = TextBlob(text)
    polarity    = blob.sentiment.polarity      # -1.0 (negative) → 1.0 (positive)
    subjectivity = blob.sentiment.subjectivity # 0.0 (objective) → 1.0 (subjective)

    # ── 1. CRISIS DETECTION (checked first — highest priority) ──────────────
    # Words that suggest thoughts of self-harm, suicide, or not wanting to live.
    crisis_keywords = [
        # Death / dying
        "die", "dying", "dead", "death", "i want to die", "i wanna die",
        "wish i was dead", "better off dead", "want to be dead",
        # Suicide
        "suicide", "suicidal", "kill myself", "end my life", "end it all",
        "take my life", "take my own life", "no reason to live",
        "don't want to live", "dont want to live", "not want to live",
        "can't go on", "cant go on", "can't do this anymore", "cant do this anymore",
        # Self-harm
        "self harm", "self-harm", "hurt myself", "cutting myself", "cut myself",
        # Hopelessness tied to crisis
        "no point", "no purpose", "life is pointless", "nothing to live for",
        "disappear forever", "everyone would be better without me",
    ]
    if any(phrase in text_lower for phrase in crisis_keywords):
        return "Crisis"

    # ── 2. STRESS KEYWORDS ───────────────────────────────────────────────────
    stress_keywords = [
        "stressed", "stress", "overwhelmed", "burnout", "exhausted",
        "deadline", "pressure", "overloaded", "tired", "can't cope",
        "cant cope", "too much", "no time", "behind", "failing",
        "drowning in work", "breaking down", "tensed",
    ]
    if any(word in text_lower for word in stress_keywords):
        return "Stressed"

    # ── 3. ANXIETY KEYWORDS ──────────────────────────────────────────────────
    anxiety_keywords = [
        "anxious", "anxiety", "nervous", "panic", "panicking", "scared",
        "fear", "fearful", "worried", "worry", "restless", "on edge",
        "heart racing", "can't breathe", "cant breathe",
        "overthinking", "what if", "dread", "uneasy",
    ]
    if any(word in text_lower for word in anxiety_keywords):
        return "Anxious"

    # ── 4. POLARITY-BASED CLASSIFICATION ─────────────────────────────────────
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    elif -0.1 <= polarity <= 0.1 and subjectivity < 0.4:
        return "Neutral"
    elif polarity < -0.1 and subjectivity > 0.5:
        return "Stressed"
    else:
        return "Neutral"