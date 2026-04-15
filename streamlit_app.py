import streamlit as st
from datetime import datetime
import pytz # Pakistan time ke liye

st.set_page_config(page_title="Easy Predictor", layout="centered")

# --- LIVE PAKISTAN TIME ---
pk_timezone = pytz.timezone('Asia/Karachi')
current_time = datetime.now(pk_timezone).strftime("%I:%M:%S %p")
st.markdown(f"### 🕒 Pakistan Time: `{current_time}`")

st.title("🏁 Quick Trap Analysis")
st.sidebar.link_button("📅 Live Race Info", "https://www.racingpost.com/greyhounds/")

# Sidebar for Race Selection
st.sidebar.subheader("Race Settings")
race_time_input = st.sidebar.text_input("Race Scheduled Time", placeholder="e.g. 12:30 PM")
distance = st.radio("Race Type", ["Sprints", "Standard", "Stayers"], horizontal=True)

st.divider()

# TABLE HEADERS
h1, h2, h3 = st.columns([1, 2, 2])
h1.write("**Trap**")
h2.write("**Live Odds**")
h3.write("**Split Time**")

traps_data = {}

# ONLY 2 BOXES PER TRAP
for i in range(1, 7):
    c1, c2, c3 = st.columns([1, 2, 2])
    c1.subheader(f"#{i}")
    l_odds = c2.number_input(f"Bhao {i}", value=4.0, key=f"l{i}", label_visibility="collapsed")
    s_time = c3.number_input(f"Time {i}", value=4.10, format="%.2f", key=f"s{i}", label_visibility="collapsed")
    traps_data[i] = {'odds': l_odds, 'split': s_time}

st.divider()

if st.button("🔥 CHECK BEST TRAP", use_container_width=True):
    limit = 3.45 if distance == "Sprints" else 4.35 if distance == "Stayers" else 4.10
    results = []

    for t_num, data in traps_data.items():
        score = 10 
        if data['split'] <= limit: score += 7 
        if data['odds'] < 3.0: score += 5
        elif data['odds'] < 5.0: score += 3
        
        pct = min(round((score / 25) * 100, 1), 100.0)
        results.append((t_num, pct))

    results.sort(key=lambda x: x[1], reverse=True)
    best_t, best_p = results[0]

    st.subheader(f"🏆 Result for {race_time_input}")
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        for t, p in results:
            if p >= 70: st.success(f"Trap {t}: {p}%")
            else: st.write(f"Trap {t}: {p}%")

    with res_col2:
        st.metric("WINNER", f"Trap {best_t}", f"{best_p}%")
        if best_p >= 70: st.balloons()
