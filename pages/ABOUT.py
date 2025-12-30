import streamlit as st
from helper import check_auth, Page

Page()



check_auth()

# Hide default Streamlit header/footer
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================
# Page Header
# ==========================
st.markdown("# 📚 HSC Study WebApp")
st.markdown("**Author:** Sakib Hossain Tahmid")

st.markdown(
    """
<p align="center">
  <img src="https://github.com/sakib-12345/HSC-study-webapp/blob/main/webapp_icon.png" alt="App Screenshot" width="200">
</p>
""",
    unsafe_allow_html=True
)

# ==========================
# Overview
# ==========================
st.markdown("## Overview")
st.markdown("""
The **HSC Study WebApp** is a distraction-free platform designed to help HSC students study efficiently. 
It brings together free one-shot classes, video lessons, and PDFs from publicly available platforms into a single, well-organized interface.  

With dedicated pages for each subject and a sidebar for easy navigation, students can access learning materials quickly without getting sidetracked by unrelated videos or content.
""")

# ==========================
# Purpose & Goals
# ==========================
st.markdown("## 🎯 Purpose & Goals")
st.markdown("""
Preparing for HSC exams can be overwhelming due to scattered online resources. This web app aims to:

- Provide **efficient access** to free HSC classes and study materials  
- Offer an **organized workflow** with subject-specific pages  
- Reduce distractions from ads and unrelated content  
- Help students **focus and retain knowledge** effectively  
- Enable learning from **any device with internet access**
""")

# ==========================
# Features
# ==========================
st.markdown("## 📚 Features")

st.markdown("### 👨‍🎓 Student Features")
st.markdown("""
- **Access Free Lessons:** Watch one-shot HSC video lessons for multiple subjects  
- **Download PDFs:** Access study materials, worksheets, and guides alongside video lessons  
- **Search & Navigation:** Quickly find the topic you want using the sidebar or search bar  
- **Distraction-Free Learning:** No ads or unrelated content to interrupt your focus  
- **Invite Code Access (Optional):** Secure private access if needed
""")

st.markdown("### 🛠️ Technical Features")
st.markdown("""
- **Built with Python & Streamlit:** Lightweight, fast, and responsive  
- **Content Aggregation:** Videos and PDFs are linked directly from YouTube and Google Drive  
- **Session-Based Access Control:** Prevent unauthorized access using session state  
- **Easy Deployment:** Works on Streamlit Cloud or any Python-compatible server  
- **Extensible Design:** Add new subjects, videos, or PDFs easily
""")

# ==========================
# Content Policy
# ==========================
st.markdown("## 🌐 Content Policy")
st.markdown("""
- All videos and PDFs are **sourced from public platforms** like YouTube and Google Drive  
- The app **does not host any content**; it only provides an interface to access publicly available resources  
- Video views are counted on the **original creators’ YouTube channels**, ensuring proper recognition  
- Users are encouraged to **support the original content creators**
""")

# ==========================
# Benefits
# ==========================
st.markdown("## 🚀 Benefits")
st.markdown("""
- Study multiple subjects in one unified platform  
- Save time searching for scattered online resources  
- Stay focused and organized while preparing for exams  
- Access content from **any device** with internet  
- Completely free access to high-quality educational materials
""")

# ==========================
# How to Use
# ==========================
st.markdown("## 🛠️ How to Use")
st.markdown("""
1. Open the app in your browser or Streamlit Cloud  
2. Navigate through the sidebar to select the subject you want to study  
3. Watch videos and download PDFs for that subject  
4. Use the search bar to quickly find specific lessons or topics  
5. Optional: Enter an invite code if the app requires private access  
6. Support content creators by watching videos on the original platforms
""")

# ==========================
# FAQ Section
# ==========================
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("Is this app free?"):
    st.markdown("Yes! All content is free to access via this platform, and videos are sourced from publicly available channels.")

with st.expander("Does the app host the videos or PDFs?"):
    st.markdown("No. This app only provides links to videos and PDFs hosted on YouTube and Google Drive. All views are counted on the original platforms.")

with st.expander("Can I use this app on mobile?"):
    st.markdown("Absolutely! The app is responsive and works on mobile devices, tablets, and desktops.")

with st.expander("How can I contribute or suggest content?"):
    st.markdown("You can contact the developer via email: `sakibhossaintahmid@gmail.com`")

# ==========================
# Disclaimer
# ==========================
st.markdown("## 🛡️ Disclaimer")
st.markdown("""
This web app is intended as a **study aid**. All content is publicly available on original platforms.  
The developer does **not claim ownership** of any videos or PDFs, and users are encouraged to support the original creators.
""")

# ==========================
# Contact
# ==========================
st.markdown("## 📧 Contact")
st.markdown("""
For questions, suggestions, or content requests:  
**Email:** sakibhossaintahmid@gmail.com
""")
