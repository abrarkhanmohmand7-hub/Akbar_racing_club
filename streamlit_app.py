import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP LIVE EXCHANGE", page_icon="🏏", layout="wide")

# --- SESSION STATE ---
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- PREMIUM CSS (Real Cards & Exchange UI) ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-box {
        background: white; color: black; width: 90px; height: 130px;
        border-radius: 8px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 2px solid #ffd700;
        box-shadow: 0px 0px 10px #ffd700; margin: 5px;
    }
    .card-num { font-size: 35px; font-weight: bold; line-height: 1; }
    .card-suit { font-size: 30px; }
    .red { color: #ff0000 !important; }
    .black { color: #000000 !important; }
    .back-btn { background-color: #72bbef; color: black; font-weight: bold; padding: 10px; text-align: center; border-radius: 4px; border: 1px solid white; }
    .lay-btn { background-color: #faa9ba; color: black; font-weight: bold; padding: 10px; text-align: center; border-radius: 4px; border: 1px solid white; }
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
    st.markdown(f'<div class="card-box"><div class="card-num {c}">{n}</div><div class="card-suit {c}">{s}</div></div>', unsafe_allow_html=True)

# --- LOGIN ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 VIP LIVE EXCHANGE</h1>", unsafe_allow_html=True)
    st.divider()
    key = st.text_input("Enter Secret Key", type="password")
    if st.button("Unlock Dashboard"):
        if key == "Akbar786":
            st.session_state.is_admin = True
            st.rerun()
else:
    # --- ADMIN DASHBOARD ---
    st.sidebar.title("👑 VIP Panel")
    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    tabs = st.tabs(["🏏 Cricket Live", "🚀 Aviator", "🔄 Casino Games", "🎨 Color Game", "💳 Wallet"])

    # 1. CRICKET LIVE (Real-Time 6-20 Over Fancy Only)
    with tabs[0]:
        st.header("🏏 Live Cricket Exchange")
        l_tabs = st.tabs(["🇵🇰 PSL 2026", "🇮🇳 IPL", "🌍 World Cup"])
        
        with l_tabs[0]:
            matches = [("Peshawar Zalmi", "Lahore Qalandars", 1.82), ("Karachi Kings", "Quetta Gladiators", 2.10)]
            for t1, t2, base_r in matches:
                st.markdown(f"### {t1} vs {t2} (LIVE)")
                # Live Rate Logic
                live_r = round(base_r + random.uniform(-0.04, 0.04), 2)
                
                c1, c2, c3 = st.columns([3, 1, 1])
                c1.write("**Match Winner**")
                c2.markdown(f"<div class='back-btn'>{live_r}<br>BACK</div>", unsafe_allow_html=True)
                c3.markdown(f"<div class='lay-btn'>{round(live_r+0.02, 2)}<br>LAY</div>", unsafe_allow_html=True)
                
                with st.expander(f"📊 Live Fancy (Max 20 Over)"):
                    # Sirf 20 over tak ki fancy
                    f_data = [("6 Over Session", 48), ("10 Over Session", 82), ("15 Over Session", 125), ("20 Over Session", 178)]
                    for f_name, f_val in f_data:
                        v = f_val + random.randint(-2, 2)
                        fc1, fc2, fc3 = st.columns([2, 1, 1])
                        fc1.markdown(f"<div class='fancy
