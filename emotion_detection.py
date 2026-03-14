# emotion_detection.py
# Detects the user's emotion from input text using keyword matching + TextBlob.

from textblob import TextBlob


def detect_emotion(text: str) -> str:
    """
    Priority order:
        1. Crisis    — self-harm / suicide / genuine death wishes
        2. Stressed  — workload, tension, overwhelm
        3. Anxious   — fear, worry, nervousness
        4. TextBlob polarity fallback → Happy / Sad / Neutral
    """
    if not text or not text.strip():
        return "Neutral"

    tl = text.lower()
    blob = TextBlob(text)
    polarity     = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # ── 1. CRISIS ─────────────────────────────────────────────────────────────
    # Only flag Crisis for clear self-harm / suicidal intent.
    # Standalone "dead" / "death" / "die" are ambiguous ("i'm dead tired",
    # "deadline", "die laughing") — so we require them to appear in a clear
    # intent phrase rather than as a bare word.
    crisis_phrases = [
        "i want to die", "i wanna die", "want to die",
        "i want to be dead", "wish i was dead", "better off dead",
        "i am going to kill myself", "kill myself", "killing myself",
        "end my life", "end it all", "take my life", "take my own life",
        "suicide", "suicidal",
        "no reason to live", "don't want to live", "dont want to live",
        "not want to live", "can't go on", "cant go on",
        "can't do this anymore", "cant do this anymore",
        "self harm", "self-harm", "hurt myself",
        "cutting myself", "cut myself",
        "no point in living", "no purpose in life", "life is pointless",
        "nothing to live for", "disappear forever",
        "everyone would be better without me",
        "i should not be alive", "i don't deserve to live",
    ]
    if any(phrase in tl for phrase in crisis_phrases):
        return "Crisis"

    # ── 2. STRESSED ───────────────────────────────────────────────────────────
    # Broad list covering everyday words people actually type.
    stress_keywords = [
        # Core stress words
        "stressed", "stress", "stressful",
        "tensed", "tense", "tension",
        "overwhelmed", "overwhelming",
        "burnout", "burnt out", "burned out",
        "exhausted", "exhausting", "drained",
        "overloaded", "overworked",
        # Workload / time pressure
        "deadline", "deadlines",
        "too much to do", "so much to do", "a lot to do",
        "too much work", "so much work",
        "too much on my plate", "piled up",
        "no time", "running out of time", "out of time",
        "behind on", "falling behind", "way behind",
        "pressure", "under pressure",
        "can't cope", "cant cope", "can't handle", "cant handle",
        "can't keep up", "cant keep up",
        # Physical / emotional exhaustion
        "tired", "so tired", "very tired",
        "fatigued", "fatigue",
        "drained", "wiped out",
        "breaking down", "break down",
        "falling apart", "losing it",
        "at my limit", "at my wit",
        "drowning in", "buried in work",
        "frustrated", "frustrating", "frustration",
        "irritated", "irritating", "agitated",
        "fed up", "sick of this", "sick and tired",
        "can't take it", "cant take it",
        "everything is too much",
    ]
    if any(kw in tl for kw in stress_keywords):
        return "Stressed"

    # ── 3. ANXIOUS ────────────────────────────────────────────────────────────
    anxiety_keywords = [
        "anxious", "anxiety", "anxiousness",
        "nervous", "nervousness",
        "panic", "panicking", "panic attack",
        "scared", "scary", "terrified",
        "fear", "fearful", "afraid",
        "worried", "worrying", "worry", "worries",
        "restless", "restlessness",
        "on edge", "uneasy", "unease",
        "heart racing", "racing heart", "palpitations",
        "can't breathe", "cant breathe", "shortness of breath",
        "overthinking", "over thinking",
        "what if", "what if i", "spiraling",
        "dread", "dreading", "impending",
        "freaking out", "freak out",
        "something bad will happen", "going to happen",
    ]
    if any(kw in tl for kw in anxiety_keywords):
        return "Anxious"

    # ── 4. POLARITY FALLBACK ──────────────────────────────────────────────────
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    elif polarity < -0.1 and subjectivity > 0.5:
        return "Stressed"   # subjective + mildly negative → likely stressed
    else:
        return "Neutral"