# app.py — MindCare AI  |  run: streamlit run app.py
import csv, os, streamlit as st, pandas as pd, altair as alt
from datetime import datetime
from textblob import TextBlob

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="MindCare AI 🌸", page_icon="🌸", layout="centered")

# ─────────────────────────────────────────────────────────────────────────────
# MOOD LOG HELPERS
# ─────────────────────────────────────────────────────────────────────────────
LOG_FILE    = "mood_log.csv"
LOG_HEADERS = ["date", "time", "mood", "note"]
MOOD_OPTIONS = ["😀 Happy", "😐 Neutral", "😢 Sad", "😰 Stressed", "😨 Anxious"]
MOOD_COLORS  = {
    "😀 Happy":    "#f9a825",
    "😐 Neutral":  "#558b2f",
    "😢 Sad":      "#1565c0",
    "😰 Stressed": "#c62828",
    "😨 Anxious":  "#283593",
}

def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=LOG_HEADERS).writeheader()

def append_mood(mood, note=""):
    init_log()
    now = datetime.now()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=LOG_HEADERS).writerow({
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M"),
            "mood": mood,
            "note": note.strip(),
        })

def read_log():
    init_log()
    with open(LOG_FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

init_log()

# ─────────────────────────────────────────────────────────────────────────────
# EMOTION DETECTION
# ─────────────────────────────────────────────────────────────────────────────
def detect_emotion(text):
    if not text.strip(): return "Neutral"
    tl = text.lower()
    # Crisis check — highest priority
    crisis_kw = [
        "die", "dying", "dead", "death", "i want to die", "i wanna die",
        "wish i was dead", "better off dead", "want to be dead",
        "suicide", "suicidal", "kill myself", "end my life", "end it all",
        "take my life", "no reason to live", "don't want to live",
        "dont want to live", "can't go on", "cant go on",
        "can't do this anymore", "cant do this anymore",
        "self harm", "self-harm", "hurt myself", "cut myself",
        "no point", "nothing to live for", "disappear forever",
        "everyone would be better without me",
    ]
    if any(p in tl for p in crisis_kw): return "Crisis"
    if any(w in tl for w in ["stressed","overwhelmed","burnout","exhausted","deadline",
                              "pressure","too much","no time","tired","can't cope"]): return "Stressed"
    if any(w in tl for w in ["anxious","anxiety","nervous","panic","scared","fear",
                              "worried","worry","restless","on edge","overthinking"]): return "Anxious"
    pol = TextBlob(text).sentiment.polarity
    if pol > 0.3:  return "Happy"
    if pol < -0.3: return "Sad"
    return "Neutral"

# ─────────────────────────────────────────────────────────────────────────────
# RESOURCES  — 5–6 links per emotion
# ─────────────────────────────────────────────────────────────────────────────
RESOURCES = {
    "Happy": {
        "msg": "You're radiating great energy today! 🌟 Keep nurturing that positivity — it's contagious.",
        "tips": [
            "🌻 Share your happiness — call or text someone you care about.",
            "📓 Journal what made today great so you can revisit it later.",
            "🎯 Channel this energy into a goal or creative project.",
            "🙏 Practice gratitude — list 3 things you're thankful for.",
            "💃 Celebrate yourself — you deserve to feel this good!",
        ],
        "links": [
            ("🎵", "Happy Vibes Playlist (YouTube)",        "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("🎧", "Feel Good Music – Spotify",             "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"),
            ("🧘", "Headspace – Mindfulness App",           "https://www.headspace.com/"),
            ("📱", "Daylio – Mood Tracker App",             "https://daylio.net/"),
            ("▶️", "The Science of Happiness (TED)",        "https://www.youtube.com/watch?v=GXy__kBVq1M"),
            ("🌐", "Action for Happiness",                  "https://actionforhappiness.org/"),
        ],
    },
    "Sad": {
        "msg": "It's okay to feel sad — emotions are valid and you are not alone. 💙 Be gentle with yourself today.",
        "tips": [
            "💧 Allow yourself to feel — don't bottle it up.",
            "🤗 Reach out to a trusted friend, family member, or counselor.",
            "🌿 Step outside for fresh air — even a short walk can help.",
            "🍵 Make yourself a warm drink and rest without guilt.",
            "📖 Try reading, drawing, or any calming creative outlet.",
        ],
        "links": [
            ("🎵", "Comforting Playlist (YouTube)",         "https://www.youtube.com/watch?v=viimfQi_pUw"),
            ("📱", "7 Cups – Free Online Support",          "https://www.7cups.com/"),
            ("🧠", "BetterHelp – Online Counseling",        "https://www.betterhelp.com/"),
            ("▶️", "How to Deal with Sadness (YouTube)",    "https://www.youtube.com/watch?v=uMNgCFBzMuA"),
            ("📱", "Woebot – Mental Health Chatbot",        "https://woebothealth.com/"),
            ("🌐", "iCall – Indian Mental Health Helpline", "https://icallhelpline.org/"),
        ],
    },
    "Neutral": {
        "msg": "You seem calm and balanced today. 😌 This is a wonderful state for reflection and gentle self-care.",
        "tips": [
            "☁️ Use this calm to set small, meaningful intentions.",
            "🧘 Try a short meditation to deepen your sense of peace.",
            "📚 Pick up a book or podcast that inspires you.",
            "🌱 Do something kind for yourself or someone else.",
            "🎨 Explore a new hobby or creative activity.",
        ],
        "links": [
            ("🎵", "Lo-Fi Chill Music for Focus (YouTube)", "https://www.youtube.com/watch?v=jfKfPfyJRdk"),
            ("🧘", "Calm App – Meditation & Sleep",         "https://www.calm.com/"),
            ("🧘", "Insight Timer – Free Meditations",      "https://insighttimer.com/"),
            ("▶️", "Mindfulness for Beginners (YouTube)",   "https://www.youtube.com/watch?v=6p_yaNFSYao"),
            ("📱", "Smiling Mind – Free Mindfulness App",   "https://www.smilingmind.com.au/"),
            ("🌐", "Greater Good Science Center",           "https://greatergood.berkeley.edu/"),
        ],
    },
    "Stressed": {
        "msg": "You're carrying a lot right now. 🌬️ Let's slow down together — one breath at a time.",
        "tips": [
            "🫁 Box breathing: Inhale 4s → Hold 4s → Exhale 4s → Hold 4s.",
            "📝 Brain dump — write everything stressing you onto paper.",
            "⏸️ Take a 5-minute tech break and step away from screens.",
            "🏃 Light physical movement (a walk, stretching) reduces cortisol.",
            "🍽️ Drink water and eat something nourishing — your body needs fuel.",
        ],
        "links": [
            ("🎵", "Stress Relief Music (YouTube)",         "https://www.youtube.com/watch?v=lFcSrYw-ARY"),
            ("🧘", "Calm – Breathing Exercises",            "https://www.calm.com/"),
            ("▶️", "5-Min Stress Relief Meditation",        "https://www.youtube.com/watch?v=inpok4MKVLM"),
            ("📱", "Headspace – Stress & Anxiety Pack",     "https://www.headspace.com/stress-anxiety"),
            ("▶️", "How to Manage Stress (TED Talk)",       "https://www.youtube.com/watch?v=hnpQrMqDoqE"),
            ("📱", "Sanvello – Stress & Anxiety App",       "https://www.sanvello.com/"),
        ],
    },
    "Crisis": {
        "msg": "What you're feeling right now sounds very painful, and I'm really glad you reached out. 💙 You are not alone — please talk to someone who can help right now.",
        "tips": [
            "📞 Please call or text a crisis helpline right now — trained counselors are there 24/7.",
            "🤝 Reach out to someone you trust — a friend, family member, or teacher.",
            "🏥 If you are in immediate danger, go to your nearest emergency room or call emergency services.",
            "🌬️ Try to slow your breathing — inhale for 4 counts, exhale for 6 counts.",
            "💬 You don't have to face this alone. Talking helps. Someone cares about you.",
        ],
        "links": [
            ("📞", "iCall India – 9152987821 (Free, Confidential)",  "https://icallhelpline.org/"),
            ("📞", "Vandrevala Foundation – 1860-2662-345 (24/7)",   "https://www.vandrevalafoundation.com/"),
            ("📞", "Snehi India – 044-24640050",                      "https://www.snehiindia.org/"),
            ("🌐", "iCall – Chat & Email Support",                    "https://icallhelpline.org/"),
            ("🌐", "The Live Love Laugh – All India Helplines",       "https://www.thelivelovelaughfoundation.org/find-help/helplines"),
            ("▶️", "You Are Not Alone – Crisis Support Video",        "https://www.youtube.com/watch?v=oWMaRNs_9KU"),
        ],
    },
    "Anxious": {
        "msg": "Anxiety can feel overwhelming, but you are safe right now. 🌊 Let's try some grounding together.",
        "tips": [
            "🖐️ 5-4-3-2-1: Name 5 things you see, 4 you touch, 3 you hear, 2 you smell, 1 you taste.",
            "🫁 Slow your breath: inhale for 4 counts, exhale for 6.",
            "🧊 Hold something cold — it interrupts the panic response.",
            "📵 Limit news and social media — they often amplify anxiety.",
            "💬 Talk to someone you trust about what's worrying you.",
        ],
        "links": [
            ("🎵", "Anxiety Relief Music (YouTube)",        "https://www.youtube.com/watch?v=1vx8iUvfyCY"),
            ("▶️", "Grounding Technique for Anxiety",       "https://www.youtube.com/watch?v=30VMIEmA114"),
            ("📱", "Rootd – Panic Attack & Anxiety Relief", "https://www.rootd.io/"),
            ("🧘", "Headspace – Managing Anxiety",          "https://www.headspace.com/anxiety"),
            ("▶️", "Understanding Anxiety (TED Talk)",      "https://www.youtube.com/watch?v=aX7jnVXXG5o"),
            ("📱", "MindShift CBT – Anxiety Canada",        "https://www.anxietycanada.com/resources/mindshift-cbt/"),
        ],
    },
}

EMOTION_CFG = {
    "Happy":    {"emoji": "😊", "bg": "#fff9c4", "border": "#f9a825", "col": "#e65100"},
    "Sad":      {"emoji": "😢", "bg": "#e3f2fd", "border": "#1565c0", "col": "#1565c0"},
    "Neutral":  {"emoji": "😌", "bg": "#f1f8e9", "border": "#558b2f", "col": "#33691e"},
    "Stressed": {"emoji": "😤", "bg": "#fce4ec", "border": "#c62828", "col": "#b71c1c"},
    "Anxious":  {"emoji": "😰", "bg": "#e8eaf6", "border": "#283593", "col": "#1a237e"},
    "Crisis":   {"emoji": "🆘", "bg": "#fce4ec", "border": "#b71c1c", "col": "#b71c1c"},
}

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS  — every color is explicit; nothing relies on Streamlit's theme
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"], .stApp, .block-container,
div, p, span, label, li, td, th, small, strong, b, a {
    font-family: 'Nunito', sans-serif !important;
}
.stApp {
    background: linear-gradient(145deg, #e6e6fa 0%, #d8d8f6 45%, #ede7f6 100%) !important;
}
.block-container {
    max-width: 760px !important;
    padding-top: 1.6rem !important;
    padding-bottom: 3rem !important;
}

/* ── Force ALL streamlit text dark ── */
.stMarkdown, .stMarkdown p, .stMarkdown li,
.stText, [data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span,
[data-testid="stCaptionContainer"],
.stAlert p, .stAlert span {
    color: #1a1a2e !important;
}

/* ── Headings ── */
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    color: #4a2c8a !important;
    font-weight: 800 !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: white !important;
    border-radius: 16px !important;
    padding: 1rem !important;
    box-shadow: 0 4px 16px rgba(120,90,180,0.13) !important;
    border: 1.5px solid #e8e0f8 !important;
}
[data-testid="stMetricLabel"] > div,
[data-testid="stMetricLabel"] > div > div,
[data-testid="stMetricLabel"] p {
    color: #5c35a0 !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
}
[data-testid="stMetricValue"] > div,
[data-testid="stMetricValue"] div {
    color: #2d1b6e !important;
    font-weight: 800 !important;
    font-size: 1.5rem !important;
}

/* ── Labels on selectbox / textarea ── */
.stSelectbox label, .stSelectbox label p,
.stTextArea label, .stTextArea label p {
    color: #4a2c8a !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
}

/* ── Input fields ── */
.stTextArea textarea, .stSelectbox > div > div {
    border-radius: 12px !important;
    border: 2px solid #d8d0f0 !important;
    background: #faf9ff !important;
    color: #1a1a2e !important;
    font-size: 0.95rem !important;
}
.stTextArea textarea:focus {
    border-color: #7c4dff !important;
    box-shadow: 0 0 0 3px rgba(124,77,255,0.14) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #7c4dff, #b39ddb) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 50px !important;
    width: 100% !important;
    padding: 0.62rem 1.5rem !important;
    box-shadow: 0 4px 14px rgba(124,77,255,0.35) !important;
    transition: all 0.25s ease !important;
    letter-spacing: 0.2px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #5e35b1, #7c4dff) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(124,77,255,0.5) !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    background: #fff !important;
    border-radius: 14px !important;
    border: 1.5px solid #e0d7f5 !important;
}
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: #880e4f !important;
    font-weight: 700 !important;
}

/* ── Info/success/warning boxes ── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border-radius: 14px !important;
    overflow: hidden !important;
}

/* ── Divider ── */
hr { border-color: #d8d0f0 !important; margin: 1.6rem 0 !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Animations ── */
@keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
@keyframes fadeUp { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }
@keyframes popIn  { 0%{opacity:0;transform:scale(0.88)} 70%{transform:scale(1.03)} 100%{opacity:1;transform:scale(1)} }
</style>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# SECTION 1 — HERO
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#ffffff,#f3f0ff);border-radius:24px;
            padding:2.2rem 2rem 1.8rem;text-align:center;
            box-shadow:0 8px 32px rgba(120,90,180,0.16);margin-bottom:1.4rem;
            animation:fadeUp .6s ease;">
  <div style="font-size:3rem;animation:bounce 2s infinite;display:inline-block;">🌸</div>
  <div style="font-size:2.1rem;font-weight:800;color:#4a2c8a;margin:.25rem 0;">MindCare AI</div>
  <div style="font-size:1.15rem;color:#7c4dff;font-weight:700;">Your Mental Health Companion</div>
  <div style="font-size:.92rem;color:#6b6b8a;margin-top:.4rem;line-height:1.5;">
    A safe, supportive space to check in with how you're feeling 💜
  </div>
</div>
""", unsafe_allow_html=True)

# Icon row
for col, icon, label in zip(st.columns(5),
    ["🧠","💙","🌱","✨","🌈"],
    ["Mindful","Caring","Growing","Positive","Hopeful"]):
    col.markdown(
        f"<div style='text-align:center;padding:.4rem 0;'>"
        f"<div style='font-size:1.7rem;'>{icon}</div>"
        f"<div style='color:#6b6b8a;font-weight:700;font-size:.78rem;margin-top:.2rem;'>{label}</div>"
        f"</div>",
        unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# SECTION 2 — EMOTION DETECTION
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="background:#ffffff;border-radius:20px;padding:1.6rem 1.8rem;
            box-shadow:0 4px 20px rgba(120,90,180,0.12);margin-bottom:.8rem;">
  <div style="font-size:1.1rem;font-weight:800;color:#4a2c8a;margin-bottom:.35rem;">
    💬 How are you feeling today?
  </div>
  <div style="color:#6b6b8a;font-size:.88rem;line-height:1.5;">
    Share your thoughts freely — this is your safe space. Everything stays private. 🔒
  </div>
</div>
""", unsafe_allow_html=True)

user_input = st.text_area(
    "thoughts",
    placeholder="e.g. I'm feeling overwhelmed with work and can't seem to relax…",
    height=115,
    label_visibility="collapsed",
)

_, bc, _ = st.columns([1, 2, 1])
with bc:
    go = st.button("🔍 Analyze My Mood")

if go:
    if not user_input.strip():
        st.warning("🌸 Please write something about how you're feeling first!")
    else:
        emotion = detect_emotion(user_input)
        cfg = EMOTION_CFG[emotion]
        res = RESOURCES[emotion]

        # ── Crisis urgent banner (shown before result card) ──
        if emotion == "Crisis":
            st.markdown("""
            <div style="background:linear-gradient(135deg,#b71c1c,#e53935);
                        border-radius:16px;padding:1.4rem 1.6rem;margin-bottom:1rem;
                        box-shadow:0 6px 20px rgba(183,28,28,0.35);text-align:center;">
              <div style="font-size:1.5rem;font-weight:800;color:#ffffff;margin-bottom:.4rem;">
                🆘 You are not alone — help is available right now
              </div>
              <div style="color:#ffcdd2;font-size:.95rem;line-height:1.6;">
                If you are having thoughts of suicide or self-harm, please reach out immediately.<br>
                <strong style="color:#ffffff;">iCall India: 9152987821</strong> &nbsp;|&nbsp;
                <strong style="color:#ffffff;">Vandrevala: 1860-2662-345</strong> &nbsp;|&nbsp;
                <strong style="color:#ffffff;">Emergency: 112</strong>
              </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Emotion result card ──
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{cfg['bg']},#ffffff);
                    border:2px solid {cfg['border']};border-radius:20px;
                    padding:1.6rem;text-align:center;margin:1rem 0;
                    box-shadow:0 6px 24px rgba(120,90,180,0.18);animation:popIn .5s ease;">
          <div style="font-size:3.4rem;animation:bounce 1.5s infinite;display:inline-block;">
            {cfg['emoji']}
          </div>
          <div style="font-size:2rem;font-weight:800;color:{cfg['col']};margin:.2rem 0;">
            {emotion}
          </div>
          <div style="font-size:.97rem;color:#3d3d5c;line-height:1.65;margin-top:.5rem;">
            {res['msg']}
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Tips card ──
        st.markdown("""
        <div style="font-size:1.1rem;font-weight:800;color:#4a2c8a;margin:1.4rem 0 .6rem;">
          💡 Personalised Tips for You
        </div>""", unsafe_allow_html=True)

        tips_rows = "".join(
            f'<div style="padding:.45rem .2rem;border-bottom:1px dashed #d8ccf0;'
            f'font-size:.93rem;color:#2d2d4e;line-height:1.5;">{t}</div>'
            for t in res["tips"]
        )
        st.markdown(
            f'<div style="background:linear-gradient(135deg,#f8f5ff,#ede7f6);'
            f'border-radius:16px;padding:1.2rem 1.5rem;'
            f'box-shadow:0 3px 12px rgba(120,90,180,0.09);">'
            f'<div style="font-weight:700;color:#4a2c8a;margin-bottom:.5rem;">Try these gentle actions:</div>'
            f'{tips_rows}</div>',
            unsafe_allow_html=True)

        # ── Resource links ──
        st.markdown("""
        <div style="font-size:1.1rem;font-weight:800;color:#4a2c8a;margin:1.4rem 0 .6rem;">
          🔗 Helpful Resources &amp; Links
        </div>""", unsafe_allow_html=True)

        for icon, label, url in res["links"]:
            st.markdown(
                f'<div style="background:#ffffff;border:1.5px solid #e0d7f5;border-radius:14px;'
                f'padding:1rem 1.2rem;margin-bottom:.55rem;'
                f'box-shadow:0 2px 8px rgba(120,90,180,0.08);'
                f'transition:box-shadow .2s;">'
                f'<span style="font-size:1.2rem;">{icon}</span>'
                f'&nbsp;&nbsp;<a href="{url}" target="_blank" rel="noopener noreferrer" '
                f'style="color:#4a2c8a;font-weight:700;text-decoration:none;font-size:.95rem;">'
                f'{label}</a>'
                f'<span style="float:right;color:#b39ddb;font-size:.82rem;margin-top:.15rem;">↗ Open</span>'
                f'</div>',
                unsafe_allow_html=True)

        # ── Crisis banner ──
        st.markdown("""
        <div style="background:linear-gradient(135deg,#fce4ec,#f8bbd0);
                    border:1.5px solid #e91e63;border-radius:14px;
                    padding:1rem 1.4rem;text-align:center;margin-top:.8rem;">
          <span style="color:#880e4f;font-size:.92rem;">
            <strong>🚨 In crisis or need immediate help?</strong><br>
            iCall India: <strong>9152987821</strong> &nbsp;|&nbsp;
            Vandrevala Foundation: <strong>1860-2662-345</strong> &nbsp;|&nbsp;
            <a href="https://www.thelivelovelaughfoundation.org/find-help/helplines"
               target="_blank" style="color:#880e4f;font-weight:700;">More Helplines ↗</a>
          </span>
        </div>
        """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# SECTION 3 — MOOD TRACKER
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# Tracker header banner
st.markdown("""
<div style="background:linear-gradient(135deg,#7c4dff,#9c6fff);
            border-radius:20px;padding:1.5rem 1.8rem;
            box-shadow:0 6px 24px rgba(124,77,255,0.3);margin-bottom:1.2rem;">
  <div style="font-size:1.65rem;font-weight:800;color:#ffffff;margin-bottom:.2rem;">
    📓 Mood Tracker
  </div>
  <div style="font-size:.9rem;color:#ede7f6;line-height:1.5;">
    Log your mood daily and watch your emotional patterns unfold over time 🌿
  </div>
</div>
""", unsafe_allow_html=True)


# ── Log form ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="font-size:1.15rem;font-weight:800;color:#4a2c8a;margin-bottom:.7rem;">
  ✍️ Log Today's Mood
</div>
""", unsafe_allow_html=True)

log_card_style = ("background:#ffffff;border-radius:18px;padding:1.4rem 1.6rem;"
                  "box-shadow:0 4px 18px rgba(120,90,180,0.11);margin-bottom:1rem;")

st.markdown(f'<div style="{log_card_style}">', unsafe_allow_html=True)
fc1, fc2 = st.columns(2, gap="medium")
with fc1:
    selected_mood = st.selectbox("Select your mood 👇", MOOD_OPTIONS)
with fc2:
    mood_note = st.text_area("📝 Optional note",
                             placeholder="e.g. Went for a walk and felt better 🌤️",
                             height=95)
st.markdown('</div>', unsafe_allow_html=True)

_, sc, _ = st.columns([1, 2, 1])
with sc:
    if st.button("💾 Save Mood Entry"):
        append_mood(selected_mood, mood_note)
        st.success(f"{selected_mood} — mood saved successfully! Keep checking in 🌸")

st.markdown("<br>", unsafe_allow_html=True)


# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="font-size:1.15rem;font-weight:800;color:#4a2c8a;margin-bottom:.7rem;">
  📊 Your Mood Stats
</div>
""", unsafe_allow_html=True)

history = read_log()
c1, c2, c3, c4 = st.columns(4)
c1.metric("📝 Total Entries",  len(history))
c2.metric("📅 Days Tracked",   len(set(e["date"] for e in history)) if history else 0)
c3.metric("😊 Latest Mood",    history[-1]["mood"] if history else "—")
c4.metric("🗓️ Last Logged",   history[-1]["date"] if history else "—")

st.markdown("<br>", unsafe_allow_html=True)


# ── Bar chart ─────────────────────────────────────────────────────────────────
st.markdown("""
<div style="font-size:1.15rem;font-weight:800;color:#4a2c8a;margin-bottom:.7rem;">
  📈 Mood Trends Chart
</div>
""", unsafe_allow_html=True)

counts = {m: 0 for m in MOOD_OPTIONS}
for e in history:
    if e["mood"] in counts:
        counts[e["mood"]] += 1

if sum(counts.values()) == 0:
    st.markdown("""
    <div style="background:#fff;border-radius:14px;padding:2rem;text-align:center;
                box-shadow:0 2px 10px rgba(120,90,180,0.09);">
      <div style="font-size:2.5rem;">🌱</div>
      <div style="color:#6b6b8a;font-weight:700;margin-top:.5rem;">
        No mood data yet — save your first entry above to see trends!
      </div>
    </div>""", unsafe_allow_html=True)
else:
    df_chart = pd.DataFrame({
        "Mood":  list(counts.keys()),
        "Count": list(counts.values()),
    })
    bar = (
        alt.Chart(df_chart)
        .mark_bar(cornerRadiusTopLeft=9, cornerRadiusTopRight=9)
        .encode(
            x=alt.X("Mood:N", sort=MOOD_OPTIONS,
                    axis=alt.Axis(labelAngle=0, labelFontSize=12, labelColor="#4a2c8a")),
            y=alt.Y("Count:Q", axis=alt.Axis(tickMinStep=1, labelColor="#4a2c8a"),
                    title="Number of Entries"),
            color=alt.Color("Mood:N",
                scale=alt.Scale(domain=list(MOOD_COLORS.keys()),
                                range=list(MOOD_COLORS.values())),
                legend=None),
            tooltip=["Mood:N", "Count:Q"],
        )
        .properties(height=290, background="#faf9ff",
            title=alt.TitleParams("How Often Have You Felt Each Mood?",
                                  fontSize=13, color="#4a2c8a", fontWeight="bold"))
        .configure_view(strokeWidth=0)
        .configure_axis(grid=False, domainColor="#e0d7f5")
    )
    st.altair_chart(bar, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── History table ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="font-size:1.15rem;font-weight:800;color:#4a2c8a;margin-bottom:.7rem;">
  🗂️ Mood History Log
</div>
""", unsafe_allow_html=True)

if not history:
    st.info("📭 No entries yet — log your first mood above!")
else:
    df = pd.DataFrame(history[::-1])
    df.columns = ["Date", "Time", "Mood", "Note"]
    df["Note"] = df["Note"].replace("", "—")
    st.dataframe(
        df.head(50),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Date": st.column_config.TextColumn("📅 Date", width="small"),
            "Time": st.column_config.TextColumn("🕐 Time", width="small"),
            "Mood": st.column_config.TextColumn("😊 Mood", width="medium"),
            "Note": st.column_config.TextColumn("📝 Note", width="large"),
        },
    )
    if len(history) > 50:
        st.caption(f"Showing 50 most recent of {len(history)} total entries.")

st.markdown("<br>", unsafe_allow_html=True)


# ── Danger zone ───────────────────────────────────────────────────────────────
with st.expander("⚠️ Clear All Mood Data"):
    st.warning("This will permanently delete your entire mood history. This cannot be undone.")
    if st.checkbox("✅ Yes, I understand — delete all my mood data"):
        _, dc, _ = st.columns([1, 2, 1])
        with dc:
            if st.button("🗑️ Clear Mood History"):
                with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
                    csv.DictWriter(f, fieldnames=LOG_HEADERS).writeheader()
                st.success("✅ Mood history cleared.")
                st.rerun()


# ═════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#9090b0;font-size:.8rem;padding-bottom:1rem;line-height:1.7;">
  Made with 💜 using Streamlit · TextBlob · Altair &nbsp;|&nbsp;
  MindCare AI is not a substitute for professional mental health care.<br>
  If you are in distress, please reach out to a qualified professional. 🌸
</div>
""", unsafe_allow_html=True)