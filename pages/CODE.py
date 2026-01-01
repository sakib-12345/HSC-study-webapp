import streamlit as st
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
ROOT = Path(__file__).parent.parent  # adjust if this file is inside /pages

EXCLUDE = {".streamlit", "venv", "__pycache__", ".git"}

files = sorted([
    f for f in ROOT.rglob("*")
    if f.is_file()
    and not any(ex in f.parts for ex in EXCLUDE)
    and f.suffix in {".py", ".txt", ".md", ".json", ".yaml", ".yml"}
])
st.write("")
st.write("")
st.write("")
for file in files:
    code = file.read_text(encoding="utf-8", errors="ignore")
    with st.expander(f"### 📄 {file.relative_to(ROOT)}", expanded=False):
        st.code(code, language="python", line_numbers=True)

    
