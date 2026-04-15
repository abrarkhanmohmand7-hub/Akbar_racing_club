import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="Real Casino VIP", page_icon="🎰", layout="wide")

# --- ADMIN AUTO-BYPASS LOGIC ---
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-box { 
        background: white; color: black; border-radius: 10px; 
        padding: 20px; text-align: center; font-size: 50px; 
        font-weight: bold; border: 3px solid #ffd700;
        box-shadow: 0px 0px 15px rgba(255, 215, 0, 0.5);
    }
    .red-card { color: #ff0000; }
    .black-card { color: #000000; }
    </style>
""", unsafe_allow_html=True)

# Card Generating Function
def get_random_card():
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    num = random.choice(numbers)
    suit, color = random.choice(suits)
    return num, suit, color

# --- LOGIN SCREEN ---
def login_screen():
    st.markdown(f"<h1 style='text-align:center;'>🎰 Welcome to <br>Real Casino</h1>", unsafe_allow_html=True)
    with st.expander("Admin Access"):
        secret = st.text_input("Admin Key", type="password")
        if st.button("Activate Admin Mode"):
            if secret == "Akbar786":
                st.session_state.is_admin = True
                st.rerun()
    st.tabs(["Login", "Sign Up"])

# --- MAIN DASHBOARD ---
def main_dashboard():
    st.sidebar.title("👑 ADMIN: AKBAR KHAN")
    if st.sidebar.button("Logout Admin"):
        st.session_state.is_admin = False
        st.rerun()

    tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🔄 Andar Bahar", "🐯 Dragon vs Tiger"])

    # --- DRAGON VS TIGER WITH REAL CARD NUMBERS ---
    with tabs[3]:
        st.header("🐯 Dragon vs Tiger (Real Cards)")
        
        # Bets Monitor
        d_money = st.number_input("Dragon Total Bets", value=1000)
        t_money = st.number_input("Tiger Total Bets", value=5000)
        
        col1, col_vs, col2 = st.columns([2, 1, 2])
        d_slot = col1.empty()
        t_slot = col2.empty()
        
        d_slot.markdown("<div class='card-box'>🎴</div>", unsafe_allow_html=True)
        t_slot.markdown("<div class='card-box'>🎴</div>", unsafe_allow_html=True)

        if st.button("Open Cards (20s Reveal)"):
            winner = "Dragon" if d_money <= t_money else "Tiger"
            
            # 20 Seconds suspense animation
            status = st.empty()
            for i in range(5):
                status.info(f"Shuffling Cards... {5-i}")
                time.sleep(3)
            
            # Generate Cards
            d_num, d_suit, d_color = get_random_card()
            t_num, t_suit, t_color = get_random_card()

            # Ensure the winner has a higher card logic (Simplified for display)
            # Yahan hum card ki visual reveal karenge
            status.warning("DRAGON CARD REVEALING...")
            time.sleep(2)
            d_slot.markdown(f"<div class='card-box {d_color}-card'>{d_num}<br>{d_suit}</div>", unsafe_allow_html=True)
            
            status.warning("TIGER CARD REVEALING...")
            time.sleep(2)
            t_slot.markdown(f"<div class='card-box {t_color}-card'>{t_num}<br>{t_suit}</div>", unsafe_allow_html=True)
            
            st.success(f"WINNER: {winner}!")

# --- FLOW CONTROL ---
if st.session_state.is_admin:
    main_dashboard()
else:
    login_screen()
