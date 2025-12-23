import streamlit as st
import sqlite3
from datetime import datetime
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



st.markdown(ani_head(), unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
e1, e2, e3 = st.columns([1, 3, 1])
with e2:
    if st.button("SEARCH", type="primary", use_container_width=True):
        st.switch_page("pages/1_SEARCH.py")


URL = "https://github.com/sakib-12345/HSC-study-webapp/blob/main/click.png?raw=true"


st.write("")
st.caption("Quick view")
with st.container(border=True):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.page_link("pages/MATH.py", label=f"![icon]({URL}) MATH")
    with a2:
        st.page_link("pages/BIOLOGY.py", label=f"![icon]({URL}) BIOLOGY")
    with a3:
        st.page_link("pages/CHEMISTRY.py", label=f"![icon]({URL}) CHEMISTRY")
    with a4:
        st.page_link("pages/ICT.py", label=f"![icon]({URL}) ICT")

st.write("")

st.write("")
st.write("")
b1, b2 =  st.columns(2)
with b1:
    st.write("")
    st.markdown(side_note_2(), unsafe_allow_html=True)
with b2:
    st.write("")
    st.markdown(side_note(), unsafe_allow_html=True)

social_links()
ADMIN_KEY = st.secrets.get("ADMIN_KEY", "changeme")

# ---------- DATABASE ----------
conn = sqlite3.connect("messages.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    name TEXT,
    message TEXT
)
""")
conn.commit()

# ---------- URL PARAMS ----------
params = st.experimental_get_query_params()
is_admin = params.get("admin", [""])[0] == ADMIN_KEY

st.write("#### Any Suggestion for videos?")
with st.sidebar.form("message_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

if submit:
    if name and message:
        c.execute(
            "INSERT INTO messages (timestamp, name, message) VALUES (?, ?, ?)",
            (datetime.now().isoformat(timespec="seconds"), name, message)
        )
        conn.commit()
        st.sidebar.success("✅ Message sent!")
    else:
        st.sidebar.error("Please fill in all fields.")

# ---------- ADMIN VIEW ----------
if is_admin:
    st.divider()
    st.subheader("📬 Admin Messages")

    rows = c.execute(
        "SELECT id, timestamp, name, message FROM messages ORDER BY id DESC"
    ).fetchall()

    if not rows:
        st.info("No messages yet.")
    else:
        for msg_id, ts, name, msg in rows:
            st.markdown(f"**{name}**  \n🕒 {ts}")
            st.write(msg)

            col1, col2 = st.columns([1, 5])
            with col1:
                if st.button("🗑️ Delete", key=f"del_{msg_id}"):
                    c.execute("DELETE FROM messages WHERE id = ?", (msg_id,))
                    conn.commit()
                    st.rerun()

            st.divider()

































































































