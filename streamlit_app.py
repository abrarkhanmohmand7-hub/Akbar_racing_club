import streamlit as st
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Akbar Khan - Racing Predictor", layout="centered")

# --- LIVE PAKISTAN TIME (Manual Calculation) ---
pk_time = datetime.utcnow() + timedelta(hours=5)
current_time = pk_time.strftime("%I:%M:%S %p")

# --- AKBAR KHAN HEADER (Wolf777 Style) ---
st.markdown(f"""
    <div style='text-align: center; padding: 20px; border-radius: 15px; background-color: #111827; border: 3px solid #fbbf24; margin-bottom: 20px;'>
        <h1 style='color: #fbbf24; margin: 0; font-family: sans-serif; letter-spacing: 2px;'>👤 AKBAR KHAN</h1>
        <p style='color: #ffffff; font-size: 18px; margin: 5px 0;'>🏆 Wolf777 Racing Expert Pro</p>
        <div style='background-color: #fbbf24; color: #111827; padding: 5px; border-radius: 5px; display: inline-block; font-weight: bold; font-size: 20px;'>
            🕒 PK Time: {current_time}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
st.sidebar.header("🕹️ Control Panel")
game_mode = st.sidebar.selectbox("Khel Chunein", ["Greyhound (Dogs)", "Horse Racing"])
race_time = st.sidebar.text_input("Race ka Time", "12:00 PM")

# Default runners
runners = 6
if game_mode == "Horse Racing":
    runners = st.sidebar.number_input("Kitne Ghoray hain?", min_value=2, max_value=20, value=8)

st.sidebar.divider()
st.sidebar.info("Wolf777 se live bhao (odds) dekh kar nichey fill karen.")

# --- MAIN INTERFACE ---
st.title(f"🏁 {game_mode} Prediction")
st.write(f"Race Time: **{race_time}**")

# Table Headers
h1, h2, h3 = st.columns([1, 2, 2])
h1.write("**No.**")
h2.write("**Live Odds (Bhao)**")
h3.write("**Form (1-6)**")

data_input = {}

# Dynamic Input Rows
for i in range(1, runners + 1):
    c1, c2, c3 = st.columns([1, 2, 2])
    c1.subheader(f"#{i}")
    odd_val = c2.number_input(f"Odds {i}", value=4.0, key=f"o_{i}", label_visibility="collapsed")
    form_val = c3.number_input(f"Form {i}", value=3.0, min_value=1.0, max_value=6.0, key=f"f_{i}", label_visibility="collapsed")
    data_input[i] = {'odds': odd_val, 'form': form_val}

st.divider()

# --- CALCULATION ---
if st.button("🔥 FIND WINNER", use_container_width=True):
    results = []
    for n, data in data_input.items():
        # Score calculation
        score = 15 # Base
        score += (7 - data['form']) * 2 # Form weight
        
        # Odds weight (Wolf777 market sentiment)
        if data['odds'] <= 2.5: score += 12
        elif data['odds'] <= 4.0: score += 7
        elif data['odds'] <= 6.0: score += 3
        
        chance = min(round((score / 37) * 100, 1), 100.0)
        results.append((n, chance))

    # Sort to get the top one
    results.sort(key=lambda x: x[1], reverse=True)
    winner_n, winner_p = results[0]

    # --- DISPLAY RESULTS ---
    st.subheader("📊 Analysis Results")
    col_left, col_right = st.columns(2)

    with col_left:
        for n, p in results[:6]: # Top 6 show honge
            if p >= 75:
                st.success(f"Number {n}: {p}% (Strong)")
            elif p >= 50:
                st.warning(f"Number {n}: {p}% (Medium)")
            else:
                st.write(f"Number {n}: {p}% (Low)")

    with col_right:
        st.metric(label="🏆 TOP RECOMMENDATION", value=f"Number {winner_n}", delta=f"{winner_p}% Chance")
        if winner_p >= 75:
            st.balloons()
            st.markdown("🎯 **Safe Bet!** Form aur market bhao dono aapke haq mein hain.")

st.divider()
st.caption("Yeh software sirf mashwara deta hai. Aakhri faisla soch samajh kar karen.")
