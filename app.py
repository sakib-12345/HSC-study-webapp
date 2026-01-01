import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from helper import social_links, check_auth, Page
Page()



check_auth()


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
           
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)


home = st.Page(
    page="pages/HOME.py",
    title="HOME",
     default=True
)
search = st.Page(
    page="pages/SEARCH.py",
    title="SEARCH"
)
about = st.Page(
    page="pages/ABOUT.py",
    title="ABOUT"
)

ict_page = st.Page(
    page="pages/ICT.py",
    title="ICT",
    
)
math_page = st.Page(
    page="pages/MATH.py",
    title="MATH",
    
)
biology_page = st.Page(
    page="pages/BIOLOGY.py",
    title="BIOLOGY",
)

chemistry_page = st.Page(
    page="pages/CHEMISTRY.py",
    title="CHEMISTRY",
)

physics_page = st.Page(
    page="pages/PHYSICS.py",
    title="PHYSICS",
)
code = st.Page(
    page="pages/CODE.py",
    title="CODE",
)
pg = st.navigation(
    {
        "🟣 Main": [home, search, code, about],
        "🟣 Subjects": [math_page, biology_page, chemistry_page, ict_page, physics_page],
    }
)

pg.run()


st.markdown(social_links(), unsafe_allow_html=True)

year = datetime.now().year
st.markdown(f"""<p style="text-align:center; font-size:14px; color:gray;">© {year} Sakib Hossain Tahmid. All rights reserved.</p>""", unsafe_allow_html=True)

st.sidebar.markdown("""
<style>
.footer {
    text-align: left;              /* left-aligned */
    padding: 10px 5px;             /* smaller padding */
    background-color: transparent; /* transparent background */
    font-size: 12px;               /* smaller font */
    line-height: 1.5;
}

.footer a {
    color: gray;           
    text-decoration: none; 
    margin-right: 15px; 
    font-weight: 500;
    transition: color 0.3s;
}

.footer a:hover {
    color: #555; 
}
</style>

<div class="footer">
    <a href="https://www.facebook.com/sakibhossain.tahmid" target="_blank">Facebook</a>
    <a href="https://www.instagram.com/_sakib_000001" target="_blank">Instagram</a>
    <a href="https://x.com/_sakib_00000001" target="_blank">X</a>
    <a href="https://github.com/sakib-12345" target="_blank">GitHub</a>
    <a href="mailto:sakibhossaintahmid@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p style=\"font-size:12px; color:#c084fc;\">Made by Sakib Hossain Tahmid</p>", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Bored???lets play")
    st.caption("Click game or press **Space**")

    # Advanced Game Engine (Optimized for Sidebar Width)
    flappy_sidebar_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; display: flex; justify-content: center; background: #222; overflow: hidden; }
            #gameCanvas { background: #70c5ce; border: 2px solid #fff; border-radius: 8px; cursor: pointer; }
            #score { position: absolute; top: 10px; left: 10px; color: white; font-family: sans-serif; font-weight: bold; text-shadow: 1px 1px #000; pointer-events: none; }
        </style>
    </head>
    <body>
        <div id="score">Score: 0</div>
        <canvas id="gameCanvas"></canvas>

        <script>
            const canvas = document.getElementById('gameCanvas');
            const ctx = canvas.getContext('2d');
            const scoreEl = document.getElementById('score');

            // Sidebar-friendly dimensions
            canvas.width = 260; 
            canvas.height = 400;

            const GRAVITY = 0.35;
            const FLAP_STRENGTH = -6;
            const PIPE_SPEED = 2;
            const PIPE_SPAWN_RATE = 90;
            const GAP_SIZE = 110;

            let bird = { x: 30, y: 150, w: 30, h: 22, dy: 0, rotation: 0 };
            let pipes = [];
            let score = 0;
            let frameCount = 0;
            let isGameOver = false;

            function reset() {
                bird = { x: 30, y: 150, w: 30, h: 22, dy: 0, rotation: 0 };
                pipes = [];
                score = 0;
                frameCount = 0;
                isGameOver = false;
                scoreEl.innerText = "Score: 0";
            }

            function update() {
                if (isGameOver) return;
                bird.dy += GRAVITY;
                bird.y += bird.dy;
                bird.rotation = Math.min(Math.PI/4, Math.max(-Math.PI/4, bird.dy * 0.1));

                if (bird.y + bird.h > canvas.height || bird.y < 0) isGameOver = true;

                if (frameCount % PIPE_SPAWN_RATE === 0) {
                    let h = Math.floor(Math.random() * (canvas.height - GAP_SIZE - 60)) + 30;
                    pipes.push({ x: canvas.width, top: h, passed: false });
                }

                for (let i = pipes.length - 1; i >= 0; i--) {
                    let p = pipes[i];
                    p.x -= PIPE_SPEED;
                    if (bird.x + bird.w > p.x && bird.x < p.x + 40) {
                        if (bird.y < p.top || bird.y + bird.h > p.top + GAP_SIZE) isGameOver = true;
                    }
                    if (!p.passed && p.x + 40 < bird.x) {
                        p.passed = true;
                        score++;
                        scoreEl.innerText = "Score: " + score;
                    }
                    if (p.x < -50) pipes.splice(i, 1);
                }
                frameCount++;
            }

            function draw() {
                ctx.fillStyle = "#70c5ce";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = "#2e8b57";
                pipes.forEach(p => {
                    ctx.fillRect(p.x, 0, 40, p.top);
                    ctx.fillRect(p.x, p.top + GAP_SIZE, 40, canvas.height);
                });
                ctx.save();
                ctx.translate(bird.x + bird.w/2, bird.y + bird.h/2);
                ctx.rotate(bird.rotation);
                ctx.font = "24px Arial";
                ctx.fillText("🐦", -12, 10);
                ctx.restore();

                if (isGameOver) {
                    ctx.fillStyle = "rgba(0,0,0,0.6)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = "white";
                    ctx.textAlign = "center";
                    ctx.font = "20px Arial";
                    ctx.fillText("GAME OVER", canvas.width/2, canvas.height/2);
                    ctx.font = "12px Arial";
                    ctx.fillText("Click to Restart", canvas.width/2, canvas.height/2 + 30);
                }
            }

            function loop() {
                update(); draw(); requestAnimationFrame(loop);
            }

            const flap = () => isGameOver ? reset() : bird.dy = FLAP_STRENGTH;
            window.addEventListener('keydown', e => { if(e.code==='Space') flap(); });
            canvas.addEventListener('mousedown', flap);
            loop();
        </script>
    </body>
    </html>
    """

    # Width matches canvas.width plus small buffer
    components.html(flappy_sidebar_html, height=450)


