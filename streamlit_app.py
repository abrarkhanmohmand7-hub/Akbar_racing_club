import streamlit as st

st.set_page_config(page_title="Race Predictor Pro", layout="centered")

# Header section
st.title("🏁 Quick Trap Predictor")
st.sidebar.link_button("📅 Check Race Times", "https://www.racingpost.com/greyhounds/")

# User Inputs for Track and Type
track = st.selectbox("Track Chunein", ['Nottingham', 'Towcester', 'Monmore', 'Romford', 'Kinsley', 'Sheffield', 'Hove', 'Newcastle', 'Sunderland', 'Yarmouth'])
distance = st.radio("Race Type", ["Sprints", "Standard", "Stayers"], horizontal=True)

st.divider()

# TABLE HEADINGS
cols = st.columns([1, 2, 2, 2])
cols[0].write("**Trap**")
cols[1].write("**Open Odds**")
cols[2].write("**Live Odds**")
cols[3].write("**Split Time**")

traps_data = {}

# SIMPLE 6-TRAP INPUTS
for i in range(1, 7):
    r = st.columns([1, 2, 2, 2])
    r[0].write(f"**# {i}**")
    o = r[1].number_input(f"O{i}", value=5.0, key=f"o{i}", label_visibility="collapsed")
    l = r[2].number_input(f"L{i}", value=4.5, key=f"l{i}", label_visibility="collapsed")
    s = r[3].number_input(f"S{i}", value=4.10, format="%.2f", key=f"s{i}", label_visibility="collapsed")
    traps_data[i] = {'o': o, 'l': l, 's': s}

st.divider()

if st.button("🔥 SHOW WINNER CHANCE", use_container_width=True):
    # Logic setup
    limit = 3.45 if distance == "Sprints" else 4.35 if distance == "Stayers" else 4.10
    results = []

    for t_num, data in traps_data.items():
        score = 10 # Base
        if data['s'] <= limit: score += 6 # Speed
        
        drop = data['o'] - data['l']
        if drop > 0: score += (drop / data['o']) * 15 # Market Trend
        
        pct = min(round((score / 25) * 100, 1), 100.0)
        results.append((t_num, pct))

    # Sort to get the highest
    results.sort(key=lambda x: x[1], reverse=True)
    best_t, best_p = results[0]

    # Display results
    st.subheader("🏆 Winning Chances")
    c_res1, c_res2 = st.columns(2)
    
    with c_res1:
        for t, p in results:
            if p >= 70: st.success(f"Trap {t}: {p}%")
            elif p >= 45: st.warning(f"Trap {t}: {p}%")
            else: st.write(f"Trap {t}: {p}%")

    with c_res2:
        st.metric("BEST BET", f"Trap {best_t}", f"{best_p}%")
        if best_p >= 75:
            st.balloons()
            st.markdown("🎯 **Solid Chance!** Bhao gir raha hai aur speed bhi achi hai.")
