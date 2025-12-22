import streamlit as st
from data import subjects
from helper import ani_head, side_note, social_links, check_auth, Page, side_note_2
from streamlit.components.v1 import html
st.text_input("top_focus", label_visibility="collapsed", key="top_focus_trick")
html("<script>window.parent.window.scrollTo(0,0);</script>", height=0)
st.html('<div id="top"></div>') 


Page()



check_auth()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            /* Prevents browser from jumping to widgets on load */
            * { overflow-anchor: none !important; }
            html { scroll-behavior: smooth; }
            </style>
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)



st.markdown(ani_head(), unsafe_allow_html=True)


PNG_URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"


st.markdown("""
    <style>
    html { 
        scroll-behavior: smooth; 
    }
    
  
    * { 
        overflow-anchor: none !important; 
    }

    .button-container { 
        display: flex; 
        justify-content: center; 
        padding: 40px 0; 
    }
    
    .scroll-button {
        background-color: #c084fc !important;
        color: white !important;
        width: 80%; 
        max-width: 550px;
        padding: 8px 0px !important;
        text-align: center;
        border-radius: 8px;
        font-weight: 500;
        text-decoration: none !important; 
        display: inline-block;
    }
    </style>
    
    <div class="button-container">
        <a href="#search-here" target="_self" class="scroll-button">Search</a>
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


st.write("")
st.write("")
b1, b2 =  st.columns(2)
with b1:
    st.markdown(side_note_2(), unsafe_allow_html=True)
with b2:
    st.markdown(side_note(), unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.html('<div id="search-here"></div>')
st.header("Search here", divider="rainbow")
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







































































