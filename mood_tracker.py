# mood_tracker.py
# Handles all Mood Tracker logic: saving entries, loading history, and chart data.

import csv
import os
from datetime import datetime

# ─── File path for the mood log CSV ───
MOOD_LOG_FILE = "mood_log.csv"

# ─── CSV column headers ───
CSV_HEADERS = ["date", "time", "mood", "note"]

# ─── Emoji map for each mood label ───
MOOD_EMOJI = {
    "😀 Happy":   "😀",
    "😐 Neutral": "😐",
    "😢 Sad":     "😢",
    "😰 Stressed":"😰",
    "😨 Anxious": "😨",
}

# ─── Color map for chart bars (matches app theme) ───
MOOD_COLORS = {
    "😀 Happy":   "#f9a825",
    "😐 Neutral": "#558b2f",
    "😢 Sad":     "#1565c0",
    "😰 Stressed":"#c62828",
    "😨 Anxious": "#283593",
}


def ensure_csv_exists():
    """
    Create the mood_log.csv file with headers if it doesn't exist yet.
    Called once at app startup.
    """
    if not os.path.exists(MOOD_LOG_FILE):
        with open(MOOD_LOG_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()


def save_mood_entry(mood: str, note: str = "") -> None:
    """
    Append a new mood entry to the CSV log with the current date and time.

    Parameters:
        mood (str): The selected mood label (e.g. '😀 Happy').
        note (str): Optional user note (can be empty string).
    """
    ensure_csv_exists()
    now = datetime.now()
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "mood": mood,
        "note": note.strip() if note else "",
    }
    with open(MOOD_LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writerow(entry)


def load_mood_history() -> list[dict]:
    """
    Load all mood entries from the CSV file as a list of dicts.
    Returns an empty list if no entries exist yet.

    Returns:
        list[dict]: Each dict has keys: date, time, mood, note.
    """
    ensure_csv_exists()
    entries = []
    with open(MOOD_LOG_FILE, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append(dict(row))
    return entries


def get_mood_counts(history: list[dict]) -> dict:
    """
    Count how many times each mood appears in the history.

    Parameters:
        history (list[dict]): Output of load_mood_history().

    Returns:
        dict: { mood_label: count } for all moods (0 if never logged).
    """
    # Initialise all moods to 0 so every bar always appears in chart
    counts = {mood: 0 for mood in MOOD_EMOJI.keys()}
    for entry in history:
        mood = entry.get("mood", "")
        if mood in counts:
            counts[mood] += 1
    return counts


def get_streak_info(history: list[dict]) -> dict:
    """
    Calculate basic streak stats from mood history.

    Returns:
        dict with keys:
            total_entries (int)
            unique_days   (int)
            latest_mood   (str)
            latest_date   (str)
    """
    if not history:
        return {
            "total_entries": 0,
            "unique_days": 0,
            "latest_mood": "—",
            "latest_date": "—",
        }

    unique_days = len(set(e["date"] for e in history))
    latest = history[-1]
    return {
        "total_entries": len(history),
        "unique_days": unique_days,
        "latest_mood": latest["mood"],
        "latest_date": latest["date"],
    }
