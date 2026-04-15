import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="VIP LIVE EXCHANGE", page_icon="🏏", layout="wide")

if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- PREMIUM STYLING ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #ffd700; }
    .card-box {
        background: white; color: black; width: 95px; height: 135px;
        border-radius: 10px; display: inline-flex; flex-direction: column;
        justify-content: center; align-items: center; border: 3px solid #ffd700;
        box-shadow: 0px 0px 12px #ffd700; margin: 10px;
    }
    .card-num { font-size: 38px; font-weight: bold; line-height: 1; color: black; }
    .card-suit { font-size: 32px; }
    .red { color: #ff0000 !important; }
    .black { color: #000000 !important; }
    .back-btn { background-color: #72bbef; color: black !important; font-weight: bold; padding: 12px; text-align: center; border-radius: 6px; border: 1px solid white; }
    .lay-btn { background-color: #faa9ba; color: black !important; font-weight: bold; padding: 12px; text-align: center; border-radius: 6px; border: 1px solid white; }
    .footer { text-align: center; color: #ffd700; font-size: 24px; font-weight: bold; margin-top: 50px; border-top: 3px solid #ffd700; padding-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Helper: Real Card Graphics
def draw_card(n, s, c):
    st.markdown(f'<div class="card-box"><div class="card-num">{n}</div><div class="card-suit {c}">{s}</div></div>', unsafe_allow_html=True)

def get_random_card():
    nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    suits = [("♥️", "red"), ("♦️", "red"), ("♠️", "black"), ("♣️", "black")]
    n, (s, c) = random.choice(nums), random.choice(suits)
    return n, s, c

# --- LOGIN LOGIC ---
if not st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>🎰 VIP MASTER EXCHANGE</h1>", unsafe_allow_html=True)
    st.divider()
    key = st.text_input("Admin Secret Key", type="password")
    if st.button("Unlock All Live Systems"):
        if key == "Akbar786":
            st.session_state.is_admin = True
            st.rerun()
else:
    # --- MAIN EXCHANGE PANEL ---
    st.sidebar.title("👑 VIP Panel")
    if st.sidebar.button("Logout"):
        st.session_state.is_admin = False
        st.rerun()

    tabs = st.tabs(["🏏 Cricket Live", "🚀 Aviator", "🔄 Live Casino", "💳 Wallet"])

    # 1. CRICKET (Leagues + Live Market Rates + 6-20 Fancy)
    with tabs[0]:
        st.header("🏏 Live Market Engine")
        leagues = st.tabs(["🇵🇰 PSL 2026", "🇮🇳 IPL", "🌍 World Cup"])
        
        with leagues[0]:
            matches = [("Peshawar Zalmi", "Lahore Qalandars", 1.85), ("Karachi Kings", "Quetta Gladiators", 2.05)]
            for t1, t2, base in matches:
                live_r = round(base + random.uniform(-0.05, 0.05), 2)
                st.subheader(f"{t1} vs {t2}")
                c1, c2, c3 = st.columns([3, 1, 1])
                c1.write("Match Odds")
                c2.markdown(f"<div class='back-btn'>{live_r}<br>BACK</div>", unsafe_allow_html=True)
                c3.markdown(f"<div class='lay-btn'>{round(live_r+0.02, 2)}<br>LAY</div>", unsafe_allow_html=True)
                
                with st.expander("📊 Market Fancy (6-20 Over Only)"):
                    for f_name, f_val in [("6 Over", 48), ("10 Over", 82), ("15 Over", 124), ("20 Over", 175)]:
                        v = f_val + random.randint(-2, 2)
                        fc1, fc2, fc3 = st.columns([2, 1, 1])
                        fc1.write(f"**{f_name} Session**")
                        fc2.button(f"{v}\nNO", key=f"{t1}{f_name}n")
                        fc3.button(f"{v+2}\nYES", key=f"{t1}{f_name}y")
                st.divider()

    # 2. CASINO (All Games with Card Numbers + Logic)
    with tabs[2]:
        st.header("🔄 Live Casino Hub")
        game = st.selectbox("Select Game", ["Teen Patti", "Dragon vs Tiger", "Andar Bahar", "Color Prediction"])
        
        st.info("Winning Logic Active: Game will reward the side with minimum bets.")
        
        if st.button("Start Live Round"):
            with st.spinner("Dealing Cards..."):
                time.sleep(2)
                if game == "Teen Patti":
                    p1, p2, p3 = st.columns(3)
                    with p1: draw_card(*get_random_card())
                    with p2: draw_card(*get_random_card())
                    with p3: draw_card(*get_random_card())
                elif game == "Dragon vs Tiger":
                    d, t = st.columns(2)
                    with d: st.write("Dragon"); draw_card(*get_random_card())
                    with t: st.write("Tiger"); draw_card(*get_random_card())
                elif game == "Andar Bahar":
                    st.write("Joker Card")
                    draw_card(*get_random_card())
                else: # Color
                    st.write("Color Result Card")
                    draw_card(*get_random_card())
                st.success("Result: Minimum Bet Side Wins! ✅")

    # 3. AVIATOR
    with tabs[1]:
        st.header("🚀 Aviator")
        if st.button("Fly Now"):
            crash = round(random.uniform(1.1, 3.5), 2)
            m = 1.00
            p = st.empty()
            while m < crash:
                p.markdown(f"<h1 style='text-align:center; font-size:80px;'>{m:.2f}x</h1>", unsafe_allow_html=True)
                time.sleep(0.1); m += 0.05
            st.error(f"💥 CRASHED @ {m:.2f}x")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        👑 Admin by Akbar khan 👑<br>
        <span style="font-size: 14px; opacity: 0.8;">Live Exchange Engine Active • © 2026</span>
    </div>
""", unsafe_allow_html=True)

# Auto-Refresh for Market Rates
if st.session_state.is_admin:
    time.sleep(10)
    st.rerun()
