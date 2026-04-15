import streamlit as st

st.set_page_config(page_title="Racing Predictor Pro", page_icon="🏁")
st.title("🏁 Greyhound Winner Predictor Pro")

# ALL TRACKS DATABASE
tracks_db = {
    'Nottingham': 1, 'Towcester': 6, 'Monmore': 1, 'Central Park': 3, 'Romford': 2,
    'Doncaster': 1, 'Harlow': 1, 'Hove': 1, 'Kinsley': 2, 'Newcastle': 1,
    'Oxford': 1, 'Perry Barr': 1, 'Sheffield': 1, 'Sunderland': 1, 'Swindon': 1,
    'Yarmouth': 1, 'Brighton': 1, 'Crayford': 1, 'Henlow': 1, 'Pelaw Grange': 1,
    'Mullingar': 1, 'Tralee': 1, 'Youghal': 1, 'Shelbourne Park': 1, 'Curraheen Park': 1,
    'Dundalk': 1, 'Enniscorthy': 1, 'Galway': 1, 'Limerick': 1, 'Thurles': 1, 'Waterford': 1
}

# SIDEBAR SECTION
st.sidebar.markdown("### 📅 Live Race Time")
st.sidebar.link_button("Check Today's Races 🔗", "https://www.racingpost.com/greyhounds/")

st.sidebar.header("📍 Race Selection")
selected_track = st.sidebar.selectbox("Track Chunein", sorted(list(tracks_db.keys())))
distance = st.sidebar.selectbox("Distance", ["Sprints (270m-300m)", "Standard (450m-480m)", "Stayers (500m+)"])

# MAIN INTERFACE
st.header(f"📊 {selected_track} ({distance})")

# Kutton ke naam ke liye khali dabbe (Empty Boxes)
st.subheader("📝 Dogs ke Naam Likhen")
col_n1, col_n2 = st.columns(2)
with col_n1:
    dog1 = st.text_input("Trap 1 Name", placeholder="E.g. Swift Bolt")
    dog2 = st.text_input("Trap 2 Name", placeholder="E.g. Blue Moon")
    dog3 = st.text_input("Trap 3 Name", placeholder="E.g. Red Fire")
with col_n2:
    dog4 = st.text_input("Trap 4 Name", placeholder="E.g. Gold Rush")
    dog5 = st.text_input("Trap 5 Name", placeholder="E.g. Black Jack")
    dog6 = st.text_input("Trap 6 Name", placeholder="E.g. Silver Star")

st.divider()

# Calculation Inputs
st.subheader("🔢 Prediction Data")
col_in1, col_in2 = st.columns(2)
with col_in1:
    check_trap = st.number_input("Kis Trap ka result dekhna hai? (1-6)", 1, 6, 1)
    last_3 = st.slider("Form (Pichli Position)", 1.0, 6.0, 3.0)
with col_in2:
    st_time = st.number_input("Split Time (Sectional)", format="%.2f", value=4.15)
    open_odds = st.number_input("Opening Bhao", value=5.0)
    curr_odds = st.number_input("Current Bhao", value=4.0)

# BUTTON AND LOGIC
if st.button("WINNER PREDICTION CHECK"):
    # Split time threshold logic
    target_split = 3.45 if "Sprints" in distance else 4.35 if "Stayers" in distance else 4.10
    
    # Core Logic Formula
    score = 0
    score += (7 - last_3) * 1.5 # Form points
    if st_time <= target_split: score += 5 # Speed points
    
    odds_diff = open_odds - curr_odds
    if odds_diff > 0: score += (odds_diff / open_odds) * 15 # Market trend
    
    # Fav Trap Bonus
    if check_trap == tracks_db[selected_track]: score += 3

    win_percent = min(round((score / 23) * 100, 2), 100.0)

    # Naam nikalna (Selection)
    dogs_list = [dog1, dog2, dog3, dog4, dog5, dog6]
    selected_dog_name = dogs_list[check_trap-1] if dogs_list[check_trap-1] else f"Trap {check_trap}"
    
    # Output Display
    if win_percent >= 75: 
        st.success(f"🔥 HIGH CHANCE WINNER: {selected_dog_name} ({win_percent}%)")
        st.balloons()
    elif win_percent >= 50: 
        st.warning(f"✅ DECENT CHANCE: {selected_dog_name} ({win_percent}%)")
    else: 
        st.error(f"❌ RISKY / LOW CHANCE: {selected_dog_name} ({win_percent}%)")

st.info("Tip: Racing Post se Dogs ke naam dekh kar yahan likhen aur result check karen.")
