import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="Real Casino - VIP Panel", page_icon="🎰", layout="wide")

# --- INITIALIZE DATABASE ---
if 'users' not in st.session_state: st.session_state.users = {}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'bets' not in st.session_state: st.session_state.bets = {"Andar": 0, "Bahar": 0, "Dragon": 0, "Tiger": 0}

# --- LOGIN / SIGNUP SYSTEM ---
def login_page():
    st.title("🎰 Welcome to Real Casino")
    choice = st.radio("Login or Create Account", ["Login", "Sign Up"], horizontal=True)
    
    u_name = st.text_input("Username")
    u_pass = st.text_input("Password", type="password")
    
    if choice == "Sign Up":
        if st.button("Create Account"):
            if u_name and u_pass:
                st.session_state.users[u_name] = {"pass": u_pass, "balance": 0, "history": []}
                st.success("Account Created! Now Login.")
            else: st.error("Please fill all fields")
            
    else:
        if st.button("Login"):
            if u_name in st.session_state.users and st.session_state.users[u_name]["pass"] == u_pass:
                st.session_state.logged_in_user = u_name
                st.rerun()
            else: st.error("Invalid Username or Password")

# --- MAIN APP LOGIC ---
if st.session_state.logged_in_user is None:
    login_page()
else:
    user = st.session_state.logged_in_user
    data = st.session_state.users[user]

    # --- SIDEBAR: WALLET & ACTIONS ---
    st.sidebar.title(f"👤 {user}")
    st.sidebar.metric("💰 Current Balance", f"PKR {data['balance']}")
    
    with st.sidebar.expander("💸 Deposit / Withdraw"):
        mode = st.radio("Action", ["Deposit", "Withdraw"])
        amount = st.number_input("Amount", min_value=100)
        if st.button("Submit Request"):
            st.success(f"{mode} request sent to Admin!")
            data['history'].append(f"{mode}: {amount} PKR (Pending)")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in_user = None
        st.rerun()

    # --- THE AUTO-WINNER LOGIC ---
    def get_auto_winner(side_a, side_b, name_a, name_b):
        if st.session_state.bets[side_a] == st.session_state.bets[side_b]:
            return random.choice([name_a, name_b])
        return name_a if st.session_state.bets[side_a] < st.session_state.bets[side_b] else name_b

    # --- GAMES INTERFACE ---
    tabs = st.tabs(["🏏 Cricket", "🚀 Aviator", "🔄 Andar Bahar", "🐯 Dragon vs Tiger"])

    # --- ANDAR BAHAR (Example with Auto-Logic) ---
    with tabs[2]:
        st.header("🔄 Andar Bahar - Smart Table")
        bet_amt = st.number_input("Bet Amount", min_value=100, step=100, key="ab_val")
        
        c1, c2 = st.columns(2)
        if c1.button("Bet ANDAR"):
            if data['balance'] >= bet_amt:
                st.session_state.bets["Andar"] += bet_amt
                data['balance'] -= bet_amt
                st.info("Bet Placed on Andar")
            else: st.error("Insufficient Balance")
            
        if c2.button("Bet BAHAR"):
            if data['balance'] >= bet_amt:
                st.session_state.bets["Bahar"] += bet_amt
                data['balance'] -= bet_amt
                st.info("Bet Placed on Bahar")
            else: st.error("Insufficient Balance")

        if st.button("🔴 START GAME (20s Reveal)"):
            winner = get_auto_winner("Andar", "Bahar", "Andar", "Bahar")
            slot = st.empty()
            for i in range(12): # Animation
                slot.markdown(f"<h1 style='text-align:center;'>{random.choice(['♠️','♥️','♣️','♦️'])}</h1>", unsafe_allow_html=True)
                time.sleep(1.5)
            
            slot.markdown(f"<h1 style='text-align:center; color:gold;'>🃏 RESULT: {winner}</h1>", unsafe_allow_html=True)
            # Reset bets for next round
            st.session_state.bets["Andar"] = 0
            st.session_state.bets["Bahar"] = 0

    # --- AVIATOR (Example) ---
    with tabs[1]:
        st.subheader("🚀 Aviator")
        if st.button("🚀 TAKE OFF"):
            crash = round(random.uniform(1.1, 1.5), 2) if random.random() < 0.9 else round(random.uniform(2.0, 5.0), 2)
            m = 1.00
            p = st.empty()
            while m < crash:
                p.markdown(f"<h1 style='text-align:center;'>{m:.2f}x ✈️</h1>", unsafe_allow_html=True)
                time.sleep(0.1); m += 0.05
            p.error(f"💥 CRASHED AT {m:.2f}x")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Real Casino | Secured by Akbar Khan")
