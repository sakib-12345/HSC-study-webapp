


def ani_head():
    return """
<style>
/* From Uiverse.io by kennyotsu */ 
.card {
  --bg-color: #111;
  background-color: var(--bg-color);
  padding: 1rem 2rem;
  border-radius: 1.25rem;
}

.loader {
  color: rgb(124, 124, 124);
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 25px;
  box-sizing: content-box;
  height: 40px;
  padding: 10px 10px;
  display: flex;
  border-radius: 8px;
}

.words {
  overflow: hidden;
  position: relative;
  height: 40px;
}

.words::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    var(--bg-color) 10%,
    transparent 30%,
    transparent 70%,
    var(--bg-color) 90%
  );
  z-index: 20;
}

.word {
  display: block;
  height: 40px;
  line-height: 40px;
  padding-left: 6px;
  color: #956afa;
  animation: spin_4991 7s infinite;
}

/* FIXED FOR 7 WORDS */
@keyframes spin_4991 {
  0%   { transform: translateY(0%); }
  14%  { transform: translateY(-100%); }
  28%  { transform: translateY(-200%); }
  42%  { transform: translateY(-300%); }
  56%  { transform: translateY(-400%); }
  70%  { transform: translateY(-500%); }
  84%  { transform: translateY(-600%); }
  100% { transform: translateY(-600%); }
}
</style>

<div class="card">
  <div class="loader">
    <p>Learn </p>
    <div class="words">
      <span class="word">Bangla</span>
      <span class="word">English</span>
      <span class="word">Maths</span>
      <span class="word">Physics</span>
      <span class="word">Chemistry</span>
      <span class="word">Biology</span>
      <span class="word">ICT</span>
    </div>
  </div>
</div>
    """



def pdf_view(pdf_url):
    return f"""
    <style>
        .pdf-wrapper {{
            position: relative;
            width: 100%;
            height: 400px;
            background: black;
        }}

        .pdf-wrapper iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}

        .fullscreen-btn {{
            position: absolute;
            top: 12px;
            right: 12px;
            z-index: 10000;
            padding: 8px 12px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
        }}
    </style>

    <div class="pdf-wrapper" id="pdfWrapper">
        <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶</button>
        <iframe src="{pdf_url}" allowfullscreen></iframe>
    </div>

    <script>
        function toggleFullscreen() {{
            const wrapper = document.getElementById("pdfWrapper");

            if (!document.fullscreenElement) {{
                wrapper.requestFullscreen().catch(err => {{
                    alert("Fullscreen failed: " + err.message);
                }});
            }} else {{
                document.exitFullscreen();
            }}
        }}
    </script>

    """








