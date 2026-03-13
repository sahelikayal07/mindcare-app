# 🌸 MindCare AI – Your Mental Health Companion

A beautiful, beginner-friendly mental health web app built with **Python** and **Streamlit**.  
Type how you're feeling → get your mood detected → receive personalised resources, tips, videos, music playlists, and mental health app links.

---

## 🖼️ What It Does

| Feature | Details |
|---|---|
| **Mood Detection** | Uses TextBlob NLP to classify your text into: Happy, Sad, Neutral, Stressed, or Anxious |
| **Personalised Resources** | Curated YouTube videos, Spotify playlists, meditation & therapy apps per emotion |
| **Coping Tips** | Practical, actionable self-care suggestions |
| **Crisis Links** | Emergency mental health helpline numbers always visible |
| **Polished UI** | Lavender theme, smooth animations, emoji cards, hover effects |

---

## 📁 Project Structure

```
mindcare-ai/
│
├── app.py               ← Main Streamlit application
├── emotion_detection.py ← TextBlob-based mood classifier
├── resources.py         ← Emotion → tips & links mapping
├── requirements.txt     ← Python dependencies
└── README.md            ← This file
```

---

## ⚙️ Installation & Setup

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/mindcare-ai.git
cd mindcare-ai
```

Or simply download the folder and `cd` into it.

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download TextBlob language data (one-time only)

```bash
python -m textblob.download_corpora
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Your browser will open automatically at **http://localhost:8501**

---

## 🎨 Visual Styling

- **Background**: Lavender gradient (`#E6E6FA` → `#D8D8F6`)
- **Font**: Nunito (Google Fonts) — warm and friendly
- **Animations**: Bouncing emojis, fade-in cards, hover lift effects, pop-in result cards
- **Cards**: White rounded cards with purple shadows for inputs, results, tips, and links
- **Button**: Gradient purple pill button with hover glow

---

## 🔗 Included Resource Links

Each emotion includes real, curated links:

- 🎵 YouTube music playlists (calm, happy, stress-relief)
- 🧘 Meditation apps: Calm, Headspace, Insight Timer, Smiling Mind
- 📱 Mental health apps: 7 Cups, BetterHelp, Woebot, Rootd, Sanvello, MindShift
- ▶️ TED Talks and guided exercises on YouTube
- 🌐 Indian helplines: iCall, Vandrevala Foundation

---

## 🚨 Crisis Resources

The app always displays emergency helpline numbers at the bottom of each result:

- **iCall India**: 9152987821
- **Vandrevala Foundation**: 1860-2662-345
- [More Helplines →](https://www.thelivelovelaughfoundation.org/find-help/helplines)

---

## 🧠 How Emotion Detection Works

`emotion_detection.py` uses **TextBlob** to analyse polarity and subjectivity scores,
combined with keyword matching for stress and anxiety terms:

| Emotion  | Logic |
|---|---|
| Happy    | Polarity > 0.3 |
| Sad      | Polarity < -0.3 |
| Neutral  | Polarity near 0, low subjectivity |
| Stressed | Stress keywords OR highly negative + subjective text |
| Anxious  | Anxiety keywords detected |

---

## ⚠️ Disclaimer

> MindCare AI is a supportive tool, **not a replacement** for professional mental health care.  
> If you are in distress, please contact a qualified mental health professional or a crisis helpline.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web UI framework
- [TextBlob](https://textblob.readthedocs.io/) – NLP sentiment analysis
- Python 3.8+

---

Made with 💜 for anyone who needs a little support today.