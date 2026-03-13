# resources.py
# Returns tailored mental health resources, advice, and links based on detected emotion.

def get_resources(emotion: str) -> dict:
    """
    Return a dictionary of resources and supportive messages for a given emotion.

    Each entry contains:
        - message (str): A warm, supportive opening message.
        - tips (list of str): Practical coping tips.
        - links (list of dict): Each dict has 'label', 'url', and 'icon'.

    Parameters:
        emotion (str): One of 'Happy', 'Sad', 'Neutral', 'Stressed', 'Anxious'

    Returns:
        dict: Resource bundle for displaying in the Streamlit UI.
    """

    resources = {

        "Happy": {
            "message": "You're radiating great energy today! 🌟 Keep nurturing that positivity — it's contagious and powerful.",
            "tips": [
                "🌻 Share your happiness — call or text someone you care about.",
                "📓 Journal what made today great so you can revisit it later.",
                "🎯 Channel this energy into a goal or creative project.",
                "🙏 Practice gratitude — list 3 things you're thankful for.",
                "💃 Celebrate yourself — you deserve to feel good!",
            ],
            "links": [
                {"icon": "🎵", "label": "Happy Vibes Playlist (YouTube)", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
                {"icon": "🎧", "label": "Feel Good Music – Spotify Playlist", "url": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"},
                {"icon": "📱", "label": "Daylio – Mood Tracker App", "url": "https://daylio.net/"},
                {"icon": "🧘", "label": "Headspace – Mindfulness App", "url": "https://www.headspace.com/"},
                {"icon": "▶️", "label": "The Science of Happiness (TED Talk)", "url": "https://www.youtube.com/watch?v=GXy__kBVq1M"},
            ],
        },

        "Sad": {
            "message": "It's okay to feel sad — emotions are valid, and you're not alone. 💙 Be gentle with yourself today.",
            "tips": [
                "💧 Allow yourself to feel — don't bottle it up.",
                "🤗 Reach out to a trusted friend, family member, or counselor.",
                "🌿 Step outside for fresh air — even a short walk can help.",
                "🍵 Make yourself a warm drink and rest without guilt.",
                "📖 Try reading, drawing, or any calming creative outlet.",
            ],
            "links": [
                {"icon": "🎵", "label": "Comforting Sad Songs Playlist", "url": "https://www.youtube.com/watch?v=viimfQi_pUw"},
                {"icon": "📱", "label": "7 Cups – Free Online Therapy & Support", "url": "https://www.7cups.com/"},
                {"icon": "🧠", "label": "BetterHelp – Online Counseling", "url": "https://www.betterhelp.com/"},
                {"icon": "▶️", "label": "How to Deal with Sadness (YouTube)", "url": "https://www.youtube.com/watch?v=uMNgCFBzMuA"},
                {"icon": "📱", "label": "Woebot – Mental Health Chatbot", "url": "https://woebothealth.com/"},
                {"icon": "🌐", "label": "iCall – Indian Mental Health Helpline", "url": "https://icallhelpline.org/"},
            ],
        },

        "Neutral": {
            "message": "You seem calm and balanced today. 😌 This is a great state for reflection and gentle self-care.",
            "tips": [
                "☁️ Use this calm to set small, meaningful intentions for the day.",
                "🧘 Try a short meditation to deepen your sense of peace.",
                "📚 Pick up a book or podcast that inspires you.",
                "🌱 Do something kind for yourself or someone else.",
                "🎨 Explore a new hobby or creative activity.",
            ],
            "links": [
                {"icon": "🎵", "label": "Lo-Fi Chill Music for Focus", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
                {"icon": "🧘", "label": "Calm App – Meditation & Sleep", "url": "https://www.calm.com/"},
                {"icon": "🧘", "label": "Insight Timer – Free Meditations", "url": "https://insighttimer.com/"},
                {"icon": "▶️", "label": "Mindfulness for Beginners (YouTube)", "url": "https://www.youtube.com/watch?v=6p_yaNFSYao"},
                {"icon": "📱", "label": "Smiling Mind – Free Mindfulness App", "url": "https://www.smilingmind.com.au/"},
            ],
        },

        "Stressed": {
            "message": "You're carrying a lot right now. 🌬️ Let's slow down together — you've got this, one breath at a time.",
            "tips": [
                "🫁 Try box breathing: Inhale 4s → Hold 4s → Exhale 4s → Hold 4s.",
                "📝 Brain dump — write everything stressing you onto paper.",
                "⏸️ Take a 5-minute tech break and step away from screens.",
                "🏃 Light physical movement (a walk, stretching) reduces cortisol.",
                "🍽️ Drink water and eat something nourishing — your body needs fuel.",
            ],
            "links": [
                {"icon": "🎵", "label": "Stress Relief Music (YouTube)", "url": "https://www.youtube.com/watch?v=lFcSrYw-ARY"},
                {"icon": "🧘", "label": "Calm App – Breathing Exercises", "url": "https://www.calm.com/"},
                {"icon": "▶️", "label": "5-Minute Stress Relief Meditation", "url": "https://www.youtube.com/watch?v=inpok4MKVLM"},
                {"icon": "📱", "label": "Headspace – Stress & Anxiety Pack", "url": "https://www.headspace.com/stress-anxiety"},
                {"icon": "▶️", "label": "How to Manage Stress (TED Talk)", "url": "https://www.youtube.com/watch?v=hnpQrMqDoqE"},
                {"icon": "📱", "label": "Sanvello – Stress & Anxiety App", "url": "https://www.sanvello.com/"},
            ],
        },

        "Anxious": {
            "message": "Anxiety can feel overwhelming, but you are safe right now. 🌊 Let's try some grounding together.",
            "tips": [
                "🖐️ Try the 5-4-3-2-1 grounding technique: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste.",
                "🫁 Slow your breath: inhale for 4 counts, exhale for 6.",
                "🧊 Hold something cold (ice cube or cold water) — it interrupts the panic response.",
                "📵 Limit news/social media — they often amplify anxiety.",
                "💬 Talk to someone you trust about what's worrying you.",
            ],
            "links": [
                {"icon": "🎵", "label": "Anxiety Relief Music (YouTube)", "url": "https://www.youtube.com/watch?v=1vx8iUvfyCY"},
                {"icon": "▶️", "label": "Grounding Technique for Anxiety (YouTube)", "url": "https://www.youtube.com/watch?v=30VMIEmA114"},
                {"icon": "📱", "label": "Rootd – Panic Attack & Anxiety Relief", "url": "https://www.rootd.io/"},
                {"icon": "🧘", "label": "Headspace – Managing Anxiety", "url": "https://www.headspace.com/anxiety"},
                {"icon": "▶️", "label": "Understanding Anxiety (TED Talk)", "url": "https://www.youtube.com/watch?v=aX7jnVXXG5o"},
                {"icon": "📱", "label": "MindShift CBT – Anxiety Canada", "url": "https://www.anxietycanada.com/resources/mindshift-cbt/"},
            ],
        },
    }

    # Fallback to Neutral if somehow an unknown emotion is passed
    return resources.get(emotion, resources["Neutral"])