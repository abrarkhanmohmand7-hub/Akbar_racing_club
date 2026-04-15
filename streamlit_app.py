import streamlit as st

st.set_page_config(page_title="Racing Predictor", page_icon="🏁")
st.title("🏁 Racing Winner Predictor Pro")

tracks_db = {
    'Nottingham': {'fav_trap': 1, 'bonus': 2.5},
    'Towcester':  {'fav_trap': 6, 'bonus': 2.2},
    'Monmore':    {'fav_trap': 1, 'bonus': 2.8},
    'Central Park': {'fav_trap': 3, 'bonus': 1.5},
    'Romford':    {'fav_trap': 2, 'bonus': 2.0}
}

selected_track = st.sidebar.selectbox("Track Chunein", list(tracks_db.keys()))
st.header(f"📍 {selected_track} Entry")

col1, col2 = st.columns(2)
with col1:
    trap = st.number_input("Trap Number", 1, 6, 1)
    last_3 = st.slider("Form (Pichli Position)", 1.0, 6.0, 3.0)
with col2:
    st_time = st.number_input("Split Time", format="%.2f", value=4.15)
    open_odds = st.number_input("Opening Bhao", value=5.0)
    curr_odds = st.number_input("Current Bhao", value=4.0)

if st.button("WINNER PREDICTION CHECK"):
    track_bonus = tracks_db[selected_track]['bonus'] if trap == tracks_db[selected_track]['fav_trap'] else 0
    st_bonus = 3.5 if st_time <= 4.10 else 0
    odds_drop = (open_odds - curr_odds) / (open_odds if open_odds != 0 else 1)
    final_score = ((7 - last_3) * 1.5) + track_bonus + st_bonus + (odds_drop * 15)
    win_percent = min(round((final_score / 25) * 100, 2), 100.0)

    if win_percent >= 75: st.success(f"🔥 WINNER ALERT: {win_percent}%")
    elif win_percent >= 50: st.warning(f"✅ ACHA CHANCE: {win_percent}%")
    else: st.error(f"❌ RISKY: {win_percent}%")
        
