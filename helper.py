import streamlit as st

def check_auth():
    # 1. Skip if login is disabled in secrets.toml
    if not st.secrets.get("LOGIN_ENABLED", False):
        return True

    # 2. Return True if already authenticated in this session
    if st.session_state.get("authenticated", False):
        return True

    # 3. Otherwise, show the invite code form
    
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.title("📈 HSC Study WebApp")
    st.caption("Private Access Required!!!")
    user_code = st.text_input("Enter Invite Code", type="password")
    if st.button("Access App"):
        if user_code == st.secrets.get("INVITE_CODE"):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid invite code.")
    st.markdown("For code contact me on ✉:")
    st.markdown("""```bash
sakibhossaintahmid@gmail.com
    """, unsafe_allow_html=True)

    with st.expander("About this app")
        st.write("*This web app helps you study without getting distracted by unnecessary YouTube videos. You can easily access free one-shot classes and their PDFs in one place.*")
    
    # 4. Stop execution of the rest of the page if not authenticated
    st.stop()



def social_links():
    return """
    <style>
        .social-icons {
            text-align: center;
            margin-top: 40px;
            color: #c084fc;
        }

        .social-icons a {
            text-decoration: none !important;
            margin: 0 10px;
            font-size: 30px;
            display: inline-block;
            color: inherit !important; /* force child i to use its color */
        }

        

        /* Hover glitch animation */
        .social-icons a:hover {
            animation: glitch 0.3s infinite;
        }

        
        /* Contact us heading */
        .contact-heading {
            text-align: center;
            font-size: 27px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #c084fc;
        }
        @keyframes glitch {
            0% { transform: translate(0px, 0px); text-shadow: 2px 2px #0ff, -2px -2px #f0f; }
            20% { transform: translate(-2px, 1px); text-shadow: -2px 2px #0ff, 2px -2px #f0f; }
            40% { transform: translate(2px, -1px); text-shadow: 2px -2px #0ff, -2px 2px #f0f; }
            60% { transform: translate(-1px, 2px); text-shadow: -2px 2px #0ff, 2px -2px #f0f; }
            80% { transform: translate(1px, -2px); text-shadow: 2px -2px #0ff, -2px 2px #f0f; }
            100% { transform: translate(0px, 0px); text-shadow: 2px 2px #0ff, -2px -2px #f0f; }
        }
    </style>
    <div class="social-icons">
    <div class="contact-heading">Contact Us:</div>
        <a class='fb' href='https://www.facebook.com/sakibhossain.tahmid' target='_blank'>
            <i class='fab fa-facebook'></i> 
        </a> 
        <a class='insta' href='https://www.instagram.com/_sakib_000001' target='_blank'>
            <i class='fab fa-instagram'></i> 
        </a> 
        <a class='github' href='https://github.com/sakib-12345' target='_blank'>
            <i class='fab fa-github'></i> 
        </a> 
        <a class='email' href='mailto:sakibhossaintahmid@gmail.com'>
            <i class='fas fa-envelope'></i> 
        </a>
    </div>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """


def side_note():
    return """
        <style>
        .about-title-dark {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 12px;
            color: #c084fc;
        }

        .about-box-dark {
            padding: 14px 16px;
            background: #1e1e2e;
            border-left: 4px solid #a855f7;
            border-radius: 10px;
            font-size: 14px;
            line-height: 1.6;
            color: #e9d5ff;
            box-shadow: 0 0 8px rgba(168, 85, 247, 0.15);
        }
        </style>
        
        <div class="about-title-dark">About this app</div>

        <div class="about-box-dark">
            The video and pdf in this app are pulled from youtube and google drive.<br> <br>
            They are free content and available in their owner's youtube channel and drive.
        </div>

        """
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
















