import streamlit as st
from data import subjects
from helper import ani_head, side_note, social_links, check_auth, Page

Page()



check_auth()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)



st.markdown(ani_head(), unsafe_allow_html=True)


PNG_URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"


st.markdown(f"""
    <style>
    html {{
        scroll-behavior: smooth;
    }}
    
    .button-container {{
        display: flex;
        justify-content: center;
        padding: 35px 0;

    }}
    
    .scroll-button {{
        background-color: #c084fc !important;
        color: white !important;
         width: 80%;           /* Takes up 80% of width on mobile */
        max-width: 550px;     /* Prevents it from getting too huge on desktop */
        
        padding: 10px 0px !important;
        text-align: center;
        border-radius: 8px;
        font-weight: 500;
        transition: opacity 0.3s ease;
        border: none;
        display: inline-block;
        text-decoration: none !important; 
    }}
    
    .scroll-button:hover {{
        opacity: 0.85;
        color: white !important;
        text-decoration: none !important; 
    }}
    </style>
    
    <div class="button-container">
        <a href="#search-here" target="_self" class="scroll-button">
            Search
        </a>
    </div>
""", unsafe_allow_html=True)
st.caption("Quick view")
with st.container(border=True):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.page_link("pages/MATH.py", label=f"![icon]({PNG_URL}) MATH PAGE")
    with a2:
        st.page_link("pages/BIOLOGY.py", label=f"![icon]({PNG_URL}) BIOLOGY")
    with a3:
        st.page_link("pages/CHEMISTRY.py", label=f"![icon]({PNG_URL}) CHEMISTRY PAGE")
    with a4:
        st.page_link("pages/ICT.py", label=f"![icon]({PNG_URL}) ICT PAGE")



st.markdown(side_note(), unsafe_allow_html=True)
st.subheader("Search here", divider="rainbow")
st.markdown('<div style="color: grey;">Only Math, Biology, Chemistry and ICT for now. Others coming soon....</div>',unsafe_allow_html=True)
sub = st.selectbox("📘 Select subject", subjects.keys())

c1, c2 = st.columns([1, 1])
with c1:
    paper = st.selectbox("📄 Select paper", subjects[sub].keys())
with c2:
    chapter = st.selectbox("Select Chapter",["All Chapters"] + list(subjects[sub][paper].keys()))

if st.button("Search"):
    if chapter == "All Chapters":
        items = subjects[sub][paper].items()
    else:
        items = [(chapter, subjects[sub][paper][chapter])]

    with st.container(height=500):
        st.markdown(f"#### 📚 {sub} - {paper} - {chapter}")
        for chap, links in items:
            with st.container(border=True):
                col1, col2 = st.columns([2, 3])

                with col1:
                    st.video(links[0])

                with col2:
                    st.markdown(f"### {chap}")
                    st.markdown(f"[Open PDF]({links[1]})")
else:
    with st.container(height=500):
        st.markdown('<div style="text-align: center; color: grey;">No search result</div>',unsafe_allow_html=True)


st.markdown(social_links(), unsafe_allow_html=True)

st.markdown(
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 


























































