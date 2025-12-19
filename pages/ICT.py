import streamlit as st


st.title("ICT Page")

data = {
    "Chapter-01":"https://youtu.be/FycgM1KkpN0?si=ZVJ4P-COyTeJ3DqW",
    "Chapter-02":"https://youtu.be/pHO9fmTlHyQ?si=MiU30dznvmqC8qVE",
    "Chapter-03":"https://youtu.be/UraWGwzZIU0?si=_k30lzcKBu3jcEqu",
    "Chapter-04":"https://youtu.be/zljcRsSi8QU?si=QuZfU7yzQS5-iJNQ",
    "Chapter-05":"https://youtu.be/PUGOQ5zJeVk?si=TGsH-CgS_M5-6j0w",
    "Chapter-06":"https://youtu.be/warR3iHt_Wc?si=Ey2aHqrfdUOh39Gw"
}
for chap, url in data.items():
    with st.container(border=True):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.video(url)
        with col2:

            st.subheader(chap)
