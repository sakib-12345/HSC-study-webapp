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


