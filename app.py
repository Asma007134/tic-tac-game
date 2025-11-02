import streamlit as st

# Initialize
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Check winner
def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] != "":
            return board[line[0]]
    if "" not in board:
        return "Draw"
    return None

# Make move
def make_move(idx):
    if st.session_state.board[idx] == "" and st.session_state.winner is None:
        st.session_state.board[idx] = st.session_state.turn
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner is None:
            st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# Reset game
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Title
st.title("🎮 Tic Tac Toe Pro")

# Winner
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("✨ It's a Draw! ✨")
    else:
        st.success(f"🏆 Player {st.session_state.winner} Wins!")

# Board using columns
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        label = st.session_state.board[idx]
        if cols[col].button(label):
            make_move(idx)

# Reset button
st.button("🔄 Reset Game", on_click=reset_game)
