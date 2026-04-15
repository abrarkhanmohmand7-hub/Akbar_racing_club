import streamlit as st
import time
import random

# 1. Page Configuration - Naya Naam "Real Casino"
st.set_page_config(
    page_title="Real Casino - Premium Gaming Hub",
    page_icon="🎰",
    layout="wide"
)

# --- SOUND & MUSIC LINKS ---
bg_music = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"
win_sfx = "https://www.myinstants.com/media/sounds/win-sound-effect.mp3"
loss_sfx = "https://www.myinstants.com/media/sounds/wrong-answer-126515.mp3"

def play_sound(url):
    st.markdown(f'<audio autoplay><source src="{url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# --- PREMIUM DARK CASINO CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #1a0033 0%, #000000 100%); color: #ffd700; }
    .stTabs [data-baseweb="tab-list"] { background-color: rgba(255, 215, 0, 0.1); border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #ffd700; font-weight: bold; }
    .stButton>button { border: 2px solid #ffd700; background-color: transparent; color: #ffd700; border-radius: 20px; transition: 0.5s; }
    .stButton>button:hover { background-color: #ffd700; color: black; box-shadow: 0px 0px 15px #ffd700; }
    h1, h2, h3 { color: #ffd700 !important; text-shadow: 2px 2px 4px #000000; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("💳 REAL CASINO WALLET")
st.sidebar.markdown("### Owner: Akbar Khan")
st.sidebar.divider()
st.sidebar.subheader("🏦 Faysal Bank")
st.sidebar.code("343931000002103")
st.sidebar.divider()
up_file = st.sidebar.file_uploader("Upload Deposit Screenshot", type=['jpg', 'png'])

# --- MAIN DASHBOARD ---
st.title("🎰 REAL CASINO")
st.write("Welcome to the most trusted gaming platform in Pakistan.")

# All Games Tabs
tabs = st.tabs(["🏏 Sports", "🚀 Aviator", "🎨 Color", "🃏 Teen Patti", "🔄 Andar Bahar", "🐯 Dragon vs Tiger"])

# --- TAB 1: SPORTS (Cricket) ---
with tabs[0]:
    st.subheader("🏏 Cricket Live Betting")
    c1, c2 = st.columns([2, 1])
    with c1:
        c_link = st.text_input("Admin: Match Link", "https://www.youtube.com/embed/live_stream_id")
        st.components.v1.iframe(c_link, height=400)
    with c2:
        st.radio("Select Winner:", ["Team A", "Team B", "Draw"], key="cric_bet")
        if st.button("Place Bet"):
            st.warning("Bet Submitted! Awaiting Admin Approval.")

# --- TAB 2: AVIATOR ---
with tabs[1]:
    st.subheader("🚀 Aviator Live")
    av_c1, av_c2 = st.columns([2, 1])
    if av_c2.button("🚀 TAKE OFF"):
        mult = 1.00
        crash = round(random.uniform(1.1, 5.0), 2)
        p_holder = av_c1.empty()
        while mult < crash:
            p_holder.markdown(f"<div style='border:5px solid #ffd700; padding:60px; border-radius:20px; text-align:center;'><h1 style='font-size:100px;'>{mult:.2f}x</h1></div>", unsafe_allow_html=True)
            time.sleep(0.1)
            mult += 0.05
        play_sound(loss_sfx)
        p_holder.markdown("<h1 style='color:red; text-align:center;'>💥 CRASHED!</h1>", unsafe_allow_html=True)

# --- TAB 6: DRAGON VS TIGER (With Full Control) ---
with tabs[5]:
    st.header("🐯 Dragon vs Tiger")
    with st.expander("🛠 Admin Control (Private)"):
        dt_win = st.radio("Next Winner:", ["Dragon", "Tiger", "Tie"])
    
    col_d, col_t = st.columns(2)
    if col_d.button("🐉 Dragon"):
        st.info("Card Shuffling...")
        time.sleep(2)
        if dt_win == "Dragon":
            play_sound(win_sfx)
            st.success("DRAGON WINS!"); st.balloons()
        else:
            play_sound(loss_sfx); st.error("TIGER WINS!")

    if col_t.button("🐯 Tiger"):
        st.info("Card Shuffling...")
        time.sleep(2)
        if dt_win == "Tiger":
            play_sound(win_sfx)
            st.success("TIGER WINS!"); st.balloons()
        else:
            play_sound(loss_sfx); st.error("DRAGON WINS!")

# --- FOOTER ---
st.divider()
st.markdown("<h4 style='text-align:center;'>💎 REAL CASINO - THE GOLD STANDARD 💎</h4>", unsafe_allow_html=True)
