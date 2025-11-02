import streamlit as st
# ---------- CSS Styling ----------
st.markdown(
"""
<style>
body {
    background: linear-gradient(to right, #1f4037, #99f2c8);
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}
.board {
    display: grid;
    grid-template-columns: repeat(3, 120px);
    grid-gap: 10px;
    justify-content: center;
    margin-top: 30px;
}
.game-button button {
    font-size: 50px;
    height: 120px;
    width: 120px;
    border-radius: 15px;
    border: 2px solid #fff;
    background-color: rgba(255, 255, 255, 0.15);
    color: #fff;
    transition: 0.3s;
}
.game-button button:hover {
    background-color: rgba(255, 255, 255, 0.35);
    transform: scale(1.1);
    cursor: pointer;
}
.winner {
    font-size: 32px;
    margin: 20px 0;
    text-align: center;
    font-weight: bold;
    text-shadow: 2px 2px #00000066;
    animation: fadeIn 0.8s ease-in-out;
}
@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}
.reset-btn button {
    margin-top: 25px;
    font-size: 22px;
    padding: 10px 30px;
    border-radius: 12px;
    background-color: rgba(255,255,255,0.3);
    color: white;
    transition: 0.3s;
}
.reset-btn button:hover {
    background-color: rgba(255,255,255,0.6);
    cursor: pointer;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True
)

# ---------- Initialize Game ----------
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# ---------- Check Winner ----------
def check_winner(board):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return board[pos[0]]
    if "" not in board:
        return "Draw"
    return None

# ---------- Make Move ----------
def make_move(idx):
    if st.session_state.board[idx] == "" and st.session_state.winner is None:
        st.session_state.board[idx] = st.session_state.turn
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner is None:
            st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# ---------- Reset Game ----------
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# ---------- Title ----------
st.title("🎮 Tic Tac Toe Pro")

# ---------- Display Winner ----------
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.markdown('<div class="winner">✨ It\'s a Draw! ✨</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="winner">🏆 Player {st.session_state.winner} Wins!</div>', unsafe_allow_html=True)

# ---------- Board ----------
st.markdown('<div class="board">', unsafe_allow_html=True)
for idx in range(9):
    # Use emojis for X and O for simplicity in GitHub deploy
    btn_label = st.session_state.board[idx]
    st.markdown(f'<div class="game-button">{st.button(btn_label, key=idx, on_click=make_move, args=(idx,))}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Reset Button ----------
st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
st.button("🔄 Reset Game", on_click=reset_game)
st.markdown('</div>', unsafe_allow_html=True)
