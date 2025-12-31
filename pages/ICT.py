import streamlit as st
from data import ict
from helper import pdf_view

st.title("ICT Review")

t1, t2 = st.tabs(["OneShot", "Pdf"])
with t1:
    for chap, url in ict.items():
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.video(url[0])
            with col2:
                st.subheader(chap)

with t2:
    for ch, ur in ict.items():
        with st.expander(ch):
            st.markdown(f"[⛶ Full veiw]({ur[1]})", unsafe_allow_html=True)
            st.markdown(pdf_view(ur[1]), unsafe_allow_html=True)












