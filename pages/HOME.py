import streamlit as st
import streamlit.components.v1 as components
import sqlite3
from datetime import datetime
from data import subjects
from helper import ani_head, side_note, side_note_2




st.markdown(ani_head(), unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
e1, e2, e3 = st.columns([1, 3, 1])
with e2:
    if st.button("Search", type="primary", use_container_width=True):
        st.switch_page("pages/SEARCH.py")
    if st.button("About", use_container_width=True):
        st.switch_page("pages/ABOUT.py")

URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"


st.write("")
st.caption("Quick view")
with st.container(border=True):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.page_link("pages/MATH.py", label=f"![icon]({URL}) MATH")
    with a2:
        st.page_link("pages/BIOLOGY.py", label=f"![icon]({URL}) BIOLOGY")
    with a3:
        st.page_link("pages/CHEMISTRY.py", label=f"![icon]({URL}) CHEMISTRY")
    with a4:
        st.page_link("pages/ICT.py", label=f"![icon]({URL}) ICT")


st.write("")
st.write("")
b1, b2 =  st.columns(2)
with b1:
    st.write("")
    st.write("")
    st.markdown(side_note_2(), unsafe_allow_html=True)
with b2:
    st.write("")
    st.write("")
    st.markdown(side_note(), unsafe_allow_html=True)




# ---------- DATABASE ----------
conn = sqlite3.connect("messages.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    name TEXT,
    message TEXT
)
""")
conn.commit()

# ---------- URL PARAMS ----------
params = st.query_params
is_admin = params.get("admin", [""]) == st.secrets["ADMIN_KEY"]
st.write("")
st.write("")
st.write("")
st.write("#### Any Suggestion for videos?")
with st.form("message_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Suggestion", height=60)
    submit = st.form_submit_button("Send")

if submit:
    if name and message:
        
        c.execute(
            "INSERT INTO messages (timestamp, name, message) VALUES (?, ?, ?)",
            (datetime.now().isoformat(timespec="seconds"), name, message)
        )
        conn.commit()
        st.success("✅ Message sent!")
    else:
        st.error("Please fill in all fields.")

# ---------- ADMIN VIEW ----------
if is_admin:
    st.divider()
    st.subheader("📬 Admin Messages")

    rows = c.execute(
        "SELECT id, timestamp, name, message FROM messages ORDER BY id DESC"
    ).fetchall()
    if st.button("🔄 Refresh Messages"):
        st.rerun()
    if not rows:
        st.info("No messages yet.")
    else:
        with st.container(height=300):
            for msg_id, ts, name, msg in rows:
                st.markdown(f"**{name}**  \n🕒 {ts}")
                st.write(msg)

                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("🗑️ Delete", key=f"del_{msg_id}"):
                        c.execute("DELETE FROM messages WHERE id = ?", (msg_id,))
                        conn.commit()
                        st.rerun()

                st.divider()




st.subheader("Bored???lets play")
st.caption("Click game or press **Space**")
flappy_main_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; display: flex; justify-content: center; background: #222; overflow: hidden; border-radius: 15px; }
        #gameCanvas { background: #70c5ce; border: 5px solid #fff; border-radius: 15px; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        #score { position: absolute; top: 20px; color: white; font-family: 'Arial Black', sans-serif; font-size: 32px; text-shadow: 3px 3px #000; pointer-events: none; }
    </style>
</head>
<body>
    <div id="score">0</div>
    <canvas id="gameCanvas"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreEl = document.getElementById('score');

        // Main Page Dimensions
        canvas.width = 500; 
        canvas.height = 500;

        // Physics Constants
        const GRAVITY = 0.35;
        const FLAP_STRENGTH = -6.5;
        const PIPE_SPEED = 2.5;
        const PIPE_SPAWN_RATE = 100;
        const GAP_SIZE = 130;

        let bird = { x: 80, y: 200, w: 34, h: 24, dy: 0, rotation: 0 };
        let pipes = [];
        let score = 0;
        let frameCount = 0;
        let isGameOver = false;

        function reset() {
            bird = { x: 80, y: 200, w: 34, h: 24, dy: 0, rotation: 0 };
            pipes = [];
            score = 0;
            frameCount = 0;
            isGameOver = false;
            scoreEl.innerText = "0";
        }

        function update() {
            if (isGameOver) return;
            
            // Bird Movement
            bird.dy += GRAVITY;
            bird.y += bird.dy;
            bird.rotation = Math.min(Math.PI/4, Math.max(-Math.PI/4, bird.dy * 0.1));

            // Ground/Ceiling Collision
            if (bird.y + bird.h > canvas.height || bird.y < 0) isGameOver = true;

            // Pipe Logic
            if (frameCount % PIPE_SPAWN_RATE === 0) {
                let h = Math.floor(Math.random() * (canvas.height - GAP_SIZE - 100)) + 50;
                pipes.push({ x: canvas.width, top: h, passed: false });
            }

            for (let i = pipes.length - 1; i >= 0; i--) {
                let p = pipes[i];
                p.x -= PIPE_SPEED;

                // Pipe Collision
                if (bird.x + bird.w > p.x && bird.x < p.x + 55) {
                    if (bird.y < p.top || bird.y + bird.h > p.top + GAP_SIZE) isGameOver = true;
                }

                // Score Counting
                if (!p.passed && p.x + 55 < bird.x) {
                    p.passed = true;
                    score++;
                    scoreEl.innerText = score;
                }

                if (p.x < -60) pipes.splice(i, 1);
            }
            frameCount++;
        }

        function draw() {
            // Draw Sky
            ctx.fillStyle = "#70c5ce";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw Pipes
            ctx.fillStyle = "#2e8b57";
            ctx.strokeStyle = "#1b4d31";
            ctx.lineWidth = 2;
            pipes.forEach(p => {
                ctx.fillRect(p.x, 0, 55, p.top);
                ctx.strokeRect(p.x, 0, 55, p.top);
                ctx.fillRect(p.x, p.top + GAP_SIZE, 55, canvas.height);
                ctx.strokeRect(p.x, p.top + GAP_SIZE, 55, canvas.height);
            });

            // Draw Bird
            ctx.save();
            ctx.translate(bird.x + bird.w/2, bird.y + bird.h/2);
            ctx.rotate(bird.rotation);
            ctx.font = "30px Arial";
            ctx.fillText("🐦", -18, 12);
            ctx.restore();

            if (isGameOver) {
                ctx.fillStyle = "rgba(0,0,0,0.7)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = "white";
                ctx.textAlign = "center";
                ctx.font = "bold 30px sans-serif";
                ctx.fillText("GAME OVER", canvas.width/2, canvas.height/2);
                ctx.font = "18px sans-serif";
                ctx.fillText("Click to Play Again", canvas.width/2, canvas.height/2 + 40);
            }
        }

        function gameLoop() {
            update(); draw(); requestAnimationFrame(gameLoop);
        }

        const handleInput = (e) => {
            if (e.code === 'Space' || e.type === 'mousedown') {
                if (isGameOver) reset();
                else bird.dy = FLAP_STRENGTH;
            }
        };

        window.addEventListener('keydown', handleInput);
        canvas.addEventListener('mousedown', handleInput);
        gameLoop();
    </script>
</body>
</html>
"""

# Render component in main page
components.html(flappy_main_html, height=550)












































































































