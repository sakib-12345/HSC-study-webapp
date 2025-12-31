import streamlit as st
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

pg = st.navigation(
    {
        "🟣 Main": [home, search, about],
        "🟣 Subjects": [ict_page, math_page, biology_page, chemistry_page],
    }
)

pg.run()


st.markdown(social_links(), unsafe_allow_html=True)

year = datetime.now().year
st.markdown(f"""<p style="text-align:center; font-size:14px; color:gray;">© {year} Sakib Hossain Tahmid. All rights reserved.</p>""", unsafe_allow_html=True)

st.sidebar.markdown("""
<style>
.footer a {
    color: gray;           /* gray text */
    text-decoration: none; /* remove underline */
    margin-left: 10px;
    font-weight: bold;
    transition: color 0.3s;
}

.footer a:hover {
    color: #555; /* darker gray on hover */
}

.footer {
    text-align: left;      /* left-aligned */
    padding: 20px;
    background-color: transparent; /* transparent background */
    line-height: 2.5;
}

.footer .icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    background-color: purple;
    border-radius: 50%;   /* makes it circular */
    margin-right: 10px;
}
</style>

<div class="footer">
    <div><span class="icon"></span><a href="https://www.facebook.com/sakibhossain.tahmid" target="_blank">Facebook</a></div>
    <div><span class="icon"></span><a href="https://www.instagram.com/_sakib_000001" target="_blank">Instagram</a></div>
    <div><span class="icon"></span><a href="https://x.com/_sakib_00000001" target="_blank">X</a></div>
    <div><span class="icon"></span><a href="https://github.com/sakib-12345" target="_blank">GitHub</a></div>
    <div><span class="icon"></span><a href="mailto:sakibhossaintahmid@gmail.com">Email</a></div>
</div>
""", unsafe_allow_html=True)
