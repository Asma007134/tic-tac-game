import streamlit as st

# Initialize the game board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Function to check for a winner
def check_winner(board):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return board[pos[0]]
    if "" not in board:
        return "Draw"
    return None

# Function to handle a move
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

st.title("Tic Tac Toe Game")

# Display winner
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f"Player {st.session_state.winner} wins!")

# Display the game board
for i in range(0, 9, 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if col.button(st.session_state.board[idx], key=idx):
            make_move(idx)

# Reset button
st.button("Reset Game", on_click=reset_game)
