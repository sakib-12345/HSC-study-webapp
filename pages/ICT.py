import streamlit as st
from helper import pdf_view

st.title("ICT Page")

data = {
    "Chapter-01":["https://youtu.be/FycgM1KkpN0?si=ZVJ4P-COyTeJ3DqW", "https://drive.google.com/file/d/1gSU2AdRz6hXbdolO2nNx6O5EseIskkYc/preview"],
    "Chapter-02":["https://youtu.be/pHO9fmTlHyQ?si=MiU30dznvmqC8qVE", "https://drive.google.com/file/d/10K7wKUJIkwS9xC8ImeyvzGHmpyaQoyPy/preview"],
    "Chapter-03":["https://youtu.be/UraWGwzZIU0?si=_k30lzcKBu3jcEqu", "https://drive.google.com/file/d/13uXWR2T7eSxczSYettpbi1fTPOARGHFa/preview"],
    "Chapter-04":["https://youtu.be/zljcRsSi8QU?si=QuZfU7yzQS5-iJNQ", "https://drive.google.com/file/d/1U0zyFNpLez8yEFzuOrH6qgzTVixaGTKW/preview"],
    "Chapter-05":["https://youtu.be/PUGOQ5zJeVk?si=TGsH-CgS_M5-6j0w", "https://drive.google.com/file/d/18T6bA1hYfWfGDkFMSCkaCGAlpJAJ8aX-/preview"],
    "Chapter-06":["https://youtu.be/warR3iHt_Wc?si=Ey2aHqrfdUOh39Gw", "https://drive.google.com/file/d/14OrI-5twzM9y5ECb5GMfZtI5_PnbXZbs/preview"]
}

t1, t2 = st.tabs(["OneShot", "Pdf"])
with t1:
    for chap, url in data.items():
        with st.container(border=True):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.video(url[0])
            with col2:
                st.subheader(chap)

with t2:
    for ch, ur in data.items():
        with st.expander(ch):
            st.markdown(pdf_view(ur[1], unsafe_allow_html=True)
