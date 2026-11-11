
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Heart AI | Smart Health Dashboard",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# ==========================================
# THEME SELECTION
# ==========================================

if "app_theme" not in st.session_state:
    st.session_state.app_theme = "Light"

if "theme_selector" not in st.session_state:
    st.session_state.theme_selector = st.session_state.app_theme


def change_theme():
    st.session_state.app_theme = st.session_state.theme_selector


top_col1, top_col2 = st.columns([5, 1.5])

with top_col1:
    st.markdown("""
        <div class="brand">
            <div class="brand-icon">❤️</div>
            <div>
                <div class="brand-name">Heart<span>AI</span></div>
                <div class="brand-subtitle">SMART HEALTH DASHBOARD</div>
            </div>
        </div>
    """, unsafe_allow_html=True)



selected_theme = st.session_state.app_theme

# ==========================================
# THEME COLORS
# ==========================================

if selected_theme == "Light":

    colors = {
        "background": "#fff8fa",
        "surface": "#ffffff",
        "surface2": "#fff0f4",
        "text": "#30212b",
        "muted": "#786875",
        "primary": "#e83e67",
        "secondary": "#ff7894",
        "border": "#f5dce4",
        "input": "#ffffff",
        "shadow": "rgba(232, 62, 103, 0.10)",
        "positive_bg": "#fff0f1",
        "positive_text": "#a51d43",
        "negative_bg": "#eafaf2",
        "negative_text": "#087443"
    }

else:

    colors = {
        "background": "#101522",
        "surface": "#1b2435",
        "surface2": "#222d40",
        "text": "#f8fafc",
        "muted": "#b1bdcf",
        "primary": "#fb7185",
        "secondary": "#e84972",
        "border": "#354155",
        "input": "#202b3d",
        "shadow": "rgba(0, 0, 0, 0.25)",
        "positive_bg": "#3b1e2b",
        "positive_text": "#fda4af",
        "negative_bg": "#15372e",
        "negative_text": "#86efac"
    }

# ==========================================
# CUSTOM CSS
# ==========================================

css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: __BACKGROUND__ !important;
    color: __TEXT__ !important;
    transition: background 0.3s ease;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* HIDE STREAMLIT ELEMENTS */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* BRAND HEADER */

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 8px 0 18px 0;
}

.brand-icon {
    width: 52px;
    height: 52px;
    background: linear-gradient(135deg, __PRIMARY__, __SECONDARY__);
    border-radius: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 27px;
    box-shadow: 0 7px 18px __SHADOW__;
    animation: heartbeat 2s infinite;
}

.brand-name {
    font-family: 'Outfit', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: __TEXT__;
    line-height: 1.1;
}

.brand-name span {
    color: __PRIMARY__;
}

.brand-subtitle {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    color: __MUTED__;
    margin-top: 5px;
}

/* ANIMATIONS */

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.12); }
    30% { transform: scale(1); }
    45% { transform: scale(1.08); }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* HERO SECTION */

.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(120deg, __PRIMARY__, __SECONDARY__);
    border-radius: 25px;
    padding: 43px 25px;
    text-align: center;
    color: white;
    margin: 10px 0 28px 0;
    box-shadow: 0 12px 30px __SHADOW__;
    animation: fadeIn 0.7s ease;
}

.hero::before {
    content: "♥";
    position: absolute;
    font-size: 190px;
    opacity: 0.09;
    right: 4%;
    top: -65px;
    transform: rotate(15deg);
}

.hero::after {
    content: "✚";
    position: absolute;
    font-size: 100px;
    opacity: 0.08;
    left: 5%;
    bottom: -35px;
}

.hero-content {
    position: relative;
    z-index: 1;
}

.hero-icon {
    font-size: 43px;
    margin-bottom: 5px;
}

.hero h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 40px;
    font-weight: 800;
    color: white !important;
    margin: 5px 0;
    letter-spacing: -1px;
}

.hero p {
    color: rgba(255,255,255,0.94) !important;
    font-size: 15px;
    margin: 7px 0;
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.35);
    padding: 8px 18px;
    border-radius: 30px;
    margin: 13px 0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

/* INTRODUCTION */

.intro-card {
    background: __SURFACE__;
    border: 1px solid __BORDER__;
    border-radius: 19px;
    padding: 23px 25px;
    margin-bottom: 28px;
    box-shadow: 0 5px 20px __SHADOW__;
    animation: fadeIn 0.8s ease;
}

.intro-title {
    color: __PRIMARY__;
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 9px;
}

.intro-text {
    color: __MUTED__;
    font-size: 14px;
    line-height: 1.8;
    margin: 0;
}

/* SECTION HEADINGS */

.section-heading {
    font-family: 'Outfit', sans-serif;
    font-size: 25px;
    font-weight: 800;
    color: __TEXT__;
    margin: 22px 0 5px 0;
}

.section-subtitle {
    color: __MUTED__;
    font-size: 13px;
    margin-bottom: 18px;
}

/* FORM */

div[data-testid="stForm"] {
    background: __SURFACE__ !important;
    border: 1px solid __BORDER__ !important;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 7px 25px __SHADOW__;
}

.form-heading {
    font-family: 'Outfit', sans-serif;
    color: __PRIMARY__;
    font-size: 19px;
    font-weight: 700;
    margin: 8px 0 16px 0;
}

/* INPUT LABELS */

div[data-testid="stWidgetLabel"] p,
label {
    color: __TEXT__ !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

/* INPUT FIELDS */

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] > div {
    background: __INPUT__ !important;
    border: 1px solid __BORDER__ !important;
    border-radius: 11px !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="select"] div,
div[data-baseweb="textarea"] textarea {
    color: __TEXT__ !important;
}

div[data-baseweb="select"] svg {
    fill: __PRIMARY__ !important;
}

/* THEME DROPDOWN FIX */

div[data-baseweb="select"] > div {
    background-color: __INPUT__ !important;
    border: 1px solid __BORDER__ !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] span {
    color: __TEXT__ !important;
}

/* DROPDOWN POPUP */

div[data-baseweb="popover"] {
    background-color: __SURFACE__ !important;
}

div[data-baseweb="popover"] ul {
    background-color: __SURFACE__ !important;
}

div[data-baseweb="popover"] li {
    background-color: __SURFACE__ !important;
    color: __TEXT__ !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: __SURFACE2__ !important;
    color: __PRIMARY__ !important;
}

div[data-baseweb="popover"] li[aria-selected="true"] {
    background-color: __SURFACE2__ !important;
    color: __PRIMARY__ !important;
}

/* BUTTONS */

.stFormSubmitButton > button,
.stButton > button {
    background: linear-gradient(120deg, __PRIMARY__, __SECONDARY__);
    color: white !important;
    border: none !important;
    border-radius: 13px !important;
    padding: 13px 20px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 17px __SHADOW__;
    transition: all 0.25s ease;
}

.stFormSubmitButton > button:hover,
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 23px __SHADOW__;
}

/* RESULT CARDS */

.result-card {
    border-radius: 22px;
    padding: 32px 22px;
    text-align: center;
    margin: 22px 0;
    animation: fadeIn 0.6s ease;
    border: 1px solid __BORDER__;
}

.result-card h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 27px;
    font-weight: 800;
    margin: 8px 0 12px 0;
}

.result-card p {
    font-size: 14px;
    line-height: 1.8;
}

.result-icon {
    font-size: 43px;
}

.high-risk {
    background: __POSITIVE_BG__ !important;
    color: __POSITIVE_TEXT__ !important;
    border: 1px solid __PRIMARY__;
}

.low-risk {
    background: __NEGATIVE_BG__ !important;
    color: __NEGATIVE_TEXT__ !important;
    border: 1px solid #34a878;
}

/* DISCLAIMER */

.disclaimer {
    background: __SURFACE2__;
    border: 1px dashed __BORDER__;
    border-radius: 17px;
    padding: 20px;
    margin-top: 35px;
    text-align: center;
}

.disclaimer h4 {
    color: __PRIMARY__;
    font-family: 'Outfit', sans-serif;
    font-size: 16px;
    margin-bottom: 8px;
}

.disclaimer p {
    color: __MUTED__;
    font-size: 12px;
    line-height: 1.8;
    margin: 0;
}

/* FOOTER */

.footer {
    text-align: center;
    color: __MUTED__;
    padding: 27px 0 10px 0;
    font-size: 12px;
    line-height: 1.8;
}

/* DIVIDER */

hr {
    border-color: __BORDER__ !important;
}

/* CAPTIONS */

div[data-testid="stCaptionContainer"] {
    color: __MUTED__;
}

/* MOBILE RESPONSIVE */

@media (max-width: 768px) {

    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .hero {
        padding: 32px 15px;
        border-radius: 18px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .hero p {
        font-size: 13px;
    }

    .brand-name {
        font-size: 23px;
    }

    .brand-icon {
        width: 45px;
        height: 45px;
    }

    .section-heading {
        font-size: 21px;
    }

    div[data-testid="stForm"] {
        padding: 17px;
    }

    .intro-card {
        padding: 18px;
    }
}

</style>
"""

# ==========================================
# APPLY THEME COLORS
# ==========================================

replacements = {
    "__BACKGROUND__": colors["background"],
    "__SURFACE__": colors["surface"],
    "__SURFACE2__": colors["surface2"],
    "__TEXT__": colors["text"],
    "__MUTED__": colors["muted"],
    "__PRIMARY__": colors["primary"],
    "__SECONDARY__": colors["secondary"],
    "__BORDER__": colors["border"],
    "__INPUT__": colors["input"],
    "__SHADOW__": colors["shadow"],
    "__POSITIVE_BG__": colors["positive_bg"],
    "__POSITIVE_TEXT__": colors["positive_text"],
    "__NEGATIVE_BG__": colors["negative_bg"],
    "__NEGATIVE_TEXT__": colors["negative_text"]
}

for key, value in replacements.items():
    css = css.replace(key, value)

st.markdown(css, unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="hero-icon">💓 🩺</div>
        <h1>Your Heart, Your Health</h1>
        <p>
            Understand your heart health with the power of Machine Learning.
        </p>
        <div class="hero-tag">
            ✨ AI POWERED HEALTH INSIGHTS
        </div>
        <p>Simple inputs. Smart predictions. Better awareness.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# INTRODUCTION
# ==========================================

st.markdown("""
<div class="intro-card">
    <div class="intro-title">💗 Welcome to Heart AI</div>
    <p class="intro-text">
        Your health journey starts with awareness. Enter the requested
        health information below and let our trained machine learning
        model generate an educational prediction.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MACHINE LEARNING MODEL
# ==========================================

@st.cache_resource
def load_models():
    try:
        model = joblib.load(BASE_DIR / "knn_heart_model.pkl")
        scaler = joblib.load(BASE_DIR / "heart_scaler.pkl")
        expected_columns = joblib.load(BASE_DIR / "heart_columns.pkl")

        return model, scaler, expected_columns, None

    except Exception as e:
        return None, None, None, str(e)


model, scaler, expected_columns, model_error = load_models()

if model is None:

    st.error("Unable to load the machine learning model.")

    st.write(
        "Please check that these three files exist "
        "in the same folder as app.py:"
    )

    st.code(
        "knn_heart_model.pkl\n"
        "heart_scaler.pkl\n"
        "heart_columns.pkl"
    )

    st.stop()

# ==========================================
# HEALTH INFORMATION FORM
# ==========================================

st.markdown(
    '<div class="section-heading">🩺 Health Assessment</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Please provide the information requested below.'
    '</div>',
    unsafe_allow_html=True
)

with st.form("heart_prediction_form"):

    # PERSONAL INFORMATION

    st.markdown(
        '<div class="form-heading">👤 Personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age (years)",
            min_value=1,
            max_value=120,
            value=30,
            help="Enter your age in years."
        )

    with col2:
        sex = st.selectbox(
            "Sex",
            ["M", "F"],
            format_func=lambda x: "Male" if x == "M" else "Female"
        )

    with col3:
        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "ASY", "TA"],
            format_func=lambda x: {
                "ATA": "Atypical Angina",
                "NAP": "Non-Anginal Pain",
                "ASY": "Asymptomatic",
                "TA": "Typical Angina"
            }[x]
        )

    st.markdown("---")

    # MEDICAL INFORMATION

    st.markdown(
        '<div class="form-heading">❤️ Medical Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        resting_bp = st.number_input(
            "Resting Blood Pressure (mmHg)",
            min_value=0,
            max_value=250,
            value=120
        )

    with col2:
        cholesterol = st.number_input(
            "Cholesterol (mg/dL)",
            min_value=0,
            max_value=700,
            value=200
        )

    with col3:
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )

    st.markdown("---")

    # HEART ACTIVITY

    st.markdown(
        '<div class="form-heading">💓 Heart Activity Details</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

    with col2:
        max_hr = st.number_input(
            "Maximum Heart Rate (bpm)",
            min_value=0,
            max_value=250,
            value=150
        )

    with col3:
        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            ["N", "Y"],
            format_func=lambda x: "No" if x == "N" else "Yes"
        )

    col1, col2 = st.columns(2)

    with col1:
        oldpeak = st.number_input(
            "Oldpeak",
            min_value=-5.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
            help="Enter the Oldpeak value from the relevant medical report."
        )

    with col2:
        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

    st.markdown("---")

    submitted = st.form_submit_button(
        "❤️ Generate My Prediction",
        use_container_width=True
    )

# ==========================================
# PREDICTION LOGIC
# ==========================================

if submitted:

    raw_input = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }

    try:

        input_data = pd.DataFrame([raw_input])

        input_data = pd.get_dummies(input_data)

        input_data = input_data.reindex(
            columns=expected_columns,
            fill_value=0
        )

        scaled_input = scaler.transform(input_data)

        prediction = model.predict(scaled_input)[0]

        st.markdown("---")

        st.markdown(
            '<div class="section-heading">'
            '📊 Your Prediction Result'
            '</div>',
            unsafe_allow_html=True
        )

        if prediction == 1:

            st.markdown("""
            <div class="result-card high-risk">
                <div class="result-icon">⚠️</div>
                <h2>Higher Risk Prediction</h2>
                <p>
                    The model identified patterns associated with
                    its positive target class.
                </p>
                <p>
                    Please discuss your health concerns with
                    a qualified healthcare professional.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-card low-risk">
                <div class="result-icon">💚</div>
                <h2>Lower Risk Prediction</h2>
                <p>
                    The model did not identify the positive
                    target pattern in the information provided.
                </p>
                <p>
                    This result does not rule out heart disease.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "Prediction generated using your saved KNN machine learning model."
        )

    except Exception as e:

        st.error(f"Unable to generate prediction: {e}")

# ==========================================
# DISCLAIMER AND FOOTER
# ==========================================

st.markdown("""
<div class="disclaimer">
    <h4>⚕️ Important Health Disclaimer</h4>
    <p>
        Heart AI is an educational machine learning project, not a medical
        diagnostic tool. Its predictions may be inaccurate and must not
        replace a doctor's advice, medical examination, or clinical testing.
        Always consult a qualified healthcare professional about health concerns.
    </p>
</div>

<div class="footer">
    Made with ❤️ using Python, Streamlit & Machine Learning<br>
    <b>Heart AI Dashboard</b> · © 2026
</div>
""", unsafe_allow_html=True)
