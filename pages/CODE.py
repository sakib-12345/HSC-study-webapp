import streamlit as st
from pathlib import Path

st.title("App Source Code")

ROOT = Path(__file__).parent

# Collect python files (exclude .streamlit, venv, etc.)
files = sorted([
    f for f in ROOT.rglob("*.py")
    if "venv" not in str(f)
    and ".streamlit" not in str(f)
])

file_paths = {str(f.relative_to(ROOT)): f for f in files}

selected = st.selectbox("Select a file", file_paths.keys())

code = file_paths[selected].read_text(encoding="utf-8")

st.code(code, language="python")
