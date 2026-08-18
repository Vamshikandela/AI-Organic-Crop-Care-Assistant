
import streamlit as st
import base64
from pathlib import Path

from utils.gemini_helper import generate_farming_advice
from utils.youtube_links import generate_youtube_links
from utils.weather import get_weather_advice


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="EcoFarm AI",
    page_icon="🌿",
    layout="centered"
)


# ---------------- BACKGROUND FUNCTION ---------------- #

def add_bg_from_local(image_file):

    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()

    st.markdown(
        """
<style>

/* ===========================
   BACKGROUND
=========================== */

.stApp {{
    background-image: url("data:image/jpg;base64,{encoded_string}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(255,255,255,0.18);
    z-index: -1;
}}

/* ===========================
   MAIN CONTAINER
=========================== */

.block-container {{
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}}


/* ========= INPUT LABEL ========= */

div[data-testid="stWidgetLabel"] p{{
    color: white !important;
    font-size: 22px !important;
    font-weight: bold !important;
}}

/* INPUT BOX */

div[data-testid="stTextInput"] input{{
    background-color: white !important;
    color: black !important;
    font-size: 18px !important;
    font-weight: 600 !important;

    border: 2px solid #43A047 !important;
    border-radius: 12px !important;

    padding: 12px !important;
}}

/* Placeholder */

div[data-testid="stTextInput"] input::placeholder{{
    color: gray !important;
    font-size: 16px !important;
}}



/* ===========================
   BUTTON
=========================== */

.stButton > button {{

    width: 100%;
    height: 50px;

    background: #2E7D32;
    color: white;

    border: none;
    border-radius: 12px;

    font-size: 18px;
    font-weight: bold;

    transition: .3s;
}}

.stButton > button:hover {{
    background: #1B5E20;
}}

/* ===========================
   RESULT BOX
=========================== */

.result-box {{

    background: rgba(255,255,255,.78);

    border-radius: 15px;

    padding: 22px;

    color: black;

    backdrop-filter: blur(8px);
}}

.result-box p,
.result-box li {{

    color: black !important;

    font-size: 17px !important;

    line-height: 1.8;
}}

/* ===========================
   SIDEBAR
=========================== */

section[data-testid="stSidebar"] {{

    background: linear-gradient(
        180deg,
        #14532D,
        #1B5E20,
        #2E7D32
    ) !important;
}}

section[data-testid="stSidebar"] * {{
    color: white !important;
}}

section[data-testid="stSidebar"] div[role="radiogroup"] label {{
    color: white !important;
    font-size: 18px !important;
}}

section[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,.35);
}}

/* ===========================
   MOBILE
=========================== */

@media (max-width:768px) {{

    .block-container {{
        padding-top: 1rem;
    }}

    .block-container h1 {{
        font-size: 32px !important;
    }}

    .block-container h2 {{
        font-size: 22px !important;
    }}

    .block-container h3 {{
        font-size: 20px !important;
    }}

    div[data-testid="stTextInput"] label {{
        font-size: 16px !important;
    }}

    div[data-testid="stTextInput"] input {{
        font-size: 16px !important;
    }}

    .stButton > button {{
        font-size: 16px !important;
    }}
}}

</style>
        """.format(encoded_string=encoded_string),
        unsafe_allow_html=True,
    )


# Load Background Image
add_bg_from_local("farm.jpg")
with st.sidebar:

    st.markdown(
        """
        <h1 style="color:white;text-align:center;">
            ⚙️ Settings
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h3 style="color:white;">
            🌐 Select Language
        </h3>
        """,
        unsafe_allow_html=True,
    )

    lang = st.radio(
        "",
        ["తెలుగు", "English"],
        label_visibility="collapsed",
        index=0,
    )

if lang == "తెలుగు":
    T = {
        "title":" AI Organic Crop Care Assistant",
        "sub":"ఏఐ సేంద్రియ పంట సంరక్షణ సహాయకుడు",
        "crop":"🌾 పంట పేరు","crop_ph":"ఉదా: Tomato / Paddy / Cotton",
        "land":"🧑‍🌾 భూమి పరిమాణం","land_ph":"ఉదా: 2 Acres",
        "season":"🌤️ సీజన్","season_ph":"ఉదా: Summer",
        "loc":"📍 ప్రాంతం","loc_ph":"ఉదా: Guntur",
        "weather":"☁️ వాతావరణ పరిస్థితి","weather_ph":"ఉదా: Heavy Rain",
        "issue":"🐛 సమస్య","issue_ph":"ఉదా: Yellow Leaves",
        "btn":"సలహా పొందండి",
        "result":"🌾 వ్యవసాయ సలహా",
        "weather_title":"🌦️ వాతావరణ సూచనలు",
        "video":"📺 సమస్య పరిష్కార వీడియోలు",
        "organic":"🌱 ఆర్గానిక్ వ్యవసాయ సూచనలు",
        "organic_video":"🌿 ఆర్గానిక్ వ్యవసాయ వీడియోలు",
        "resp":"Telugu"
    }
    organic = """
✅ రసాయన ఎరువులు తగ్గించండి

✅ జీవామృతం ఉపయోగించండి

✅ వర్మీ కంపోస్ట్ వాడండి

✅ వేపనూనె స్ప్రే చేయండి

✅ పంట మార్పిడి చేయండి

✅ మల్చింగ్ చేయండి

✅ నీరు నిల్వ ఉండకుండా చూసుకోండి
"""
    yt_lang="telugu"
else:
    T = {
        "title":" AI Organic Crop Care Assistant",
        "sub":"AI Organic Crop Care Assistant",
        "crop":"🌾 Crop Name","crop_ph":"Example: Tomato",
        "land":"🧑‍🌾 Land Size","land_ph":"Example: 2 Acres",
        "season":"🌤️ Season","season_ph":"Example: Summer",
        "loc":"📍 Location","loc_ph":"Example: Guntur",
        "weather":"☁️ Weather Condition","weather_ph":"Example: Heavy Rain",
        "issue":"🐛 Describe Problem","issue_ph":"Example: Yellow Leaves",
        "btn":"Get Farming Advice",
        "result":"🌾 Farming Advice",
        "weather_title":"🌦️ Weather Suggestions",
        "video":"📺 Recommended Videos",
        "organic":"🌱 Organic Farming Tips",
        "organic_video":"🌿 Organic Farming Videos",
        "resp":"English"
    }
    organic = """
✅ Reduce chemical fertilizers

✅ Use Jeevamrutham

✅ Apply Vermicompost

✅ Spray Neem Oil

✅ Practice Crop Rotation

✅ Use Mulching

✅ Prevent water stagnation
"""
    yt_lang="english"


if lang == "తెలుగు":
    prompt_file = Path("prompts") / "telugu_prompt.txt"
else:
    prompt_file = Path("prompts") / "english_prompt.txt"

with open(prompt_file, "r", encoding="utf-8") as f:
    crop_prompt = f.read()

st.title(T["title"])
st.subheader(T["sub"])

# ---------------- INPUT FIELDS ---------------- #

# Crop Name
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['crop']}</h4>",
    unsafe_allow_html=True
)
crop = st.text_input(
    "",
    placeholder=T["crop_ph"],
    label_visibility="collapsed",
    key="crop"
)

# Land Size
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['land']}</h4>",
    unsafe_allow_html=True
)
land = st.text_input(
    "",
    placeholder=T["land_ph"],
    label_visibility="collapsed",
    key="land"
)

# Season
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['season']}</h4>",
    unsafe_allow_html=True
)
season = st.text_input(
    "",
    placeholder=T["season_ph"],
    label_visibility="collapsed",
    key="season"
)

# Location
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['loc']}</h4>",
    unsafe_allow_html=True
)
location = st.text_input(
    "",
    placeholder=T["loc_ph"],
    label_visibility="collapsed",
    key="location"
)

# Weather
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['weather']}</h4>",
    unsafe_allow_html=True
)
weather = st.text_input(
    "",
    placeholder=T["weather_ph"],
    label_visibility="collapsed",
    key="weather"
)

# Problem
st.markdown(
    f"<h4 style='color:white; font-size:22px; font-weight:bold; margin-bottom:0px;'>{T['issue']}</h4>",
    unsafe_allow_html=True
)
issue = st.text_input(
    "",
    placeholder=T["issue_ph"],
    label_visibility="collapsed",
    key="issue"
)

weather_tip=get_weather_advice(weather,language=T['resp'])

if st.button(T["btn"]):
    prompt=f"""
{crop_prompt}

Farmer Details:
Crop:{crop}
Land Size:{land}
Season:{season}
Location:{location}
Weather:{weather}
Problem:{issue}

Weather Advice:
{weather_tip}

Give complete farming guidance in {T["resp"]}.
"""

    result=generate_farming_advice(prompt)

    st.markdown('<div class="result-box">',unsafe_allow_html=True)
    st.subheader(T["result"])
    st.write(result)

    st.subheader(T["weather_title"])
    st.write(weather_tip)

    st.subheader(T["video"])
    st.markdown(generate_youtube_links(crop,weather,issue))

    st.subheader(T["organic"])
    st.markdown(organic)

    st.subheader(T["organic_video"])
    st.markdown(f"""
1. https://www.youtube.com/results?search_query={crop}+organic+farming+{yt_lang}

2. https://www.youtube.com/results?search_query={crop}+natural+fertilizer+{yt_lang}

3. https://www.youtube.com/results?search_query=jeevamrutham+preparation+{yt_lang}

4. https://www.youtube.com/results?search_query=neem+oil+pest+control+{yt_lang}

5. https://www.youtube.com/results?search_query=vermicompost+preparation+{yt_lang}
""")
    st.markdown("</div>",unsafe_allow_html=True)
