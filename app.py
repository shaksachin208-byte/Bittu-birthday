import streamlit as st
import time
import random

# Page setup
st.set_page_config(page_title="Happy Birthday Bittu 🎂", page_icon="🎉", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ff9966 0%, #ff5e62 100%);
            color: #333;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.8em;
            color: white;
            text-shadow: 2px 2px 15px #ff0055;
            font-weight: 700;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3em;
            color: black;
            margin-top: -10px;
        }
        .section {
            background: rgba(255, 255, 255, 0.92);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
        h2 {
            color: #ff5e62;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            margin-top: 50px;
            color: black;
        }
        .emoji {
            font-size: 1.4em;
        }
    </style>
""", unsafe_allow_html=True)

# Balloons 🎈
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

typing_effect("🎉 Happy Birthday, Bittu! 🎂")

st.markdown("<p class='subtitle'>Celebrating the birthday of my lil bro Rudraksh — the Free Fire legend himself 💫</p>", unsafe_allow_html=True)

# 🎂 Birthday Section
with st.container():
    st.markdown("<div class='section'><h2>🎂 Birthday Wishes 🎉</h2>", unsafe_allow_html=True)
    st.write("""
    **Dear Bittu,**  

    Today is *your* day, little champ! 🥳  
    Wishing you a birthday filled with **smiles, laughter, and endless Booyahs!** 🎮  

    You’re more than just my K's brother —  
    you’re my **own little bro**, my **gaming partner**, and my **favorite chaos machine** 😄  

    May your year ahead be full of happiness, success, and epic Free Fire moments 💥  
    Keep shining, keep smiling, and never stop being YOU! 💫  

    🎈 **Happy Birthday once again, Bittu!** You deserve all the love in the world ❤️  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# About Bittu
with st.container():
    st.markdown("<div class='section'><h2>🌟 Who is Bittu?</h2>", unsafe_allow_html=True)
    st.write("""
    Meet **Rudraksh**, lovingly known as **Bittu** —  
    the younger brother of my Kittuu and my *younger bro*! 💪  

    Always full of energy, jokes, and life —  
    Bittu is that one person who can make any boring moment fun. 😎  
    He’s the **spark** in every group and the **vibe** in every game! ⚡
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Free Fire Section
with st.container():
    st.markdown("<div class='section'><h2>🔥 Free Fire Partner</h2>", unsafe_allow_html=True)
    st.write("""
    Our **Free Fire** duo is unstoppable — from last-zone madness to surprise victories!  
    Playing with Bittu isn’t just a game, it’s an **adventure** every single time.  

    He brings the **clutch**, the **confidence**, and the **chaos**! 💥  
    Whether it’s roasting each other or celebrating a win —  
    every match is a story worth remembering. 🎮  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Brother Bond Section
with st.container():
    st.markdown("<div class='section'><h2>🤝 Big Bro x Little Bro Bond</h2>", unsafe_allow_html=True)
    st.write("""
    I may be older by a few years, but in **fun, humor, and gaming**,  
    Bittu is my **equal** — or sometimes even the boss 😂  

    From endless Free Fire talks to random jokes,  
    our bond is pure **brotherhood** — no conditions, no filters, just fun and trust ❤️  

    You’ve grown up fast, Bittu — and I’m proud to be your **big bro**.  
    Keep rocking, keep winning, and keep being awesome! 💫
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Random Compliment
compliments = [
    "Bittu’s smile = 100% positive energy 🌞",
    "If Bittu were in Free Fire, he’d be a *mythic skin* 😎",
    "No photo needed — his energy lights up the room 💥",
    "Bittu’s vibe is stronger than any 1v4 clutch 😆",
    "few years younger, but 100 years wiser in fun! 🎉"
]
st.markdown(f"<div class='section'><h2>💬 Fun Fact About Bittu:</h2><p>{random.choice(compliments)}</p></div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        Made with ❤️ by his big bro (and Free Fire partner) | Streamlit 🎮  
        <br>Happy Birthday, Bittu! 🎂🎈
    </div>
""", unsafe_allow_html=True)
