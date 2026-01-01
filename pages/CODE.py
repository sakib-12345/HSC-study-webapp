import streamlit as st
import pandas as pd
from data import subjects
from pathlib import Path

st.title("Project Source Code")

st.markdown("OPEN IN GITHUB [CLICK HERE](https://github.com/sakib-12345/HSC-study-webapp)", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("### 🔧 File Structure")
st.markdown("""
```
HSC-study-webapp/
├── .streamlit/
│   └── config.toml
├── License
├── README.md
├── app.py
├── click.png
├── data.py
├── helper.py
├── pages/
│   ├── ABOUT.py
│   ├── BIOLOGY.py
│   ├── CHEMISTRY.py
│   ├── CODE.py
│   ├── HOME.py
│   ├── ICT.py
│   ├── MATH.py
│   ├── PHYSICS.py
│   └── SEARCH.py
├── requirements.txt
└── webapp_icon.png
```
""", unsafe_allow_html=True)

data = []

for subject, papers in subjects.items():
    for paper_name, chapters in papers.items():
        for chapter_name, links in chapters.items():
            youtube_link = links[0] if len(links) > 0 else ""
            drive_link = links[1] if len(links) > 1 else ""
            data.append([subject, paper_name, chapter_name, youtube_link, drive_link])

df_master = pd.DataFrame(data, columns=["Subject", "Paper", "Chapter", "YouTube Link", "Drive Link"])

with st.expander("Video and Pdf Links"):
    st.dataframe(df_master)
    
ROOT = Path(__file__).parent.parent  # adjust if this file is inside /pages

EXCLUDE = {".streamlit", "venv", "__pycache__", ".git"}

files = sorted([
    f for f in ROOT.rglob("*")
    if f.is_file()
    and not any(ex in f.parts for ex in EXCLUDE)
    and f.suffix in {".py", ".txt", ".md", ".json", ".yaml", ".yml",".toml"}
])
st.write("")
st.write("")
st.write("### Code")
st.write("")
for file in files:
    code = file.read_text(encoding="utf-8", errors="ignore")
    with st.expander(f"📄 {file.relative_to(ROOT)}", expanded=False):
        st.code(code, language="python", line_numbers=True)

with st.expander("🖼️ Used Images", expanded=False):
    st.image("click.png", caption="click.png")
    st.image("webapp_icon.png", caption="webapp_icon.png")
with st.expander("⚙ .streamlit/config.toml", expanded=False):
    st.code("""
    [theme]
    base="dark"
    primaryColor="#c084fc"              
    """, language="python", line_numbers=True)
st.write("")
st.write("")
st.write("### Or, Clone and Run")
st.code("git clone https://github.com/sakib-12345/HSC-study-webapp.git")
