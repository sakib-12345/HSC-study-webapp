import streamlit as st
from helper import ani_head, side_note, social_links


st.set_page_config(
    page_title="Hsc Study",
    page_icon="📈",
    layout="wide"
)
 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
    
st.markdown(hide_st_style, unsafe_allow_html=True)



st.markdown(ani_head(), unsafe_allow_html=True)

st.write("> study material will be updated soon...")

with st.expander("Quick View"):
    st.markdown("[ICT PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/ICT#ict-review)")
    st.markdown("[MATH PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/MATH#math-review)")

st.markdown(side_note(), unsafe_allow_html=True)
st.markdown(social_links(), unsafe_allow_html=True)

st.markdown(
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 












