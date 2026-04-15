import streamlit as st
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="Akbar Khan - One Click Predictor", layout="centered")

# --- LIVE PAKISTAN TIME ---
pk_time = datetime.utcnow() + timedelta(hours=5)
current_time = pk_time.strftime("%I:%M:%S %p")

# --- HEADER ---
st.markdown(f"""
    <div style='text-align: center; padding: 20px; border-radius: 15px; background-color: #111827; border: 3px solid #fbbf24; margin-bottom: 20px;'>
        <h1 style='color: #fbbf24; margin: 0;'>👤 AKBAR KHAN</h1>
        <p style='color: #ffffff; font-size: 18px;'>🏆 Fast Wolf777 Odds Predictor</p>
        <div style='background-color: #fbbf24; color: #111827; padding: 5px; border-radius: 5px; display: inline-block; font-weight: bold;'>
            🕒 PK Time: {current_time}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- TRACKS DATABASE ---
dog_tracks = ["Addington (NZ)", "Albion Park (AU)", "Angas Park (AU)", "Ballarat (AU)", "Bendigo (AU)", "Brighton (UK)", "Central Park (UK)", "Crayford (UK)", "Doncaster (UK)", "Harlow (UK)", "Henlow (UK)", "Hove (UK)", "Kinsley (UK)", "Monmore (UK)", "Newcastle (UK)", "Nottingham (UK)", "Oxford (UK)", "Pelaw Grange (UK)", "Perry Barr (UK)", "Romford (UK)", "Sheffield (UK)", "Sunderland (UK)", "Swindon (UK)", "Towcester (UK)", "Yarmouth (UK)", "Youghal (IE)"]
horse_tracks = ["Aintree", "Ascot", "Cheltenham", "Chester", "Curragh", "Doncaster", "Dundalk", "Epsom Downs", "Goodwood", "Haydock", "Kempton", "Leopardstown", "Lingfield", "Newbury", "Newcastle", "Newmarket", "Sandown", "Southwell", "Wolverhampton", "York"]

# --- SIDEBAR CONTROL ---
st.sidebar.header("🕹️ Setup")
game_mode = st.sidebar.radio("Khel Chunein", ["Greyhound (Dogs)", "Horse Racing"])

if game_mode == "Greyhound (Dogs)":
    selected_track = st.sidebar.selectbox("Track", sorted(dog_tracks))
    runners = 6
else:
    selected_track = st.sidebar.selectbox("Track", sorted(horse_tracks))
    runners = st.sidebar.number_input("Kitne Ghoray hain?", 2, 25, 8)

race_time = st.sidebar.text_input("Race Time", "12:00 PM")

# --- MAIN INTERFACE ---
st.title(f"🏁 {game_mode} Prediction")
st.markdown(f"📍 **{selected_track}** | ⏰ **{race_time}**")

st.divider()

# Only Odds Input
st.subheader("Write Odds (Bhao) Below:")
odds_input = {}

for i in range(1, runners + 1):
    c1, c2 = st.columns([1, 4])
    c1.write(f"### #{i}")
    val = c2.number_input(f"Odds for {i}", value=4.0, key=f"o_{i}", label_visibility="collapsed")
    odds_input[i] = val

st.divider()

if st.button("🔥 ANALYZE NOW", use_container_width=True):
    results = []
    for n, o in odds_input.items():
        # Score based strictly on Odds
        if o <= 2.0: score = 95
        elif o <= 3.0: score = 80
        elif o <= 4.5: score = 65
        elif o <= 7.0: score = 45
        else: score = 25
        
        results.append((n, score))

    results.sort(key=lambda x: x[1], reverse=True)
    winner_n, winner_p = results[0]

    st.subheader("📊 Top Pick")
    res_c1, res_c2 = st.columns(2)
    with res_c1:
        for n, p in results[:5]:
            if p >= 80: st.success(f"Number {n}: {p}% Chance")
            else: st.write(f"Number {n}: {p}%")
    with res_c2:
        st.metric("BEST BET", f"#{winner_n}", f"{winner_p}%")
        if winner_p >= 80: st.balloons()
