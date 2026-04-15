import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP Casino Panel", page_icon="🎰", layout="wide")

# --- SESSION STATE ---
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'balance' not in st.session_state: st.session_state.balance = 1000

# --- PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-container {
        background: white; color: black; width: 130px; height: 190px;
        border-radius: 12px; display: flex; flex-direction: column;
        justify-content: center; align-items: center; border: 4px solid #ffd700;
        box-shadow: 0px 0px 20px #ffd700; margin: auto;
    }
    .card-num { font-size: 55px; font-weight: bold; color: black; line-height: 1; }
    .card-suit { font-size: 45px; }
    .red { color: #ff0000 !important; }
    .black { color: #000000 !important; }
    .main-footer {
        text-align: center; color: #ffd700; font-size: 18px; 
        font-weight: bold; margin-top: 60px; border-top: 2px solid #ffd700; padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Card Logic
def get_card():
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    n, (s, c) = random.choice(nums), random.choice(suits)
    return n, s, c

def draw_card(n, s, c):
    st.markdown(f'<div class="card-container"><div class="card-num {c}">{n}</div><div class="card-suit {c}">{s}</div></div>', unsafe_allow_html=True)

# --- LOGIN / ACCESS ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 Welcome to Real Casino</h1>", unsafe_allow_html=True)
    
    st.sidebar.header("🔑 Admin Access")
    key = st.sidebar.text_input("Secret Key", type="password")
    if st.sidebar.button("Unlock Panel"):
        if key == "Akbar786":
            st.session_state.is_admin = True
            st.rerun()
        else:
            st.sidebar.error("Access Denied!")

    st.tabs(["Login", "Sign Up"])
    st.info("Enter Admin Key in sidebar to open all games.")

else:
    # --- ADMIN DASHBOARD ---
    st.sidebar.title("👑 Admin Panel")
    st.sidebar.markdown(f"💰 **Wallet:** PKR {st.session_state.balance}")
    
    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    # ALL GAMES TABS
    tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🔄 Andar Bahar", "🐯 Dragon vs Tiger", "🃏 Teen Patti", "💳 Wallet"])

    # 1. CRICKET
    with tabs[0]:
        st.header("🏏 Cricket Exchange")
        st.info("Live Markets Active")
        c1, c2 = st.columns(2)
        c1.button("1.80 (Back)", use_container_width=True, key="cr_b")
        c2.button("1.82 (Lay)", use_container_width=True, key="cr_l")
        st.divider()
        st.subheader("Fancy")
        st.columns(2)[0].button("No", key="f_n")
        st.columns(2)[1].button("Yes", key="f_y")

    # 2. AVIATOR
    with tabs[1]:
        st.header("🚀 Aviator")
        if st.button("Start Flight"):
            crash = round(random.uniform(1.1, 1.4), 2)
            m = 1.00
            p = st.empty()
            while m < crash:
                p.markdown(f"<h1 style='text-align:center;'>{m:.2f}x</h1>", unsafe_allow_html=True)
                time.sleep(0.1); m += 0.05
            st.error(f"💥 CRASHED @ {m:.2f}x")

    # 3. DRAGON VS TIGER
    with tabs[3]:
        st.header("🐯 Dragon vs Tiger")
        d_m = st.number_input("Dragon Bets", value=100)
        t_m = st.number_input("Tiger Bets", value=800)
        col_d, col_t = st.columns(2)
        if st.button("Deal Cards"):
            winner = "Dragon" if d_m <= t_m else "Tiger"
            with st.spinner("Revealing..."):
                time.sleep(17)
                n1, s1, c1 = get_card(); n2, s2, c2 = get_card()
                with col_d: draw_card(n1, s1, c1)
                time.sleep(1.5)
                with col_t: draw_card(n2, s2, c2)
                st.success(f"WINNER: {winner}")

    # 4. WALLET
    with tabs[5]:
        st.header("💳 Deposit / Withdraw")
        mode = st.selectbox("Action", ["Deposit", "Withdraw"])
        st.number_input("Amount (PKR)", min_value=500)
        if mode == "Deposit":
            st.text_input("Transaction ID (TID)")
        if st.button("Submit Request"):
            st.success("Request sent to Admin")

# --- FOOTER ---
st.markdown("""
    <div class="main-footer">
        👑 Admin By Casino VIP 👑<br>
        <span style="font-size: 14px; opacity: 0.8;">Verified System © 2026</span>
    </div>
""", unsafe_allow_html=True)
