import streamlit as st
import time
import random

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Real Casino - Premium Gaming Hub",
    page_icon="🎰",
    layout="wide"
)

# --- SOUND & MUSIC SYSTEM ---
bg_music = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"
win_sfx = "https://www.myinstants.com/media/sounds/win-sound-effect.mp3"
loss_sfx = "https://www.myinstants.com/media/sounds/wrong-answer-126515.mp3"

def play_sound(url):
    st.markdown(f'<audio autoplay><source src="{url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# Background Music (Mute option sidebar mein hai)
st.markdown(f'<iframe src="{bg_music}" allow="autoplay" style="display:none"></iframe>', unsafe_allow_html=True)

# --- PREMIUM CASINO CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #1a0033 0%, #000000 100%); color: #ffd700; }
    .stTabs [data-baseweb="tab-list"] { background-color: rgba(255, 215, 0, 0.1); border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: #ffd700; font-weight: bold; font-size: 16px; }
    .stButton>button { border: 2px solid #ffd700; background-color: transparent; color: #ffd700; border-radius: 10px; width: 100%; transition: 0.3s; height: 3em; }
    .stButton>button:hover { background-color: #ffd700; color: black; box-shadow: 0px 0px 15px #ffd700; }
    .game-card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #ffd700; text-align: center; }
    /* Cricket Specific Colors */
    button[key^="back"] { background-color: #72bbef !important; color: black !important; }
    button[key^="lay"] { background-color: #faa9ba !important; color: black !important; }
    button[key^="yes"] { background-color: #28a745 !important; color: white !important; }
    button[key^="no"] { background-color: #dc3545 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: WALLET & ADMIN ---
st.sidebar.title("🎰 REAL CASINO")
st.sidebar.subheader("👤 Owner: Akbar Khan")
st.sidebar.divider()
st.sidebar.info("💳 Faysal Bank: 343931000002103")
up_ss = st.sidebar.file_uploader("Upload Deposit Screenshot", type=['jpg', 'png'])
if st.sidebar.button("Submit Payment"):
    st.sidebar.success("Payment Sent for Verification!")

# --- MAIN INTERFACE ---
st.title("🎰 REAL CASINO - THE GOLD STANDARD")

tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🎨 Color", "🃏 Teen Patti", "🔄 Andar Bahar", "🐯 Dragon vs Tiger"])

# --- TAB 1: CRICKET EXCHANGE ---
with tabs[0]:
    st.subheader("🏏 Cricket Live Exchange")
    league = st.selectbox("Tournament", ["PSL 2026", "IPL 2026", "World Cup", "BBL", "The Hundred"])
    cric_link = st.text_input("Admin: Live Link", "https://www.youtube.com/embed/live_stream_id")
    st.components.v1.iframe(cric_link, height=400)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("### Teams")
        st.info("Team A")
        st.info("Team B")
    with col2:
        st.write("🟦 BACK")
        st.button("1.80", key="back1")
        st.button("2.10", key="back2")
    with col3:
        st.write("🟥 LAY")
        st.button("1.82", key="lay1")
        st.button("2.12", key="lay2")
        
    st.divider()
    st.subheader("🔥 Fancy Market")
    f1, f2 = st.columns(2)
    with f1:
        st.write("6 Over Session (Team A)")
        c_n, c_y = st.columns(2)
        c_n.button("48 (No)", key="no1")
        c_y.button("50 (Yes)", key="yes1")

# --- TAB 2: AVIATOR (90% LOSS LOGIC + PLANE ANIMATION) ---
with tabs[1]:
    st.subheader("🚀 Aviator Live")
    av_c1, av_c2 = st.columns([2, 1])
    with av_c2:
        bet = st.number_input("Bet Amount", min_value=100, key="avbet")
        if st.button("🚀 TAKE OFF", key="avstart"):
            # 90% chance of crash below 1.8x
            crash = round(random.uniform(1.10, 1.80), 2) if random.random() < 0.90 else round(random.uniform(2.0, 5.0), 2)
            mult = 1.00
            p_hold = av_c1.empty()
            while mult < crash:
                p_hold.markdown(f"<div class='game-card'><h1 style='font-size:80px;'>{mult:.2f}x</h1><h2>✈️</h2></div>", unsafe_allow_html=True)
                time.sleep(0.1)
                mult += 0.04
            play_sound(loss_sfx)
            p_hold.markdown(f"<div class='game-card'><h1 style='color:red;'>💥 CRASHED @ {mult:.2f}x</h1></div>", unsafe_allow_html=True)

# --- TAB 3: COLOR PREDICTION ---
with tabs[2]:
    st.header("🎨 Color Prediction")
    with st.expander("🛠 Admin Control"):
        cp_winner = st.radio("Next Color:", ["Red", "Green", "Violet"])
    
    u_col = st.radio("Pick Color:", ["🔴 Red", "🟢 Green", "🟣 Violet"], horizontal=True)
    if st.button("Submit Prediction", key="cp_btn"):
        with st.spinner("Wait..."):
            time.sleep(2)
            if cp_winner in u_col:
                play_sound(win_sfx); st.success("WINNER!"); st.balloons()
            else:
                play_sound(loss_sfx); st.error(f"LOSS! Result: {cp_winner}")

# --- TAB 4: TEEN PATTI ---
with tabs[3]:
    st.header("🃏 Teen Patti")
    with st.expander("🛠 Admin Control"):
        tp_win = st.radio("Winner Hand:", ["Player A", "Player B"])
    
    t_a, t_b = st.columns(2)
    if t_a.button("Bet Player A", key="tpa"):
        time.sleep(1.5)
        if tp_win == "Player A": play_sound(win_sfx); st.success("WIN")
        else: play_sound(loss_sfx); st.error("LOSS")
    if t_b.button("Bet Player B", key="tpb"):
        time.sleep(1.5)
        if tp_win == "Player B": play_sound(win_sfx); st.success("WIN")
        else: play_sound(loss_sfx); st.error("LOSS")

# --- TAB 5: ANDAR BAHAR (SMART LOSS) ---
with tabs[4]:
    st.header("🔄 Andar Bahar")
    with st.expander("🛠 Admin Control (Bets)"):
        a_money = st.number_input("Andar Total Money", value=0)
        b_money = st.number_input("Bahar Total Money", value=0)
    
    ab_a, ab_b = st.columns(2)
    if ab_a.button("🅰️ ANDAR", key="aba"):
        res = "Bahar" if a_money > b_money else "Andar"
        time.sleep(2); st.write(f"Result: {res}")
        if res == "Andar": st.success("WIN")
        else: st.error("LOSS")
    if ab_b.button("🅱️ BAHAR", key="abb"):
        res = "Andar" if b_money > a_money else "Bahar"
        time.sleep(2); st.write(f"Result: {res}")
        if res == "Bahar": st.success("WIN")
        else: st.error("LOSS")

# --- TAB 6: DRAGON VS TIGER (SMART LOSS) ---
with tabs[5]:
    st.header("🐯 Dragon vs Tiger")
    with st.expander("🛠 Admin Control"):
        d_money = st.number_input("Dragon Bet", value=0)
        t_money = st.number_input("Tiger Bet", value=0)
    
    d_btn, t_btn = st.columns(2)
    if d_btn.button("🐉 Dragon", key="dbtn"):
        res = "Tiger" if d_money > t_money else "Dragon"
        time.sleep(1.5); st.write(f"Result: {res}")
        if res == "Dragon": st.success("WIN")
        else: st.error("LOSS")
    if t_btn.button("🐯 Tiger", key="tbtn"):
        res = "Dragon" if t_money > d_money else "Tiger"
        time.sleep(1.5); st.write(f"Result: {res}")
        if res == "Tiger": st.success("WIN")
        else: st.error("LOSS")

st.divider()
st.markdown("<p style='text-align:center;'>💎 REAL CASINO - SECURE & TRUSTED 💎</p>", unsafe_allow_html=True)
