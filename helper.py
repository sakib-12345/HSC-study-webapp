import streamlit as st

def side():
    st.sidebar.markdown("""
    <style>
    .social-footer {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        padding: 20px 0px;
        justify-items: center;
    }
    .social-item {
        text-decoration: none;
        color: #c084fc;
        opacity: 0.8;
    }
    .social-item:hover {
        opacity: 1.0;
        color: #c084fc; /* Streamlit Red accent */
    }
    .social-svg {
        width: 22px;
        height: 22px;
        fill: currentColor;
    }
    </style>
    
    <div class="social-footer">
        <!-- Facebook -->
        <a class="social-item" href="www.facebook.com/sakibhossain.tahmid" target="_blank" title="Facebook">
            <svg class="social-svg" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </a>
        <!-- Instagram -->
        <a class="social-item" href="www.instagram.com/_sakib_000001" target="_blank" title="Instagram">
            <svg class="social-svg" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <!-- X -->
        <a class="social-item" href="x.com/_sakib_00000001" target="_blank" title="X">
            <svg class="social-svg" viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
        </a>
        <!-- GitHub -->
        <a class="social-item" href="github.com/sakib-12345" target="_blank" title="GitHub">
            <svg class="social-svg" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        </a>
        <!-- Email -->
        <a class="social-item" href="mailto:sakibhossaintahmid@gmail.com" title="Email">
            <svg class="social-svg" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
    </div>
""", unsafe_allow_html=True)


def Page():
    
    st.logo("webapp_icon.png", size="large")

    st.set_page_config(
    page_title="Hsc Study",
    page_icon="webapp_icon.png",
    layout="wide"
    )

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
    PNG_URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/webapp_icon.png?raw=true"

    st.title(f"![icon]({PNG_URL}) HSC Study WebApp")
    st.caption("Private Access Required!!!")
    user_code = st.text_input("Enter Invite Code", type="password")
    if st.button("Access App"):
        if user_code == st.secrets.get("INVITE_CODE"):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid invite code.")
    st.markdown("For code contact me :")
    st.markdown("""```bash
sakibhossaintahmid@gmail.com
    """, unsafe_allow_html=True)

    with st.expander("About this app"):
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
           The videos and PDFs in this app are sourced from YouTube and Google Drive.<br><br>
           All content is free and publicly available on the original creators’ platforms.<br><br>
           All video views are counted on the original creators’ YouTube channels, not on this app.
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




























