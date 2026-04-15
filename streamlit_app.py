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
import streamlit as st

# Page ki setting (Browser tab ka naam aur layout)
st.set_page_config(page_title="Akbar Khan Admin Panel", layout="wide")

# Sidebar - Jahan se aap settings control kareinge
st.sidebar.title("🛠 Admin Settings")
user_name = st.sidebar.text_input("User Name", "Akbar Khan")
user_balance = st.sidebar.number_input("Wallet Balance", value=1000)

# Live Stream link dalnay ki jagah (YouTube ya kisi bhi site ka link)
st.sidebar.markdown("---")
st.sidebar.subheader("Live Stream Control")
live_url = st.sidebar.text_input("Paste Live Link Here", "https://www.youtube.com/embed/live_stream_id")

# --- Main Dashboard ---
st.title("🏆 Live Games & Betting Dashboard")
st.write(f"Welcome back, **{user_name}** | Balance: **${user_balance}**")

# Screen ko 2 hisson mein taqseem karna (Video aur Data)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📺 Live Match / Race")
    if "youtube.com" in live_url or "youtu.be" in live_url:
        # Agar YouTube ka link hai
        st.video(live_url)
    else:
        # Agar koi betting site ka embed link hai
        st.components.v1.iframe(live_url, height=500, scrolling=True)

with col2:
    st.subheader("📊 Live Odds")
    st.info("Market: Greyhound Racing (Nottingham)")
    
    # Fake Data (Isay aap manually edit kar saktay hain)
    odds_list = [
        {"Trap": 1, "Runner": "Fast Bullet", "Price": "2.50"},
        {"Trap": 2, "Runner": "Golden Paws", "Price": "4.00"},
        {"Trap": 3, "Runner": "Silver Streak", "Price": "1.85"},
        {"Trap": 4, "Runner": "Night Owl", "Price": "6.00"}
    ]
    st.table(odds_list)

    # Betting Section
    st.subheader("💰 Place Your Bet")
    pick = st.selectbox("Select Runner (Trap)", [1, 2, 3, 4])
    amount = st.number_input("Enter Bet Amount", min_value=10, step=10)
    
    if st.button("Confirm Bet"):
        if amount <= user_balance:
            st.success(f"Bet of ${amount} placed on Trap {pick}!")
        else:
            st.error("Insufficient Balance!")

# --- Bottom Section: Results ---
st.divider()
st.subheader("🕒 Recent Results & History")
results_data = {
    "Time": ["14:10", "14:20", "14:30"],
    "Track": ["Kinsley", "Nottingham", "Towcester"],
    "Winner": ["Trap 2", "Trap 5", "Trap 1"],
    "Status": ["Closed", "Closed", "Closed"]
}
st.table(results_data)
    
