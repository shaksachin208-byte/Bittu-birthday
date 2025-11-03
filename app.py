import streamlit as st
import time
import random

# Page setup
st.set_page_config(page_title="Bittu's World 🌍", page_icon="🎮", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%);
            color: #333;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.6em;
            color: white;
            text-shadow: 2px 2px 15px #ff0055;
            font-weight: 700;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3em;
            color: grey;
            margin-top: -10px;
        }
        .section {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
        h2 {
            color: #ff4e50;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            margin-top: 50px;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Balloons for fun
st.balloons()

# Typing effect intro
def typing_effect(text, speed=0.05):
    typed = ""
    ph = st.empty()
    for ch in text:
        typed += ch
        ph.markdown(f"<h1 class='title'>{typed}</h1>", unsafe_allow_html=True)
        time.sleep(speed)
    time.sleep(0.3)

typing_effect("🎉 Welcome to Bittu's World 🎮")

st.markdown("<p class='subtitle'>A small tribute to my lil bro Rudraksh — the legend himself 💫</p>", unsafe_allow_html=True)

# About Section
with st.container():
    st.markdown("<div class='section'><h2>🌟 Who is Bittu?</h2>", unsafe_allow_html=True)
    st.write("""
    Meet **Rudraksh**, lovingly known as **Bittu** —  
    the little brother of my loved one and my *mini bro for life!* ❤️  

    He might be **younger**, but trust me —  
    his energy, jokes, and gaming skills make him a total vibe!  
    Always full of life, full of ideas, and full of madness 😆  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Gaming Section
with st.container():
    st.markdown("<div class='section'><h2>🔥 Free Fire Buddies</h2>", unsafe_allow_html=True)
    st.write("""
    When it comes to **Free Fire**, Bittu is my **teammate, strategist, and hype man**.  
    Whether it’s clutching in the last zone or getting roasted for camping 😜 —  
    we’ve done it all.  
    Every match turns into a **memory**, every win into **a celebration!** 🏆  

    🎮 **“Booyah with Bittu”** isn’t just a game — it’s an emotion!
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Relationship Section
with st.container():
    st.markdown("<div class='section'><h2>👦 Big Bro & Little Bro Bond</h2>", unsafe_allow_html=True)
    st.write("""
    Bittu is more than a gaming buddy —  
    he’s my **little bro**, my **mini version**, and sometimes my **biggest headache** 😂  

    From roasting each other to backing each other up,  
    we’ve built a bond that’s strong, honest, and full of fun.  

    He might be *younger by age*,  
    but in **loyalty, love, and laughter**, he’s way ahead. 💯
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Random Compliment / Fun Fact
compliments = [
    "Bittu = Energy + Vibes + Unlimited Laughter ⚡",
    "He might be younger, but his gaming IQ is 10 years ahead 😎",
    "Legend says Free Fire servers lag when Bittu joins 🔥",
    "No photo needed — Bittu’s aura speaks for itself 💫",
]
st.markdown(f"<div class='section'><h2>💬 Random Bittu Fact:</h2><p>{random.choice(compliments)}</p></div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        Made with ❤️ by his big bro (and Free Fire partner) 🚀
    </div>
""", unsafe_allow_html=True)
