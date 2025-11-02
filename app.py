import streamlit as st
import random
import time

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
if "tick" not in st.session_state:
    st.session_state.tick = 0

# ---------- Move Snake ----------
def move_snake():
    head_x, head_y = st.session_state.snake[-1]
    dir = st.session_state.direction
    if dir == "UP":
        head_y -= 1
    elif dir == "DOWN":
        head_y += 1
    elif dir == "LEFT":
        head_x -= 1
    elif dir == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)
    
    # Collision
    if head_x < 0 or head_x > 9 or head_y < 0 or head_y > 9 or new_head in st.session_state.snake:
        st.session_state.game_over = True
        return
    
    st.session_state.snake.append(new_head)
    
    # Food
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.pop(0)

# ---------- Reset ----------
def reset_game():
    st.session_state.snake = [(5,5)]
    st.session_state.direction = "RIGHT"
    st.session_state.food = (random.randint(0,9), random.randint(0,9))
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.tick = 0

# ---------- Keyboard Input ----------
st.markdown("""
<script>
document.addEventListener('keydown', function(e) {
    if(e.key == 'ArrowUp'){window.parent.postMessage({func:'up'}, '*')}
    if(e.key == 'ArrowDown'){window.parent.postMessage({func:'down'}, '*')}
    if(e.key == 'ArrowLeft'){window.parent.postMessage({func:'left'}, '*')}
    if(e.key == 'ArrowRight'){window.parent.postMessage({func:'right'}, '*')}
});
</script>
""", unsafe_allow_html=True)

def key_input():
    from streamlit.components.v1 import html
    html("""
    <script>
    const send = (dir) => { window.parent.postMessage({func: dir}, '*') }
    window.addEventListener('message', event => {
        if(event.data.func === 'up'){window.parent.stSetValue('direction','UP')}
        if(event.data.func === 'down'){window.parent.stSetValue('direction','DOWN')}
        if(event.data.func === 'left'){window.parent.stSetValue('direction','LEFT')}
        if(event.data.func === 'right'){window.parent.stSetValue('direction','RIGHT')}
    });
    </script>
    """, height=0)

key_input()

# ---------- Auto-move using st_autorefresh ----------
if not st.session_state.game_over:
    st.session_state.tick += 1
    if st.session_state.tick % 1 == 0:  # Adjust speed
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

# ---------- Reset Button ----------
st.button("🔄 Reset Game", on_click=reset_game)

# ---------- Auto-refresh every 0.5s ----------
st_autorefresh = st.experimental_rerun  # simple trick
st.experimental_rerun()



