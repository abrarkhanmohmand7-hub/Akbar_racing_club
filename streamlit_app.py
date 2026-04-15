import streamlit as st

st.set_page_config(page_title="Racing Predictor Pro", page_icon="🏁")
st.title("🏁 Greyhound Winner Predictor Pro")

# SARY TRACKS (UK & IRELAND)
tracks_db = {
    'Nottingham': 1, 'Towcester': 6, 'Monmore': 1, 'Central Park': 3, 'Romford': 2,
    'Doncaster': 1, 'Harlow': 1, 'Hove': 1, 'Kinsley': 2, 'Newcastle': 1,
    'Oxford': 1, 'Perry Barr': 1, 'Sheffield': 1, 'Sunderland': 1, 'Swindon': 1,
    'Yarmouth': 1, 'Brighton': 1, 'Crayford': 1, 'Henlow': 1, 'Pelaw Grange': 1,
    'Mullingar': 1, 'Tralee': 1, 'Youghal': 1, 'Shelbourne Park': 1, 'Curraheen Park': 1,
    'Dundalk': 1, 'Enniscorthy': 1, 'Galway': 1, 'Limerick': 1, 'Thurles': 1, 'Waterford': 1
}

# LIVE SCHEDULE BUTTON
st.sidebar.markdown("### 📅 Live Race Time & Info")
st.sidebar.link_button("Check Today's Races 🔗", "https://www.racingpost.com/greyhounds/racecards/")

st.sidebar.header("📍 Race Selection")
selected_track = st.sidebar.selectbox("Track Chunein", sorted(list(tracks_db.keys())))
distance = st.sidebar.selectbox("Distance", ["Sprints (270m-300m)", "Standard (450m-480m)", "Stayers (500m+)"])

st.header(f"📊 {selected_track} Entry")

col1, col2 = st.columns(2)
with col1:
    trap = st.number_input("Trap Number", 1, 6, 1)
    last_3 = st.slider("Form (Pichli Position)", 1.0, 6.0, 3.0)
with col2:
    st_time = st.number_input("Split Time", format="%.2f", value=4.15)
    open_odds = st.number_input("Opening Bhao", value=5.0)
    curr_odds = st.number_input("Current Bhao", value=4.0)

if st.button("WINNER PREDICTION CHECK"):
    target_split = 3.45 if "Sprints" in distance else 4.35 if "Stayers" in distance else 4.10
    score = ((7 - last_3) * 1.5) + (5 if st_time <= target_split else 0) + (((open_odds - curr_odds) / (open_odds if open_odds != 0 else 1)) * 15)
    if trap == tracks_db[selected_track]: score += 3
    win_percent = min(round((score / 23) * 100, 2), 100.0)

    if win_percent >= 75: st.success(f"🔥 HIGH CHANCE: {win_percent}%"); st.balloons()
    elif win_percent >= 50: st.warning(f"✅ DECENT CHANCE: {win_percent}%")
    else: st.error(f"❌ RISKY: {win_percent}%")
        
