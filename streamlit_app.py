import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP Live Exchange", page_icon="🏏", layout="wide")

# --- LIVE AUTO-REFRESH ENGINE ---
# Ye line har 5 second baad page ko khud refresh karegi taake rates badalte rahen
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Har 5 second baad auto-refresh (Live feel ke liye)
st.empty() 

if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'balance' not in st.session_state: st.session_state.balance = 5000

# --- PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .rate-card { background: #1e2130; padding: 12px; border-radius: 8px; border: 1px solid #333; margin-bottom: 10px; }
    .back-btn { background-color: #72bbef; color: black; font-weight: bold; border-radius: 4px; padding: 10px; text-align: center; border: 1px solid white; box-shadow: 0px 2px 5px rgba(0,0,0,0.5); }
    .lay-btn { background-color: #faa9ba; color: black; font-weight: bold; border-radius: 4px; padding: 10px; text-align: center; border: 1px solid white; box-shadow: 0px 2px 5px rgba(0,0,0,0.5); }
    .rate-val { font-size: 20px; display: block; line-height: 1; }
    .rate-label { font-size: 10px; display: block; font-weight: normal; }
    .card-container { background: white; color: black; width: 100px; height: 150px; border-radius: 10px; display: inline-flex; flex-direction: column; justify-content: center; align-items: center; border: 3px solid #ffd700; margin: 5px; }
    .footer { text-align: center; color: #ffd700; font-size: 20px; font-weight: bold; margin-top: 50px; border-top: 2px solid #ffd700; padding-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Helper Functions
def get_live_rate(base):
    # Thori si random tabdeeli taake rate live lagay
    change = random.uniform(-0.03, 0.03)
    return round(base + change, 2)

def draw_card(n, s, c):
    st.markdown(f'<div class="card-container"><div style="font-size:35px; font-weight:bold;">{n}</div><div style="font-size:30px;" class="{c}">{s}</div></div>', unsafe_allow_html=True)

# --- ACCESS CONTROL ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 VIP LIVE EXCHANGE</h1>", unsafe_allow_html=True)
    st.divider()
    key = st.text_input("Enter Secret Key", type="password")
    if st.button("Unlock Live Markets"):
        if key == "Akbar786": st.session_state.is_admin = True; st.rerun()
else:
    # --- ADMIN DASHBOARD ---
    st.sidebar.title("👑 VIP ACCESS")
    st.sidebar.write(f"💰 Balance: PKR {st.session_state.balance}")
    if st.sidebar.button("Logout"): st.session_state.is_admin = False; st.rerun()

    tabs = st.tabs(["🏏 Cricket Live", "🚀 Aviator", "🔄 Casino Games", "💳 Wallet"])

    # 1. CRICKET (With Auto-Changing Rates)
    with tabs[0]:
        st.header("🏏 Live Markets (Auto-Update)")
        match_tabs = st.tabs(["🏆 PSL 2026", "🇮🇳 IPL"])
        
        with match_tabs[0]:
            # Live Match Data
            matches = [("Peshawar Zalmi", 1.85), ("Lahore Qalandars", 1.87)]
            for team, base_rate in matches:
                live_rate = get_live_rate(base_rate)
                st.markdown(f"<div class='rate-card'><b>{team}</b>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([3, 1, 1])
                c1.write("Match Winner (In-Play)")
                
                # Live Buttons with Rates
                c2.markdown(f"<div class='back-btn'><span class='rate-val'>{live_rate}</span><span class='rate-label'>BACK</span></div>", unsafe_allow_html=True)
                c3.markdown(f"<div class='lay-btn'><span class='rate-val'>{round(live_rate + 0.02, 2)}</span><span class='rate-label'>LAY</span></div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            # Fancy 6-50 Over
            with st.expander("📊 All Fancy Markets"):
                for over in ["6 Over", "10 Over", "20 Over", "50 Over"]:
                    fc1, fc2, fc3 = st.columns([2, 1, 1])
                    fc1.write(f"**{over} Session**")
                    val = random.randint(48, 290)
                    fc2.button(f"{val}\nNO", key=over+"n")
                    fc3.button(f"{val+2}\nYES", key=over+"y")

    # 2. CASINO (With Real Cards)
    with tabs[2]:
        st.header("🔄 Live Casino")
        if st.button("Deal Dragon vs Tiger"):
            with st.spinner("Dealing..."):
                time.sleep(3)
                c_a, c_b = st.columns(2)
                # Random cards
                with c_a: st.write("Dragon:"); draw_card("K", "♠️", "black")
                with c_b: st.write("Tiger:"); draw_card("7", "♥️", "red")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        👑 Admin by Akbar khan 👑<br>
        <span style="font-size: 14px; opacity: 0.8;">Live Market Engine Active • © 2026</span>
    </div>
""", unsafe_allow_html=True)

# Auto-Refresh Script (Last Line)
time.sleep(5)
st.rerun()
