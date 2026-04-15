import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP Casino Master", page_icon="🎰", layout="wide")

if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'balance' not in st.session_state: st.session_state.balance = 5000

# --- PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-container {
        background: white; color: black; width: 100px; height: 150px;
        border-radius: 10px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 3px solid #ffd700;
        margin: 5px; box-shadow: 0px 0px 10px #ffd700;
    }
    .card-num { font-size: 35px; font-weight: bold; }
    .red { color: #ff0000 !important; }
    .black { color: #000000 !important; }
    .fancy-box { background: #1e2130; padding: 10px; border-radius: 5px; margin: 5px; border: 1px solid #ffd700; }
    </style>
""", unsafe_allow_html=True)

# Helper: Card System
def get_card():
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    n, (s, c) = random.choice(nums), random.choice(suits)
    return n, s, c

def draw_card(n, s, c):
    st.markdown(f'<div class="card-container"><div class="card-num {c}">{n}</div><div style="font-size:30px" class="{c}">{s}</div></div>', unsafe_allow_html=True)

# --- ACCESS CONTROL ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 Welcome to Real Casino</h1>", unsafe_allow_html=True)
    st.divider()
    st.subheader("🔑 Admin Direct Access")
    key = st.text_input("Enter Secret Key", type="password")
    if st.button("Unlock All Games"):
        if key == "Akbar786":
            st.session_state.is_admin = True
            st.rerun()
        else: st.error("Wrong Key!")
else:
    # --- MAIN PANEL ---
    st.sidebar.title("👑 VIP PANEL")
    st.sidebar.write(f"💰 Balance: PKR {st.session_state.balance}")
    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🔄 Andar Bahar", "🐯 Dragon vs Tiger", "🃏 Teen Patti", "🎨 Color", "💳 Wallet"])

    # 1. CRICKET (With Full Fancy 6-50 Over)
    with tabs[0]:
        st.header("🏏 Cricket Exchange & Fancy")
        st.info("PAK vs IND - Live Market")
        c1, c2 = st.columns(2)
        c1.button("1.80 (Back)", use_container_width=True)
        c2.button("1.82 (Lay)", use_container_width=True)
        
        st.subheader("📊 Fancy Market (Yes/No)")
        fancies = ["6 Over Session", "10 Over Session", "15 Over Session", "20 Over Session", "35 Over Session", "50 Over Session"]
        for f in fancies:
            col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
            col_f1.markdown(f"<div class='fancy-box'>{f}</div>", unsafe_allow_html=True)
            col_f2.button(f"No", key=f+"no", use_container_width=True)
            col_f3.button(f"Yes", key=f+"yes", use_container_width=True)

    # 2. AVIATOR
    with tabs[1]:
        st.header("🚀 Aviator")
        if st.button("Start Flight"):
            crash = round(random.uniform(1.1, 2.5), 2)
            m = 1.00
            p = st.empty()
            while m < crash:
                p.markdown(f"<h1 style='text-align:center;'>{m:.2f}x</h1>", unsafe_allow_html=True)
                time.sleep(0.1); m += 0.04
            st.error(f"💥 CRASHED @ {m:.2f}x")

    # 3. ANDAR BAHAR
    with tabs[2]:
        st.header("🔄 Andar Bahar")
        j_slot = st.empty()
        if st.button("Start AB Game"):
            jn, js, jc = get_card()
            with j_slot: draw_card(jn, js, jc)
            with st.spinner("Dealing cards..."):
                time.sleep(10)
                st.success("Result: ANDAR wins!")

    # 4. DRAGON VS TIGER
    with tabs[3]:
        st.header("🐯 Dragon vs Tiger")
        st.number_input("Dragon Bet", value=100)
        st.number_input("Tiger Bet", value=500)
        if st.button("Reveal Result"):
            with st.spinner("Revealing..."):
                time.sleep(5)
                draw_card(*get_card()); draw_card(*get_card())

    # 5. TEEN PATTI
    with tabs[4]:
        st.header("🃏 Teen Patti")
        if st.button("Deal Player Hands"):
            with st.spinner("Shuffling..."):
                time.sleep(5)
                st.write("Player A:")
                draw_card(*get_card()); draw_card(*get_card()); draw_card(*get_card())
                st.write("Player B:")
                draw_card(*get_card()); draw_card(*get_card()); draw_card(*get_card())

    # 6. COLOR GAME
    with tabs[5]:
        st.header("🎨 Color Prediction")
        st.radio("Pick Color", ["🔴 Red", "🟢 Green", "🟣 Violet"], horizontal=True)
        if st.button("Bet on Color"):
            time.sleep(2)
            st.success("Winning Color: Red 🔴")

    # 7. WALLET
    with tabs[6]:
        st.header("💳 Wallet")
        st.selectbox("Action", ["Deposit", "Withdraw"])
        st.text_input("Amount")
        st.text_input("TID Number")
        st.button("Submit")

st.markdown("<br><div style='text-align:center; border-top:1px solid gold;'>👑 Admin By Casino VIP © 2026</div>", unsafe_allow_html=True)
