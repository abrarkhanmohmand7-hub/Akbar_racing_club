import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP LIVE EXCHANGE", page_icon="🎰", layout="wide")

# --- SESSION STATE ---
if 'is_admin' not in st.session_state: 
    st.session_state.is_admin = False

# --- PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-box {
        background: white; color: black; width: 90px; height: 130px;
        border-radius: 8px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 2px solid #ffd700;
        box-shadow: 0px 0px 10px #ffd700; margin: 5px;
    }
    .card-num { font-size: 35px; font-weight: bold; line-height: 1; color: black; }
    .card-suit { font-size: 30px; }
    .red { color: #ff0000 !important; }
    .black { color: #000000 !important; }
    .back-btn { background-color: #72bbef; color: black !important; font-weight: bold; padding: 10px; text-align: center; border-radius: 4px; border: 1px solid white; }
    .lay-btn { background-color: #faa9ba; color: black !important; font-weight: bold; padding: 10px; text-align: center; border-radius: 4px; border: 1px solid white; }
    .fancy-row { background: #1e2130; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #333; }
    .footer { text-align: center; color: #ffd700; font-size: 22px; font-weight: bold; margin-top: 40px; border-top: 2px solid #ffd700; padding-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Helper: Card Generator
def get_card():
    nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    n, (s, c) = random.choice(nums), random.choice(suits)
    return n, s, c

def draw_card(n, s, c):
    st.markdown(f'<div class="card-box"><div class="card-num">{n}</div><div class="card-suit {c}">{s}</div></div>', unsafe_allow_html=True)

# --- LOGIN ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 VIP LIVE EXCHANGE</h1>", unsafe_allow_html=True)
    st.divider()
    key = st.text_input("Enter Secret Key", type="password", key="login_key")
    if st.button("Unlock Dashboard"):
        if key == "Akbar786":
            st.session_state.is_admin = True
            st.rerun()
        else:
            st.error("Access Denied!")
else:
    # --- DASHBOARD ---
    st.sidebar.title("👑 VIP Panel")
    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    tabs = st.tabs(["🏏 Cricket Live", "🚀 Aviator", "🔄 Casino Games", "🎨 Color Game", "💳 Wallet"])

    # 1. CRICKET (6-20 Over Fancy & Live Rates)
    with tabs[0]:
        st.header("🏏 Live Cricket Exchange")
        l_tabs = st.tabs(["🇵🇰 PSL", "🇮🇳 IPL", "🌍 World Cup"])
        
        with l_tabs[0]:
            matches = [("Peshawar Zalmi", "Lahore Qalandars", 1.82), ("Karachi Kings", "Multan Sultans", 2.10)]
            for t1, t2, base_r in matches:
                st.markdown(f"### {t1} vs {t2} (LIVE)")
                live_r
