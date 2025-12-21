import streamlit as st
from data import botany, zoology, check_auth


st.set_page_config(
    page_title="Hsc Study",
    page_icon="📈",
    layout="wide"
)

check_auth()
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)


st.header("Biology Review")

t3, t4 = st.tabs(["Botany", "Zoology"])
with t3:
    for chap1, url1 in botany.items():
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.video(url1[0])
            with col2:
                st.subheader(chap1)
 
with t4:
    for chap2, url2 in zoology.items():
         with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                 st.video(url2[0])
            with col2:
                st.subheader(chap2)
