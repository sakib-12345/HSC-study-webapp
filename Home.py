import streamlit as st
from helper import ani_head, side_note, social_links

st.markdown(ani_head(), unsafe_allow_html=True)

st.write("> study material will be updated soon...")

with st.expander("Quick View"):
    st.markdown("[ICT PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/ICT#ict-review)")
    st.markdown("[MATH PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/MATH#math-review)")

m = "The video and pdf in this app are pulled from youtube and google drive.<br> They are free content and available in their owner's youtube channel and drive."
st.markdown(side_note("About this app", m), unsafe_allow_html=True)
st.markdown(social_links(), unsafe_allow_html=True)









