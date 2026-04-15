import streamlit as st
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="Akbar Khan - Elite Racing Predictor", layout="centered")

# --- LIVE PAKISTAN TIME ---
pk_time = datetime.utcnow() + timedelta(hours=5)
current_time = pk_time.strftime("%I:%M:%S %p")

# --- HEADER (Wolf777 Style) ---
st.markdown(f"""
    <div style='text-align: center; padding: 20px; border-radius: 15px; background-color: #111827; border: 3px solid #fbbf24; margin-bottom: 20px;'>
        <h1 style='color: #fbbf24; margin: 0; letter-spacing: 2px;'>👤 AKBAR KHAN</h1>
        <p style='color: #ffffff; font-size: 18px; margin: 5px 0;'>🏆 World Tracks Dogs & Horse Predictor</p>
        <div style='background-color: #fbbf24; color: #111827; padding: 5px; border-radius: 5px; display: inline-block; font-weight: bold; font-size: 20px;'>
            🕒 PK Time: {current_time}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- EXPANDED TRACKS DATABASE (50+ Dogs Tracks) ---
dog_tracks = [
    "Addington (NZ)", "Albion Park (AU)", "Angas Park (AU)", "Ballarat (AU)", "Bendigo (AU)", 
    "Brighton (UK)", "Bundaberg (AU)", "Cannington (AU)", "Casino (AU)", "Central Park (UK)", 
    "Cranbourne (AU)", "Crayford (UK)", "Dapto (AU)", "Devonport (AU)", "Doncaster (UK)", 
    "Dubbo (AU)", "Enniscorthy (IE)", "Gawler (AU)", "Geelong (AU)", "Goulburn (AU)", 
    "Grafton (AU)", "Harlow (UK)", "Henlow (UK)", "Hobart (AU)", "Hove (UK)", 
    "Ipswich (AU)", "Kinsley (UK)", "Launceston (AU)", "Limerick (IE)", "Maitland (AU)", 
    "Meadows (AU)", "Monmore (UK)", "Mullingar (IE)", "Murray Bridge (AU)", "Newcastle (UK)", 
    "Newington (UK)", "Northam (AU)", "Nottingham (UK)", "Nowra (AU)", "Oxford (UK)", 
    "Pelaw Grange (UK)", "Perry Barr (UK)", "Richmond (AU)", "Rockhampton (AU)", "Romford (UK)", 
    "Sandown Park (AU)", "Sheffield (UK)", "Shelbourne Park (IE)", "Sunderland (UK)", "Swindon (UK)", 
    "Tamworth (AU)", "Taree (AU)", "Temora (AU)", "The Gardens (AU)", "Towcester (UK)", 
    "Tralee (IE)", "Wagga (AU)", "Warragul (AU)", "Warrnambool (AU)", "Wentworth Park (AU)", 
    "Yarmouth (UK)", "Youghal (IE)"
]

horse_tracks = [
    "Aintree", "Ascot", "Ayr", "Bangor-On-Dee", "Bath", "Beverley", "Brighton", 
    "Carlisle", "Cartmel", "Chelmsford City", "Cheltenham", "Chepstow", "Chester", 
    "Curragh", "Doncaster", "Dundalk", "Epsom Downs", "Exeter", "Fakenham", 
    "Ffos Las", "Fontwell", "Goodwood", "Hamilton", "Haydock", "Hereford", 
    "Huntingdon", "Kelso", "Kempton", "Leicester", "Leopardstown", "Lingfield", 
    "Ludlow", "Market Rasen", "Musselburgh", "Newbury", "Newcastle", "Newmarket", 
    "Newton Abbot", "Nottingham", "Perth", "Plumpton", "Pontefract", "Punchstown", 
    "Redcar", "Ripon", "Salisbury", "Sandown", "Sedgefield", "Southwell", 
    "Stratford", "Taunton", "Thirsk", "Uttoxeter", "Warwick", "Wetherby", 
    "Wincanton", "Windsor", "Wolverhampton", "Worcester", "Yarmouth", "York"
]

# --- SIDEBAR CONTROL ---
st.sidebar.header("🕹️ Control Panel")
game_mode = st.sidebar.radio("Khel Chunein", ["Greyhound (Dogs)", "Horse Racing"])

if game_mode == "Greyhound (Dogs)":
    selected_track = st.sidebar.selectbox("Dogs Track (50+ List)", sorted(dog_tracks))
    runners = 6
else:
    selected_track = st.sidebar.selectbox("Horse Track Select Karen", sorted(horse_tracks))
    runners = st.sidebar.number_input("Kitne Runners (Horses) hain?", 2, 25, 8)

race_time = st.sidebar.text_input("Race Time (Wolf777 se dekhen)", "12:00 PM")
st.sidebar.divider()

# --- MAIN INTERFACE ---
st.title(f"🏁 {game_mode} Analysis")
st.markdown(f"📍 Track: **{selected_track}** | ⏰ Time: **{race_time}**")

# Table Headers
h1, h2, h3 = st.columns([1, 2, 2])
h1.write("**No.**")
h2.write("**Live Odds**")
h3.write("**Form (1-6)**")

data_input = {}

for i in range(1, runners + 1):
    c1, c2, c3 = st.columns([1, 2, 2])
    c1.subheader(f"#{i}")
    odd_val = c2.number_input(f"Bhao {i}", value=4.0, key=f"o_{i}", label_visibility="collapsed")
    form_val = c3.number_input(f"Form {i}", value=3.0, min_value=1.0, max_value=6.0, key=f"f_{i}", label_visibility="collapsed")
    data_input[i] = {'odds': odd_val, 'form': form_val}

st.divider()

if st.button("🔥 START ANALYSIS", use_container_width=True):
    results = []
    for n, data in data_input.items():
        score = 15
        score += (7 - data['form']) * 2
        if data['odds'] <= 2.5: score += 12
        elif data['odds'] <= 4.0: score += 7
        elif data['odds'] <= 6.0: score += 3
        
        chance = min(round((score / 37) * 100, 1), 100.0)
        results.append((n, chance))

    results.sort(key=lambda x: x[1], reverse=True)
    winner_n, winner_p = results[0]

    st.subheader("📊 Winning Probability")
    col_l, col_r = st.columns(2)
    with col_l:
        for n, p in results[:10]: # Top 10 tak show karega
            if p >= 75: st.success(f"No. {n}: {p}% (Strong)")
            elif p >= 50: st.warning(f"No. {n}: {p}% (Medium)")
            else: st.write(f"No. {n}: {p}%")
    with col_r:
        st.metric("BEST PICK", f"#{winner_n}", f"{winner_p}%")
        if winner_p >= 75: st.balloons()
