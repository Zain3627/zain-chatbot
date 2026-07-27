import streamlit as st
import time
from main import answer_question

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chat with Zain",
    page_icon="💬",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide default Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* Page background */
    .stApp {
        background-color: #0f1117;
    }

    /* Chat header card */
    .chat-header {
        display: flex;
        align-items: center;
        gap: 14px;
        background: #1a1d27;
        border: 1px solid #2a2d3e;
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 24px;
    }
    .chat-header img {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #4f8ef7;
    }
    .chat-header-info h3 {
        margin: 0;
        color: #e8eaf0;
        font-size: 1.05rem;
        font-weight: 600;
    }
    .chat-header-info p {
        margin: 2px 0 0;
        color: #4caf50;
        font-size: 0.78rem;
    }

    /* Message bubbles */
    .msg-row {
        display: flex;
        margin-bottom: 14px;
        align-items: flex-end;
        gap: 10px;
    }
    .msg-row.user {
        flex-direction: row-reverse;
    }
    .avatar {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        object-fit: cover;
        flex-shrink: 0;
    }
    .avatar-placeholder {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        background: #4f8ef7;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
        flex-shrink: 0;
    }
    .bubble {
        max-width: 72%;
        padding: 10px 15px;
        border-radius: 18px;
        font-size: 0.93rem;
        line-height: 1.5;
        word-wrap: break-word;
    }
    .bubble.bot {
        background: #1e2235;
        color: #dde1f0;
        border-bottom-left-radius: 4px;
        border: 1px solid #2a2d3e;
    }
    .bubble.user {
        background: #4f8ef7;
        color: #ffffff;
        border-bottom-right-radius: 4px;
    }

    /* Input area */
    .stTextInput input {
        background: #1a1d27 !important;
        border: 1px solid #2a2d3e !important;
        border-radius: 24px !important;
        color: #e8eaf0 !important;
        padding: 12px 20px !important;
        font-size: 0.93rem !important;
    }
    .stTextInput input:focus {
        border-color: #4f8ef7 !important;
        box-shadow: 0 0 0 2px rgba(79,142,247,0.2) !important;
    }
    .stButton button {
        background: #4f8ef7 !important;
        color: white !important;
        border: none !important;
        border-radius: 50% !important;
        width: 48px !important;
        height: 48px !important;
        font-size: 1.2rem !important;
        padding: 0 !important;
        transition: background 0.2s;
    }
    .stButton button:hover {
        background: #3a7ae0 !important;
    }
</style>
""", unsafe_allow_html=True)


# ── Response generator (replace with your logic) ──────────────────────────────
def response_generator(user_message: str) -> str:
    time.sleep(0.2)
    return answer_question(user_message)


# ── Session state ──────────────────────────────────────────────────────────────
WELCOME = "Welcome! I am Zain's chat bot. You can call me Zain. How can I help you?"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": WELCOME}]


# ── Load avatar ────────────────────────────────────────────────────────────────
import base64, os

def img_to_b64(path: str) -> str | None:
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

avatar_b64 = img_to_b64("media/profile.jpg")
avatar_tag = (
    f'<img src="data:image/png;base64,{avatar_b64}" class="avatar">'
    if avatar_b64
    else '<div class="avatar-placeholder">Z</div>'
)


# ── Header ─────────────────────────────────────────────────────────────────────
header_img = (
    f'<img src="data:image/png;base64,{avatar_b64}">'
    if avatar_b64
    else '<div style="width:52px;height:52px;border-radius:50%;background:#4f8ef7;display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:1.1rem;">Z</div>'
)

st.markdown(f"""
<div class="chat-header">
    {header_img}
    <div class="chat-header-info">
        <h3>Zain</h3>
        <p>● Online</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Render chat history ────────────────────────────────────────────────────────
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "bot":
            st.markdown(f"""
            <div class="msg-row bot">
                {avatar_tag}
                <div class="bubble bot">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-row user">
                <div class="avatar-placeholder">U</div>
                <div class="bubble user">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)


# ── Handle pending message (runs before input renders) ─────────────────────────
if "pending" in st.session_state and st.session_state.pending:
    text = st.session_state.pending
    st.session_state.pending = None

    st.session_state.messages.append({"role": "user", "content": text})
    reply = response_generator(text)
    st.session_state.messages.append({"role": "bot", "content": reply})
    st.rerun()


# ── Input row ──────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
col_input, col_btn = st.columns([9, 1])

with col_input:
    user_input = st.text_input(
        label="message",
        placeholder="Type a message…",
        label_visibility="collapsed",
        key="chat_input",
    )

with col_btn:
    send = st.button("➤", key="send_btn")


# ── On send: stash the message and rerun ───────────────────────────────────────
if (send or user_input) and user_input.strip():
    st.session_state.pending = user_input.strip()
    st.rerun()