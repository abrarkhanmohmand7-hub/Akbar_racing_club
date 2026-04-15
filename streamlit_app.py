import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="Real Casino VIP", page_icon="🎰", layout="wide")

# --- INITIALIZE SESSION STATES ---
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'balance' not in st.session_state: st.session_state.balance = 500
if 'history' not in st.session_state: st.session_state.history = []

# --- PREMIUM CSS (Cards, Wallet & Theme) ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-container {
        background: white; color: black; width: 130px; height: 190px;
        border-radius: 12px; display: flex; flex-direction: column;
        justify-content: center; align-items: center; border: 4px solid #ffd700;
        box-shadow: 0px 0px 20px #ffd700; margin: auto; font-family: Arial;
    }
    .card-num { font-size: 55px; font-weight: bold; line-height: 1; }
    .card-suit { font-size: 45px; }
    .red { color: #ff0000; }
    .black { color: #000000; }
    .stTabs [data-baseweb="tab"] { color: #ffd700; font-weight: bold; font-size: 18px; }
    .wallet-box { background: #1e2130; padding: 15px; border-radius: 10px; border-left: 5px solid #ffd700; }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def get_card():
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    n, (s, c) = random.choice(nums), random.choice(suits)
    return n, s, c

def draw_card(n, s, c):
    st.markdown(f'<div class="card-container"><div class="card-num {c}">{n}</div><div class="card-suit {c}">{s}</div></div>', unsafe_allow_html=True)

# --- LOGIN SCREEN ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 Welcome to Real Casino</h1>", unsafe_allow_html=True)
    with st.sidebar:
        st.subheader("🛠 Admin Bypass")
        key = st.text_input("Secret Key", type="password")
        if st.button("Enter Directly"):
            if key == "Akbar786":
                st.session_state.is_admin = True
                st.rerun()
    st.tabs(["Login", "Sign Up"])
    st.info("Please login to access all games.")

else:
    # --- ADMIN DASHBOARD ---
    st.sidebar.title("👤 AKBAR KHAN")
    st.sidebar.markdown(f"<div class='wallet-box'>💰 Balance: <b>PKR {st.session_state.balance}</b></div>", unsafe_allow_html=True)
    
    # Wallet Section (Deposit/Withdraw with TID)
    with st.sidebar.expander("💳 Deposit & Withdrawal"):
        mode = st.selectbox("Action", ["Deposit", "Withdraw"])
        amt = st.number_input("Amount", min_value=500, step=500)
        method = st.selectbox("Method", ["EasyPaisa", "JazzCash", "Bank Transfer"])
        if mode == "Deposit":
            st.code("Send to: 03XX-XXXXXXX", language=None)
            tid = st.text_input("Transaction ID (TID)")
        if st.button("Submit Request"):
            if mode == "Deposit" and not tid: st.error("TID is required!")
            else:
                st.success("Request Sent!")
                st.session_state.history.append(f"{mode}: {amt} ({method})")

    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    # --- MAIN GAMES TABS ---
    tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🔄 Andar Bahar", "🐯 Dragon vs Tiger", "🃏 Teen Patti", "🎨 Color"])

    # 1. CRICKET (Back, Lay, Fancy)
    with tabs[0]:
        st.header("🏏 Cricket Exchange")
        c1, c2, c3 = st.columns([3, 1, 1])
        c1.subheader("Pakistan vs India")
        if c2.button("1.80 \n Back", key="b1"): st.info("Bet placed on Back")
        if c3.button("1.82 \n Lay", key="l1"): st.info("Bet placed on Lay")
        st.divider()
        st.write("### Fancy Market")
        f1, f2 = st.columns(2)
        f1.button("48 (No)", key="no1", use_container_width=True)
        f2.button("50 (Yes)", key="yes1", use_container_width=True)

    # 2. AVIATOR
    with tabs[1]:
        st.header("🚀 Aviator")
        if st.button("🚀 Start Flight"):
            crash = round(random.uniform(1.1, 1.8), 2) if random.random() < 0.8 else 4.2
            m = 1.00
            p = st.empty()
            while m < crash:
                p.markdown(f"<h1 style='text-align:center; font-size:80px;'>{m:.2f}x</h1>", unsafe_allow_html=True)
                time.sleep(0.1); m += 0.04
            st.error(f"💥 CRASHED @ {m:.2f}x")

    # 3. ANDAR BAHAR (Real Card Reveal)
    with tabs[2]:
        st.header("🔄 Andar Bahar")
        j_slot = st.empty()
        if st.button("Deal Joker & Play (20s)"):
            n, s, c = get_card()
            with j_slot: draw_card(n, s, c)
            with st.spinner("Dealing..."):
                time.sleep(17)
                st.success("Result: ANDAR Wins!")

    # 4. DRAGON VS TIGER (Real Card Reveal)
    with tabs[3]:
        st.header("🐯 Dragon vs Tiger")
        d_m = st.number_input("Dragon Bets", value=100)
        t_m = st.number_input("Tiger Bets", value=500)
        col_d, col_t = st.columns(2)
        if st.button("Open Cards (20s)"):
            winner = "Dragon" if d_m <= t_m else "Tiger"
            with st.spinner("Scanning..."):
                time.sleep(18)
                n1, s1, c1 = get_card()
                n2, s2, c2 = get_card()
                with col_d: draw_card(n1, s1, c1)
                with col_t: draw_card(n2, s2, c2)
                st.success(f"WINNER: {winner}")

    # 5. TEEN PATTI
    with tabs[4]:
        st.header("🃏 Teen Patti")
        if st.button("Deal Player Hands"):
            with st.spinner("Shuffling..."):
                time.sleep(5)
                c1, c2, c3 = st.columns(3)
                with c1: draw_card(*get_card())
                with c2: draw_card(*get_card())
                with c3: draw_card(*get_card())

    # 6. COLOR PREDICTION
    with tabs[5]:
        st.header("🎨 Color Prediction")
        st.selectbox("Select Period", ["1 Min", "3 Min", "5 Min"])
        st.radio("Choose Color", ["🔴 Red", "🟢 Green", "🟣 Violet"], horizontal=True)
        st.button("Place Color Bet")

st.divider()
st.caption("© 2026 Real Casino | Admin: Akbar Khan | All Systems Active")
