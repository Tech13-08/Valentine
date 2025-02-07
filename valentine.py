import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Will You Be My Valentine?", page_icon="❤️")

if not "name" in st.query_params:
    st.query_params["name"] = "Crush"
recipient_name = st.query_params["name"]

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #FFEBEB;
        color: #FF8C8C;
        border: 2px solid #FF5A5F;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF8C8C;
        color: #FFFFFF;
        border-color: #FF8C8C;
    }

    .stImage img {
        border: 2px solid #FF5A5F;
        border-radius: 8px;
    }

    .heart {
        position: absolute;
        font-size: 60px;
        color: #FF5A5F;
        animation: moveHeart 5s infinite ease-in-out;
        pointer-events: none;
    }

    @keyframes moveHeart {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        50% { transform: translateY(200px) rotate(180deg); opacity: 0.7; }
        100% { transform: translateY(0) rotate(360deg); opacity: 1; }
    }

    .heart:nth-child(n) {
        animation-delay: 0s;
    }

    .heart:nth-child(2n) {
        animation-delay: 0.5s;
    }

    .heart:nth-child(3n) {
        animation-delay: 1s;
    }

    .heart:nth-child(6n) {
        animation-delay: 1.5s;
    }

    </style>
    """, unsafe_allow_html=True
)

if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'happy_face_index' not in st.session_state:
    st.session_state.happy_face_index = 0
if 'image_state' not in st.session_state:
    st.session_state.image_state = "normal"
if 'no_disabled' not in st.session_state:
    st.session_state.no_disabled = False
if 'hearts' not in st.session_state:
    st.session_state.hearts = ""
    for _ in range(300):
        top = random.uniform(-18, 70)
        left = random.choice([random.uniform(-35, -5), random.uniform(43, 70)])
        st.session_state.hearts += f'<div class="heart" style="top: {top}vh; left: {left}vw;">❤️</div>'

button_key = f"no_button_{st.session_state.no_count}"

happy_faces = [
    "assets/happy.png",
    "assets/shocked.png",
    "assets/sad.png"
]

if st.session_state.image_state == "normal":
    image = Image.open(happy_faces[st.session_state.happy_face_index])
else:
    st.balloons()
    image = Image.open("assets/yippee.png")

st.markdown(f"""
    <style>
    </style>
    {st.session_state.hearts}
""", unsafe_allow_html=True)

st.title(f"To: {recipient_name}! 💖")
st.subheader("Will you be my Valentine? 😊")

col1, col2 = st.columns([3.5, 1])

st.image(image, width=650)

with col1:
    if st.button("Yes 💘"):
        st.session_state.image_state = "celebrate"
        st.session_state.no_disabled = True
        st.rerun()

with col2:
    if st.session_state.no_count < 2 and not st.session_state.no_disabled:
        if st.button(f"No ❌", key=button_key):
            st.session_state.no_count += 1
            st.session_state.happy_face_index = min(st.session_state.no_count, len(happy_faces) - 1)
            st.session_state.image_state = "normal"
            st.rerun()
    else:
        st.session_state.no_disabled = True
        st.button(f"No ❌", disabled=True)
        st.markdown("""
            <script>
                alert('You cannot press "No" anymore! Please press "Yes" 💖');
            </script>
        """, unsafe_allow_html=True)
