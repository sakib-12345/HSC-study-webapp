import streamlit as st
from helper import pdf_view

st.header("Math Review")

m1 = {
    "Chapter-01":["https://youtu.be/KtqyZ-ANMUk?si=6-Ffhn9xd8ucJi1u", "https://drive.google.com/file/d/1sfeRxeinnL8FKsOU-ODgmhv59LDMRP6B/preview"],
    "Chapter-02":["https://youtu.be/JLuKC_yxoWs?si=XxqArKd0FiJaFKSD", "https://drive.google.com/file/d/1c8RxLWqjJh1dQtYBlPlv0qqjUnCkxzHd/preview"],
    "Chapter-03":["https://youtu.be/-WP3xRkTuaM?si=NC-M771PaZR1hxaX", "https://drive.google.com/file/d/1JbOla0UYqXvAvziTDNCapIavtgpt2RjJ/preview"],
    "Chapter-04":["https://youtu.be/1jjTSSpq2pQ?si=2QsrHeNSixstiKgu", "https://drive.google.com/file/d/1rKmSz4VPuWJjUJFaoZfJoCBkk-WivmX7/preview"],
    "Chapter-05":["https://youtu.be/pU_iwduItHs?si=UEWowLNnMGt7Hf7O", "https://drive.google.com/file/d/10XXPq6l-ORAQ_4oEuPc_79l5LZKVqwFM/preview"],
    "Chapter-06":["https://youtu.be/9pwpsJD0tL8?si=kJkg79HRbAmzPqUl", "https://drive.google.com/file/d/1-5b5yvEbB4Y7kygtfOpu64v2ZTar55D6/preview"],
    "Chapter-07":["https://youtu.be/piZLlyz3wbs?si=yAE5xCl5DPOAcU3F", "https://drive.google.com/file/d/1oDH5rBfTsIujRk4o1LnY8LYJpH0z2pdI/preview"],
    "Chapter-08":["https://youtu.be/oYeRl4OQo0Y?si=YQSggT45qemDniSY", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbwCqrOBsE34a4TawgSpB0mmg9ThGSJQkw6dx7Y2bQCA&s"],
    "Chapter-09":["https://youtu.be/DKSpBV109fE?si=e0fy5yPMacniDqKF", "https://drive.google.com/file/d/1O5Xwb6MW8D1vI5nlyUeKlYhy-5ENITMk/preview"],
    "Chapter-10":["https://youtu.be/WXMaW-VdpzA?si=7GI5VWDv0yyarz-X", "https://drive.google.com/file/d/1jawOlQHjIvlHyMr6AlLG8M6AXtXXnluF/preview"]
}

m2 = {
    "Chapter-01":["https://youtu.be/Ak7Y7Yx38uw?si=Q12f1WKwdiPIjFNW", "https://drive.google.com/file/d/1i8rlzm1Cc2PpJmsoM3Y3B8VrvTIHU12q/preview"],
    "Chapter-02":["https://youtu.be/C1OAPt1Q26U?si=M7YXLsN5zFfgFM0N", "https://drive.google.com/file/d/1oAdRLlnw3InYWvmmAQc73efuhK9PhTTM/preview"],
    "Chapter-03":["https://youtu.be/yO-qpIO6rQU?si=PXgQPSxvevMeceO_", "https://drive.google.com/file/d/1ZCZAtuG0ULRDm6nNyz5jH1IMFHpnwyuW/preview"],
    "Chapter-04":["https://youtu.be/KBrLO601OVU?si=9pmaNra_wIbEKJFj", "https://drive.google.com/file/d/1VHGt2JfT99E5bdR4TJFCmSybTpduSNu6/preview"],
    "Chapter-05":["https://youtu.be/g4dmJ7vVY5U?si=Jf4GOy-6a5rpDvsw", "https://drive.google.com/file/d/1vzwomNRQZuXKvxdu_5ToI-pi3r8rzUIs/preview"],
    "Chapter-06":["https://youtu.be/e5UjvcHh87E?si=rwiq0x1Vx9GztwDq", "https://drive.google.com/file/d/1umING1Orn8AmBQ8Z8UowOoj7hYWpcxjA/preview"],
    "Chapter-07":["https://youtu.be/dxU1TOy9jvM?si=7YRUqti24tS3wwo7", "https://drive.google.com/file/d/1PgUxuFP9XKTm33US3On8MST2huJsS2XD/preview"],
    "Chapter-08":["https://youtu.be/n9kLnm_Tqg8?si=YknEfb-kIrB65ash", "https://drive.google.com/file/d/1KaYFo_G9AlpC3xUqwE-CNv2MvWSCHxB-/preview"],
    "Chapter-09":["https://youtu.be/K5ddkgvdVvM?si=lafPaSe_Acc8kZPo", "https://drive.google.com/file/d/1zN0U2AoeFBKvS5yuO_ZvZiS0x_Z--vHe/preview"],
    "Chapter-10":["https://youtu.be/9wdcmsJcHXI?si=rZA2OC8t2falAK2k", "https://drive.google.com/file/d/1X9RcESKPQwbChJAeiFCdqS3EeTBIQOUn/preview"]
}

t1, t2 = st.tabs(["OneShot", "Pdf"])

with t1:
    t3, t4 = st.tabs(["1st Paper", "2nd Paper"])
    with t3:
        for chap1, url1 in m1.items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.video(url1[0])
                with col2:
                    st.subheader(chap1)
    with t4:
        for chap2, url2 in m2.items():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.video(url2[0])
                with col2:
                    st.subheader(chap2)
with t2:
    t5, t6 = st.tabs(["1st Paper", "2nd Paper"])
    with t5:
        for ch1, ur1 in m1.items():
            with st.expander(ch1):
                st.markdown(f"[⛶ Full veiw]({ur1[1]})", unsafe_allow_html=True)
                st.markdown(pdf_view(ur1[1]), unsafe_allow_html=True)
    with t6:
        for ch2, ur2 in m2.items():
            with st.expander(ch2):
                st.markdown(f"[⛶ Full veiw]({ur2[1]})", unsafe_allow_html=True)

                st.markdown(pdf_view(ur2[1]), unsafe_allow_html=True)
