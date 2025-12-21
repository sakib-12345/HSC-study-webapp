import streamlit as st
from data import math1, math2
from helper import pdf_view

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


st.header("Math Review")

t1, t2 = st.tabs(["OneShot", "Pdf"])

with t1:
    option1 = st.radio("",["1st Paper", "2nd Paper"])
    if option == "1st Paper":
        for chap1, url1 in math1.items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.video(url1[0])
                with col2:
                    st.subheader(chap1)
    else:
        for chap2, url2 in math2.items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.video(url2[0])
                with col2:
                    st.subheader(chap2)
with t2:
    t5, t6 = st.tabs(["1st Paper", "2nd Paper"])
    with t5:
        for ch1, ur1 in math1.items():
            with st.expander(ch1):
                st.markdown(f"[⛶ Full veiw]({ur1[1]})", unsafe_allow_html=True)
                st.markdown(pdf_view(ur1[1]), unsafe_allow_html=True)
    with t6:
        for ch2, ur2 in math2.items():
            with st.expander(ch2):
                st.markdown(f"[⛶ Full veiw]({ur2[1]})", unsafe_allow_html=True)

                st.markdown(pdf_view(ur2[1]), unsafe_allow_html=True)



