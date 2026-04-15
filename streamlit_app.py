import streamlit as st
import time
import random

# 1. Page Config (Mobile Friendly)
st.set_page_config(page_title="Y999 Exchange", page_icon="🟢", layout="wide")

# --- CUSTOM CSS (Neon Green & Black Theme) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background: #0b0e11; color: #ffffff; }
    
    /* Top Header Bar */
    .top-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px; background: #1a1d23; border-bottom: 2px solid #39ff14;
        position: sticky; top: 0; z-index: 100;
    }
    .balance-box { background: #2c313c; padding: 5px 15px; border-radius: 20px; color: #ffd700; font-weight: bold; }
    .deposit-btn { background: #39ff14; color: black; padding: 5px 15px; border-radius: 5px; font-weight: bold; }

    /* Game Cards Styling */
    .game-card {
        background: #1a1d23; border-radius: 12px; border: 1px solid #333;
        padding: 5px; text-align: center; transition: 0.3s; margin-bottom: 15px;
    }
    .game-card:hover { border-color: #39ff14; box-shadow: 0px 0px 10px #39ff14; }
    .game-img { width: 100%; border-radius: 8px; margin-bottom: 5px; }
    .game-title { font-size: 12px; font-weight: bold; color: #ddd; }

    /* Category Headers */
    .cat-header {
        display: flex; align-items: center; gap: 10px;
        font-size: 18px; font-weight: bold; margin: 20px 0 10px 0; color: #39ff14;
    }

    /* Bottom Navigation */
    .nav-bar {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #1a1d23; display: flex; justify-content: space-around;
        padding: 10px; border-top: 1px solid #333; z-index: 1000;
    }
    .nav-item { text-align: center; color: #888; font-size: 12px; }
    .nav-item.active { color: #39ff14; }

    /* Card Graphics */
    .playing-card {
        background: white; color: black; width: 80px; height: 110px;
        border-radius: 8px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 2px solid #ffd700;
        font-weight: bold; font-size: 25px; margin: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.markdown("""
    <div class="top-bar">
        <div style="font-size: 24px; font-weight: bold; color: #39ff14;">Y999</div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <div class="balance-box">Rs 0.00 🔄</div>
            <div class="deposit-btn">Deposit</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state: st.session_state.page = 'Home'

# --- CONTENT ---
if st.session_state.page == 'Home':
    # 1. LIVE SECTION
    st.markdown('<div class="cat-header">👤 Live</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="game-card"><img src="https://img.freepik.com/free-vector/casino-glitter-banner_1017-14361.jpg" class="game-img"><div class="game-title">EVO Live</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="game-card"><img src="https://img.freepik.com/free-photo/beauty-portrait-woman-with-clean-fresh-skin_1150-13781.jpg" class="game-img"><div class="game-title">SEXY Live</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="game-card"><img src="https://img.freepik.com/free-photo/gorgeous-woman-celebrating-with-confetti_23-2148416301.jpg" class="game-img"><div class="game-title">PP Live</div></div>', unsafe_allow_html=True)

    # 2. SPORTS SECTION (All Leagues)
    st.markdown('<div class="cat-header">⚽ Sports</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        if st.button("9Wickets"): st.session_state.page = 'Cricket'
        st.markdown('<div class="game-card"><div class="game-title">9Wickets Sports</div></div>', unsafe_allow_html=True)
    with s2: st.markdown('<div class="game-card"><div class="game-title">SABA Sports</div></div>', unsafe_allow_html=True)
    with s3: st.markdown('<div class="game-card"><div class="game-title">WG Sports</div></div>', unsafe_allow_html=True)

    # 3. CARDS & SLOTS
    st.markdown('<div class="cat-header">🃏 Cards & Slots</div>', unsafe_allow_html=True)
    cl1, cl2, cl3 = st.columns(3)
    with cl1: 
        if st.button("Teen Patti"): st.session_state.page = 'Casino'
        st.markdown('<div class="game-title">JILI Cards</div>', unsafe_allow_html=True)
    with cl2: st.markdown('<div class="game-title">Aviator</div>', unsafe_allow_html=True)
    with cl3: st.markdown('<div class="game-title">Dragon Tiger</div>', unsafe_allow_html=True)

elif st.session_state.page == 'Cricket':
    st.header("🏏 Live Cricket Exchange")
    st.info("Market: PSL 2026 - Peshawar vs Lahore")
    rate = round(random.uniform(1.80, 1.90), 2)
    col1, col2, col3 = st.columns([2,1,1])
    col1.write("### Match Odds")
    col2.button(f"{rate}\nBACK")
    col3.button(f"{rate+0.02}\nLAY")
    
    st.subheader("📊 Fancy (6-20 Over)")
    for f in ["6 Over", "10 Over", "20 Over"]:
        r1, r2, r3 = st.columns([2,1,1])
        r1.write(f)
        r2.button("NO", key=f+"n")
        r3.button("YES", key=f+"y")
    if st.button("Back to Home"): st.session_state.page = 'Home'; st.rerun()

elif st.session_state.page == 'Casino':
    st.header("🃏 Live Casino Round")
    if st.button("Deal Real Cards"):
        c1, c2, c3 = st.columns(3)
        nums = ["A", "K", "Q", "J", "10"]
        suits = [("♥️","red"), ("♠️","black")]
        for c in [c1, c2, c3]:
            n = random.choice(nums)
            s, color = random.choice(suits)
            with c: st.markdown(f'<div class="playing-card" style="color:{color}">{n}<br>{s}</div>', unsafe_allow_html=True)
    
    # Logic: Jis side pe kam paise lagein wo win karey
    st.warning("Admin Logic: Side with MINIMUM bets will win automatically.")
    if st.button("Back to Home"): st.session_state.page = 'Home'; st.rerun()

# --- BOTTOM NAVIGATION ---
st.markdown("""
    <div class="nav-bar">
        <div class="nav-item active">🏠<br>Home</div>
        <div class="nav-item">🎁<br>Offers</div>
        <div class="nav-item">👥<br>Invite</div>
        <div class="nav-item">🎧<br>Support</div>
        <div class="nav-item">👤<br>Profile</div>
    </div>
""", unsafe_allow_html=True)

# Footer Branding
st.markdown(f"<div style='text-align:center; padding: 50px; color: #39ff14;'>👑 Admin by Akbar khan 👑<br>Verified Exchange © 2026</div>", unsafe_allow_html=True)
