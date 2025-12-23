import streamlit as st
from data import subjects
from helper import ani_head, side_note, social_links, check_auth, Page, side_note_2



Page()



check_auth()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
           
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)



st.markdown(ani_head(), unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
e1, e2, e3 = st.columns([1, 3, 1])
with e2:
    if st.button("SEARCH", type="primary", use_container_width=True):
        st.switch_page("pages/1_SEARCH.py")


PNG_URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"


st.write("")
st.caption("Quick view")
with st.container(border=True):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.page_link("pages/MATH.py", label=f"![icon]({PNG_URL}) MATH")
    with a2:
        st.page_link("pages/BIOLOGY.py", label=f"![icon]({PNG_URL}) BIOLOGY")
    with a3:
        st.page_link("pages/CHEMISTRY.py", label=f"![icon]({PNG_URL}) CHEMISTRY")
    with a4:
        st.page_link("pages/ICT.py", label=f"![icon]({PNG_URL}) ICT")

st.write("")

st.write("")
st.write("")
b1, b2 =  st.columns(2)
with b1:
    st.write("")
    st.markdown(side_note_2(), unsafe_allow_html=True)
with b2:
    st.write("")
    st.markdown(side_note(), unsafe_allow_html=True)

st.markdown(social_links(), unsafe_allow_html=True)

st.markdown(
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 




























































































