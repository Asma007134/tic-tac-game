import streamlit as st
import random

st.set_page_config(layout="wide", page_title="🐍 Snake Game")

# ---------- Initialize ----------
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
if "direction" not in st.session_state:
    st.session_state.direction = "RIGHT"
if "food" not in st.session_state:
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ---------- Move Snake ----------
def move_snake():
    head_x, head_y = st.session_state.snake[-1]
    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Check collisions
    if head_x < 0 or head_x > 9 or head_y < 0 or head_y > 9 or new_head in st.session_state.snake:
        st.session_state.game_over = True
        return

    st.session_state.snake.append(new_head)

    # Check food
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.pop(0)

# ---------- Reset Game ----------
def reset_game():
    st.session_state.snake = [(5, 5)]
    st.session_state.direction = "RIGHT"
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.score = 0
    st.session_state.game_over = False

# ---------- Controls ----------
cols = st.columns(3)
with cols[0]:
    if st.button("⬅️ Left"):
        if st.session_state.direction != "RIGHT":
            st.session_state.direction = "LEFT"
with cols[1]:
    if st.button("⬆️ Up"):
        if st.session_state.direction != "DOWN":
            st.session_state.direction = "UP"
    if st.button("🔄 Reset"):
        reset_game()
with cols[2]:
    if st.button("➡️ Right"):
        if st.session_state.direction != "LEFT":
            st.session_state.direction = "RIGHT"
    if st.button("⬇️ Down"):
        if st.session_state.direction != "UP":
            st.session_state.direction = "DOWN"

# ---------- Game Tick ----------
if not st.session_state.game_over:
    move_snake()
else:
    st.warning("💀 Game Over! Press Reset.")

# ---------- Display Board ----------
board = [["⬜" for _ in range(10)] for _ in range(10)]
for x, y in st.session_state.snake:
    board[y][x] = "🟩"
fx, fy = st.session_state.food
board[fy][fx] = "🍎"

for row in board:
    st.write("".join(row))

# ---------- Score ----------
st.info(f"Score: {st.session_state.score}")


