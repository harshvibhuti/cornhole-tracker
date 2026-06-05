import streamlit as st

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🎯 Cornhole Tracker",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
  /* Import fonts */
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');

  /* Global styles */
  html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
  }

  /* App background */
  .stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
  }

  /* Hide default Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }

  /* Title */
  .title-block {
    text-align: center;
    padding: 1rem 0 0.5rem;
  }
  .title-block h1 {
    font-size: clamp(2rem, 8vw, 3.5rem);
    font-weight: 900;
    background: linear-gradient(90deg, #f7971e, #ffd200);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: -1px;
  }
  .title-block p {
    color: #a0aec0;
    font-size: 1rem;
    margin: 0;
  }

  /* Score board */
  .scoreboard {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
  }
  .score-card {
    flex: 1;
    border-radius: 20px;
    padding: 1.25rem 0.75rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    border: 2px solid transparent;
  }
  .score-card.team-a {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    border-color: #4a90d9;
  }
  .score-card.team-b {
    background: linear-gradient(135deg, #7b1e1e, #b03030);
    border-color: #e05555;
  }
  .score-card.leading {
    box-shadow: 0 0 24px rgba(255, 210, 0, 0.5);
    border-color: #ffd200 !important;
  }
  .score-label {
    color: rgba(255,255,255,0.7);
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
  }
  .score-name {
    color: #fff;
    font-size: clamp(1.2rem, 4vw, 1.6rem);
    font-weight: 900;
    margin-bottom: 0.5rem;
    word-break: break-word;
  }
  .score-value {
    font-size: clamp(3rem, 12vw, 5rem);
    font-weight: 900;
    line-height: 1;
    color: #fff;
    text-shadow: 0 4px 12px rgba(0,0,0,0.4);
  }
  .score-to-win {
    color: rgba(255,255,255,0.6);
    font-size: 0.78rem;
    margin-top: 0.4rem;
  }
  .crown {
    font-size: 1.4rem;
    display: block;
    margin-bottom: 0.2rem;
  }

  /* Round counter */
  .round-badge {
    text-align: center;
    margin: 0.5rem 0 1rem;
  }
  .round-badge span {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 50px;
    padding: 0.3rem 1.2rem;
    color: #e2e8f0;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 1px;
  }

  /* Section headers */
  .section-header {
    color: rgba(255,255,255,0.8);
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 1.2rem 0 0.6rem;
    text-align: center;
  }

  /* Input columns */
  .input-group {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 1rem;
    margin-bottom: 0.75rem;
  }
  .input-group-label {
    color: #fff;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  /* Number inputs — bigger touch targets */
  div[data-testid="stNumberInput"] input {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    height: 3.2rem !important;
    border-radius: 12px !important;
    background: rgba(255,255,255,0.1) !important;
    color: #fff !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
  }
  div[data-testid="stNumberInput"] button {
    font-size: 1.4rem !important;
    min-width: 3rem !important;
    min-height: 3rem !important;
    border-radius: 10px !important;
  }

  /* Buttons */
  div[data-testid="stButton"] > button {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 900 !important;
    font-size: clamp(1rem, 4vw, 1.3rem) !important;
    border-radius: 16px !important;
    padding: 0.85rem 1rem !important;
    width: 100% !important;
    border: none !important;
    transition: all 0.15s ease !important;
    letter-spacing: 0.5px !important;
  }
  div[data-testid="stButton"] > button:active {
    transform: scale(0.97) !important;
  }

  /* Primary button (Next Round) */
  div[data-testid="stButton"]:nth-child(1) > button {
    background: linear-gradient(135deg, #f7971e, #ffd200) !important;
    color: #1a1a2e !important;
    box-shadow: 0 6px 20px rgba(247,151,30,0.4) !important;
  }

  /* Divider */
  hr {
    border-color: rgba(255,255,255,0.1) !important;
    margin: 1rem 0 !important;
  }

  /* Winner banner */
  .winner-banner {
    background: linear-gradient(135deg, #f7971e, #ffd200);
    border-radius: 20px;
    padding: 2rem 1rem;
    text-align: center;
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(247,151,30,0.5);
    animation: pulse-glow 1.5s ease-in-out infinite alternate;
  }
  @keyframes pulse-glow {
    from { box-shadow: 0 8px 32px rgba(247,151,30,0.4); }
    to   { box-shadow: 0 8px 48px rgba(247,151,30,0.9); }
  }
  .winner-banner h2 {
    font-size: clamp(1.8rem, 8vw, 3rem);
    font-weight: 900;
    color: #1a1a2e;
    margin: 0 0 0.5rem;
  }
  .winner-banner p {
    font-size: 1rem;
    color: rgba(26,26,46,0.75);
    margin: 0;
  }

  /* Round history */
  .history-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0.75rem;
    border-radius: 10px;
    margin-bottom: 0.3rem;
    background: rgba(255,255,255,0.05);
    color: #cbd5e0;
    font-size: 0.88rem;
  }
  .history-row:nth-child(even) {
    background: rgba(255,255,255,0.03);
  }
  .history-label {
    color: #a0aec0;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
  }

  /* Stale label fix */
  label { color: rgba(255,255,255,0.75) !important; font-size: 0.9rem !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ─── Session state defaults ────────────────────────────────────────────────────
def _init():
    defaults = {
        "score_a": 0,
        "score_b": 0,
        "round_num": 1,
        "game_over": False,
        "winner": "",
        "history": [],       # list of dicts per round
        "team_a_name": "Team A",
        "team_b_name": "Team B",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init()

# ─── Helper ────────────────────────────────────────────────────────────────────
def reset_game():
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.round_num = 1
    st.session_state.game_over = False
    st.session_state.winner = ""
    st.session_state.history = []


def submit_round(board_a, hole_a, board_b, hole_b):
    raw_a = board_a * 1 + hole_a * 3
    raw_b = board_b * 1 + hole_b * 3

    # Cancellation scoring
    if raw_a > raw_b:
        net_a = raw_a - raw_b
        net_b = 0
    elif raw_b > raw_a:
        net_a = 0
        net_b = raw_b - raw_a
    else:
        net_a = 0
        net_b = 0

    st.session_state.score_a += net_a
    st.session_state.score_b += net_b

    st.session_state.history.append(
        {
            "round": st.session_state.round_num,
            "raw_a": raw_a,
            "raw_b": raw_b,
            "net_a": net_a,
            "net_b": net_b,
            "total_a": st.session_state.score_a,
            "total_b": st.session_state.score_b,
        }
    )

    # Check winner
    if st.session_state.score_a >= 21 or st.session_state.score_b >= 21:
        st.session_state.game_over = True
        if st.session_state.score_a > st.session_state.score_b:
            st.session_state.winner = st.session_state.team_a_name
        elif st.session_state.score_b > st.session_state.score_a:
            st.session_state.winner = st.session_state.team_b_name
        else:
            st.session_state.winner = "Both Teams (Tie!)"
    else:
        st.session_state.round_num += 1


# ─── Title ─────────────────────────────────────────────────────────────────────
st.markdown(
    "<div class='title-block'><h1>🎯 Cornhole</h1><p>Cancellation Scoring</p></div>",
    unsafe_allow_html=True,
)

# ─── Team name customisation (collapsed expander) ──────────────────────────────
with st.expander("✏️ Customize Team Names"):
    col1, col2 = st.columns(2)
    with col1:
        new_a = st.text_input("Team A Name", value=st.session_state.team_a_name, max_chars=16)
    with col2:
        new_b = st.text_input("Team B Name", value=st.session_state.team_b_name, max_chars=16)
    if new_a != st.session_state.team_a_name:
        st.session_state.team_a_name = new_a
    if new_b != st.session_state.team_b_name:
        st.session_state.team_b_name = new_b

# ─── Scoreboard ───────────────────────────────────────────────────────────────
sa = st.session_state.score_a
sb = st.session_state.score_b
a_lead = sa > sb
b_lead = sb > sa

crown_a = "👑 " if a_lead else ""
crown_b = "👑 " if b_lead else ""
lead_a  = " leading" if a_lead else ""
lead_b  = " leading" if b_lead else ""

to_win_a = max(0, 21 - sa)
to_win_b = max(0, 21 - sb)

st.markdown(
    f"""
<div class="scoreboard">
  <div class="score-card team-a{lead_a}">
    <div class="score-label">🔵 {st.session_state.team_a_name}</div>
    <div class="score-value">{crown_a}{sa}</div>
    <div class="score-to-win">{"🏆 Wins!" if sa >= 21 else f"{to_win_a} pts to win"}</div>
  </div>
  <div class="score-card team-b{lead_b}">
    <div class="score-label">🔴 {st.session_state.team_b_name}</div>
    <div class="score-value">{crown_b}{sb}</div>
    <div class="score-to-win">{"🏆 Wins!" if sb >= 21 else f"{to_win_b} pts to win"}</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Winner banner ─────────────────────────────────────────────────────────────
if st.session_state.game_over:
    st.markdown(
        f"""
<div class="winner-banner">
  <h2>🏆 {st.session_state.winner} Wins!</h2>
  <p>Final score: {st.session_state.team_a_name} {sa} – {sb} {st.session_state.team_b_name}</p>
</div>
""",
        unsafe_allow_html=True,
    )
    if st.button("🔄 Play Again", use_container_width=True):
        reset_game()
        st.rerun()
    st.stop()

# ─── Round badge ───────────────────────────────────────────────────────────────
st.markdown(
    f"<div class='round-badge'><span>ROUND {st.session_state.round_num}</span></div>",
    unsafe_allow_html=True,
)

# ─── Round input ───────────────────────────────────────────────────────────────
st.markdown("<div class='section-header'>Enter This Round's Bags</div>", unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"<div class='input-group'>", unsafe_allow_html=True)
    st.markdown(f"**🔵 {st.session_state.team_a_name}**")
    board_a = st.number_input(
        "🟫 On Board (1 pt each)",
        min_value=0, max_value=4, value=0, step=1,
        key="board_a",
    )
    hole_a = st.number_input(
        "🕳️ In Hole (3 pts each)",
        min_value=0, max_value=4, value=0, step=1,
        key="hole_a",
    )
    round_total_a = board_a * 1 + hole_a * 3
    st.markdown(f"**Round raw: {round_total_a} pts**")
    st.markdown("</div>", unsafe_allow_html=True)

with col_b:
    st.markdown(f"<div class='input-group'>", unsafe_allow_html=True)
    st.markdown(f"**🔴 {st.session_state.team_b_name}**")
    board_b = st.number_input(
        "🟫 On Board (1 pt each)",
        min_value=0, max_value=4, value=0, step=1,
        key="board_b",
    )
    hole_b = st.number_input(
        "🕳️ In Hole (3 pts each)",
        min_value=0, max_value=4, value=0, step=1,
        key="hole_b",
    )
    round_total_b = board_b * 1 + hole_b * 3
    st.markdown(f"**Round raw: {round_total_b} pts**")
    st.markdown("</div>", unsafe_allow_html=True)

# Live cancellation preview
diff = round_total_a - round_total_b
if diff > 0:
    preview = f"➕ **{st.session_state.team_a_name}** scores **{diff}** point{'s' if diff != 1 else ''} this round"
elif diff < 0:
    preview = f"➕ **{st.session_state.team_b_name}** scores **{abs(diff)}** point{'s' if abs(diff) != 1 else ''} this round"
else:
    preview = "⚖️ **Cancelled!** No points awarded this round"

st.info(preview)

# ─── Action buttons ────────────────────────────────────────────────────────────
st.markdown("")
btn_col1, btn_col2 = st.columns([3, 1])

with btn_col1:
    if st.button("✅ Next Round", use_container_width=True):
        submit_round(board_a, hole_a, board_b, hole_b)
        st.rerun()

with btn_col2:
    if st.button("🔄 Reset", use_container_width=True, type="secondary"):
        reset_game()
        st.rerun()

# ─── Round history ─────────────────────────────────────────────────────────────
if st.session_state.history:
    st.divider()
    st.markdown("<div class='section-header'>Round History</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='history-label'>"
        "Rd &nbsp;&nbsp; "
        f"{st.session_state.team_a_name[:6]} raw → net (total) &nbsp; | &nbsp; "
        f"{st.session_state.team_b_name[:6]} raw → net (total)"
        "</div>",
        unsafe_allow_html=True,
    )
    for h in reversed(st.session_state.history):
        st.markdown(
            f"<div class='history-row'>"
            f"<b>R{h['round']}</b> &nbsp;"
            f"🔵 {h['raw_a']}→<b>{h['net_a']}</b> ({h['total_a']}) &nbsp;|&nbsp; "
            f"🔴 {h['raw_b']}→<b>{h['net_b']}</b> ({h['total_b']})"
            f"</div>",
            unsafe_allow_html=True,
        )
