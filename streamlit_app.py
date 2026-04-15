import streamlit as st
import time
import random

# 1. Page Config (Mobile Optimized)
st.set_page_config(page_title="Y999 VIP", page_icon="🟢", layout="wide")

# --- CUSTOM CSS (Professional Box Interface) ---
st.markdown("""
    <style>
    .stApp { background: #0b0e11; color: #ffffff; }
    
    /* Top Bar */
    .header-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 15px; background: #1a1d23; border-bottom: 2px solid #39ff14;
        position: sticky; top: 0; z-index: 999;
    }
    .balance-box { background: #2c313c; padding: 5px 12px; border-radius: 20px; color: #ffd700; font-weight: bold; border: 1px solid #444; font-size: 14px; }
    .deposit-btn { background: #39ff14; color: black; padding: 5px 15px; border-radius: 6px; font-weight: bold; font-size: 14px; }

    /* Game Category Styling */
    .cat-header { color: #39ff14; font-size: 18px; font-weight: bold; margin: 20px 0 10px 10px; display: flex; align-items: center; gap: 8px; }
    
    /* Individual Game Box */
    .game-container {
        background: #1a1d23; border-radius: 15px; border: 1px solid #333;
        overflow: hidden; text-align: center; transition: 0.3s;
        margin-bottom: 15px; position: relative;
    }
    .game-container:hover { border-color: #39ff14; box-shadow: 0px 0px 15px #39ff14; }
    .game-img-placeholder {
        width: 100%; height: 110px; background: linear-gradient(45deg, #1a1d23, #2c313c);
        display: flex; justify-content: center; align-items: center; font-size: 40px;
    }
    .game-label {
        background: rgba(0,0,0,0.7); color: #fff; padding: 5px;
        font-size: 12px; font-weight: bold; border-top: 1px solid #444;
    }

    /* Bottom Nav */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #1a1d23; display: flex; justify-content: space-around;
        padding: 12px 0; border-top: 1px solid #333; z-index: 999;
    }
    .nav-icon { text-align: center; color: #888; font-size: 12px; }
    .nav-icon.active { color: #39ff14; }

    /* Real Cards Styling */
    .playing-card {
        background: white; color: black; width: 80px; height: 115px;
        border-radius: 10px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 3px solid #ffd700;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.5); margin: 5px;
    }
    .card-val { font-size: 35px; font-weight: bold; line-height: 1; }
    .card-sym { font-size: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"

# --- HEADER ---
st.markdown(f"""
    <div class="header-bar">
        <div style="font-size: 22px; font-weight: bold; color: #39ff14;">Y999</div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <div class="balance-box">Rs 0.00 🔄</div>
            <div class="deposit-btn">Deposit</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- HELPER: Game Box UI ---
def game_box(name, icon, key):
    with st.container():
        st.markdown(f"""
            <div class="game-container">
                <div class="game-img-placeholder">{icon}</div>
                <div class="game-label">{name}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Play Now", key=key, use_container_width=True):
            if name == "9Wickets": st.session_state.page = "Cricket"
            elif name in ["JILI Cards", "Tiger"]: st.session_state.page = "Casino"
            st.rerun()

# --- PAGES ---

if st.session_state.page == "Home":
    # 1. LIVE SECTION
    st.markdown('<div class="cat-header">👤 Live Casino</div>', unsafe_allow_html=True)
    l1, l2, l3 = st.columns(3)
    with l1: game_box("EVO Live", "🎬", "evo")
    with l2: game_box("SEXY Live", "💃", "sexy")
    with l3: game_box("PP Live", "🃏", "pp")

    # 2. SPORTS SECTION
    st.markdown('<div class="cat-header">⚽ Sports</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1: game_box("9Wickets", "🏏", "9w")
    with s2: game_box("SABA Sports", "⚽", "saba")
    with s3: game_box("WG Sports", "🎾", "wg")

    # 3. CARDS & SLOTS
    st.markdown('<div class="cat-header">🃏 Cards & Slots</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: game_box("JILI Cards", "🎴", "jili")
    with c2: game_box("Aviator", "🚀", "avi")
    with c3: game_box("Tiger", "🐯", "tiger")

elif st.session_state.page == "Cricket":
    st.header("🏏 9Wickets Live")
    st.markdown("### Peshawar vs Lahore (In-Play)")
    rate = round(random.uniform(1.82, 1.88), 2)
    
    col_a, col_b = st.columns(2)
    col_a.info(f"BACK: {rate}")
    col_b.error(f"LAY: {round(rate+0.02, 2)}")
    
    st.subheader("📊 Live Fancy (6-20 Over Only)")
    for f in ["6 Over", "10 Over", "20 Over"]:
        st.write(f"**{f} Session**")
        v = random.randint(45, 170)
        c1, c2 = st.columns(2)
        c1.button(f"{v}\nNO", key=f+"n")
        c2.button(f"{v+2}\nYES", key=f+"y")
    
    if st.button("← Back"): st.session_state.page = "Home"; st.rerun()

elif st.session_state.page == "Casino":
    st.header("🃏 Live Table")
    st.warning("Admin Logic: Minimum Bet side will win automatically.")
    
    if st.button("Deal Real Cards"):
        time.sleep(1)
        res_cols = st.columns(3)
        cards = [("A","♥️","red"), ("K","♠️","black"), ("10","♦️","red"), ("Q","♣️","black"), ("J","♠️","black")]
        for i in range(3):
            val, sym, col = random.choice(cards)
            with res_cols[i]:
                st.markdown(f'<div class="playing-card" style="color:{col}"><div class="card-val">{val}</div><div class="card-sym">{sym}</div></div>', unsafe_allow_html=True)
        st.success("Result Generated!")

    if st.button("← Back"): st.session_state.page = "Home"; st.rerun()

# --- BOTTOM NAV ---
st.markdown("""
    <div class="bottom-nav">
        <div class="nav-icon active">🏠<br>Home</div>
        <div class="nav-icon">🎁<br>Offers</div>
        <div class="nav-icon">👥<br>Invite</div>
        <div class="nav-icon">🎧<br>Support</div>
        <div class="nav-icon">👤<br>Profile</div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br><br><div style='text-align:center; color:#39ff14; font-weight:bold;'>👑 Admin by Akbar khan 👑<br>© 2026 Verified System</div>", unsafe_allow_html=True)
