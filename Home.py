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

st.write("> study material will be updated soon...")

PNG_URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"

with st.expander("Quick View"):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.page_link("pages/MATH.py", label=f"![icon]({PNG_URL}) MATH PAGE")
    with a2:
        st.page_link("pages/BIOLOGY.py", label=f"![icon]({PNG_URL}) BIOLOGY")
    with a3:
        st.page_link("pages/CHEMISTRY.py", label=f"![icon]({PNG_URL}) CHEMISTRY PAGE")
    with a4:
        st.page_link("pages/ICT.py", label=f"![icon]({PNG_URL}) ICT PAGE")

import streamlit as st

# Custom CSS to center the button and apply your hex color
st.markdown(f"""
    <style>
    /* Centers the button container */
    .stLinkButton {{
        display: flex;
        justify-content: center;
    }}
    /* Styles the button itself */
    .stLinkButton > a {{
        background-color: #c084fc !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        border-radius: 8px !important;
        transition: opacity 0.3s ease;
    }}
    /* Subtle hover effect */
    .stLinkButton > a:hover {{
        opacity: 0.85 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# The Start Button
st.link_button("Start", "https://hsc-study-webapp-by-sakib.streamlit.app/~/+/#search-here")


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



st.markdown(side_note(), unsafe_allow_html=True)
st.markdown(social_links(), unsafe_allow_html=True)

st.markdown(
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 











































