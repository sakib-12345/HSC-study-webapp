import streamlit as st
from pathlib import Path

st.title("Project Source Code")

st.markdown("OPEN IN GITHUB [CLICK HERE](https://github.com/sakib-12345/HSC-study-webapp)", unsafe_allow_html=True)

ROOT = Path(__file__).parent.parent  # adjust if this file is inside /pages

EXCLUDE = {".streamlit", "venv", "__pycache__", ".git"}

files = sorted([
    f for f in ROOT.rglob("*")
    if f.is_file()
    and not any(ex in f.parts for ex in EXCLUDE)
    and f.suffix in {".py", ".txt", ".md", ".json", ".yaml", ".yml"}
])

for file in files:
    st.markdown(f"### 📄 {file.relative_to(ROOT)}")
    code = file.read_text(encoding="utf-8", errors="ignore")
    st.code(code, language=file.suffix.lstrip("."), line_numbers=True)
    st.write("")
    st.write("")
    st.write("")
    
