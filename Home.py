import streamlit as st
from helper import ani_head

st.header("Home")
ani_head()

st.write("> study material will be updated soon...")

with st.expander("Quick View"):
    st.markdown("[ICT PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/ICT#ict-review)")
    st.markdown("[MATH PAGE](https://hsc-study-webapp-by-sakib.streamlit.app/MATH#math-review)")





