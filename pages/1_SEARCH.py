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


st.header("Search here", divider="violet")
st.markdown('<div style="color: grey;">Only Math, Biology, Chemistry and ICT for now. Others coming soon....</div>',unsafe_allow_html=True)
sub = st.selectbox("📘 Select subject", subjects.keys())

c1, c2 = st.columns([1, 1])
with c1:
    paper = st.selectbox("📄 Select paper", subjects[sub].keys())
with c2:
    chapter = st.selectbox("Select Chapter",["All Chapters"] + list(subjects[sub][paper].keys()))

if st.button("Search"):
    if chapter == "All Chapters":
        items = subjects[sub][paper].items()
    else:
        items = [(chapter, subjects[sub][paper][chapter])]

    with st.container(height=500):
        st.markdown(f"#### 📚 {sub} - {paper} - {chapter}")
        for chap, links in items:
            with st.container(border=True):
                col1, col2 = st.columns([2, 3])

                with col1:
                    st.video(links[0])

                with col2:
                    st.markdown(f"### {chap}")
                    st.markdown(f"[Open PDF]({links[1]})")
else:
    with st.container(height=500):
        st.markdown('<div style="text-align: center; color: grey;">No search result</div>',unsafe_allow_html=True)



st.markdown(social_links(), unsafe_allow_html=True)

st.markdown(
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 

