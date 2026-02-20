# app.py
import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, quran_reader, scholar_tafsir, hadith_specialist, how_to_use

st.set_page_config(
    page_title="NoorAI - Islamic Guidance Platform",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== PROFESSIONAL DARK ISLAMIC THEME ==========
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Poppins:wght@300;400;500;600&display=swap');
    
    /* ===== GLOBAL STYLES ===== */
    * {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0f1c 0%, #1a1f2f 100%);
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu, header, footer, .stDeployButton, .stAppToolbar {
        display: none !important;
    }
    
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* ===== SIDEBAR STYLING ===== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1a2f 0%, #1a2a3f 100%) !important;
        border-right: 2px solid #c4a962;
        box-shadow: 5px 0 30px rgba(0,0,0,0.5);
    }
    
    /* Sidebar Content Wrapper */
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    /* Sidebar Header with Logo */
    .sidebar-header {
        background: linear-gradient(135deg, #1a2a3a, #0f1a2f);
        padding: 2rem 1.5rem;
        margin-bottom: 2rem;
        border-bottom: 2px solid #c4a962;
        text-align: center;
        position: relative;
        overflow: hidden;
        border-radius: 0 0 20px 20px;
    }
    
    .sidebar-header::before {
        content: "﷽";
        position: absolute;
        top: -10px;
        right: -10px;
        font-size: 4rem;
        font-family: 'Amiri', serif;
        color: rgba(196, 169, 98, 0.1);
        transform: rotate(15deg);
    }
    
    .sidebar-logo {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-title {
        color: #d4af37;
        font-size: 2rem;
        font-family: 'Amiri', serif;
        font-weight: 700;
        margin-bottom: 0.25rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .sidebar-subtitle {
        color: #c4a962;
        font-size: 0.85rem;
        letter-spacing: 1px;
        opacity: 0.9;
    }
    
    /* ===== NAVIGATION OPTIONS - LIKE PRAYER TIMES ===== */
    /* Container for all options */
    .nav-options-container {
        background: transparent;
        padding: 0.5rem;
    }
    
    /* Individual option box - EXACTLY LIKE PRAYER TIMES */
    .nav-option-box {
        background: linear-gradient(135deg, #1a2a3a, #152238);
        border: 1px solid #c4a962;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .nav-option-box:hover {
        background: linear-gradient(135deg, #2a3a4a, #1e2a3a);
        border: 1px solid #d4af37;
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(196, 169, 98, 0.2);
    }
    
    .nav-option-box.active {
        background: linear-gradient(135deg, #c4a962, #d4af37);
        border: 1px solid #d4af37;
        box-shadow: 0 4px 15px rgba(196, 169, 98, 0.3);
    }
    
    .nav-option-box.active .nav-option-text {
        color: #0a0f1c;
        font-weight: 600;
    }
    
    .nav-option-box.active .nav-option-icon {
        color: #0a0f1c;
    }
    
    .nav-option-icon {
        font-size: 1.3rem;
        color: #c4a962;
        width: 28px;
        text-align: center;
    }
    
    .nav-option-text {
        font-size: 1rem;
        color: #e8e8e8;
        font-weight: 500;
    }
    
    /* ===== PRAYER WIDGET - EXISTING STYLE ===== */
    .prayer-widget {
        background: linear-gradient(135deg, #1a2a3a, #152238);
        border: 1px solid #c4a962;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .prayer-title {
        color: #d4af37;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        text-align: center;
        font-family: 'Amiri', serif;
    }
    
    .prayer-row {
        display: flex;
        justify-content: space-between;
        padding: 0.6rem 0;
        border-bottom: 1px solid rgba(196, 169, 98, 0.2);
        color: #e8e8e8;
    }
    
    .prayer-row:last-child {
        border-bottom: none;
    }
    
    .prayer-name {
        color: #c4a962;
        font-weight: 500;
    }
    
    .prayer-time {
        color: #e8e8e8;
    }
    
    /* ===== DIVIDER ===== */
    .nav-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c4a962, transparent);
        margin: 2rem 1rem;
    }
    
    /* ===== ISLAMIC DATE ===== */
    .islamic-date {
        background: linear-gradient(135deg, #1a2a3a, #152238);
        padding: 1rem;
        border-radius: 12px;
        margin: 1rem;
        text-align: center;
        border: 1px solid #c4a962;
    }
    
    /* ===== MAIN HEADER ===== */
    .main-header {
        background: linear-gradient(135deg, #1a2a3a, #0f1a2f);
        padding: 2.5rem;
        border-radius: 20px;
        border: 2px solid #c4a962;
        margin: 1rem 1rem 2rem 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: "﷽";
        position: absolute;
        bottom: -20px;
        left: -20px;
        font-size: 8rem;
        font-family: 'Amiri', serif;
        color: rgba(196, 169, 98, 0.05);
        transform: rotate(-10deg);
    }
    
    .main-title {
        color: #d4af37;
        font-size: 3.5rem;
        font-weight: 700;
        font-family: 'Amiri', serif;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        color: #e8e8e8;
        text-align: center;
        font-size: 1.1rem;
        letter-spacing: 1px;
    }
    
    /* ===== CARDS ===== */
    .card {
        background: linear-gradient(135deg, #1a2a3a, #0f1a2f);
        border: 1px solid #c4a962;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .card-title {
        color: #d4af37;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        font-family: 'Amiri', serif;
        border-bottom: 2px solid #c4a962;
        padding-bottom: 0.5rem;
    }
    
    /* ===== ARABIC TEXT ===== */
    .arabic-text {
        font-family: 'Amiri', serif;
        font-size: 2rem;
        color: #d4af37;
        text-align: right;
        line-height: 1.8;
        padding: 1.5rem;
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        border: 1px solid #c4a962;
        margin: 1rem 0;
        direction: rtl;
    }
    
    /* ===== FOOTER ===== */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        background: linear-gradient(135deg, #1a2a3a, #0f1a2f);
        border-top: 2px solid #c4a962;
        color: #e8e8e8;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session states
def init_session_states():
    states = {
        'current_ayah': None,
        'translation': None,
        'messages': [],
        'page': "Home",
        'emotion': None,
        'step': 'emotion'
    }
    for key, value in states.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_states()

# ===== SIDEBAR =====
with st.sidebar:
    # Header with Logo
    st.markdown("""
    <div class='sidebar-header'>
        <div class='sidebar-logo'>🕌</div>
        <div class='sidebar-title'>NoorAI</div>
        <div class='sidebar-subtitle'>نور الذكاء الاصطناعي</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Menu - Custom HTML/CSS instead of option_menu
    st.markdown('<div class="nav-options-container">', unsafe_allow_html=True)
    
    # Home Option
    home_selected = "active" if st.session_state.get('page', 'Home') == 'Home' else ""
    if st.button("🏠 Home", key="nav_home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
    
    # Quran Reader Option
    if st.button("📖 Quran Reader", key="nav_quran", use_container_width=True):
        st.session_state.page = "Quran Reader"
        st.rerun()
    
    # Scholar Tafsir Option
    if st.button("👨‍🏫 Scholar Tafsir", key="nav_scholar", use_container_width=True):
        st.session_state.page = "Scholar Tafsir"
        st.rerun()
    
    # Hadith Specialist Option
    if st.button("📚 Hadith Specialist", key="nav_hadith", use_container_width=True):
        st.session_state.page = "Hadith Specialist"
        st.rerun()
    
    # How to Use Option
    if st.button("ℹ️ How to Use", key="nav_howto", use_container_width=True):
        st.session_state.page = "How to Use"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Decorative Divider
    st.markdown("<div class='nav-divider'></div>", unsafe_allow_html=True)
    
    # Prayer Times Widget - EXACT STYLE
    st.markdown("""
    <div class='prayer-widget'>
        <div class='prayer-title'>🕌 Prayer Times</div>
        <div class='prayer-row'>
            <span class='prayer-name'>Fajr</span>
            <span class='prayer-time'>05:12 AM</span>
        </div>
        <div class='prayer-row'>
            <span class='prayer-name'>Dhuhr</span>
            <span class='prayer-time'>12:30 PM</span>
        </div>
        <div class='prayer-row'>
            <span class='prayer-name'>Asr</span>
            <span class='prayer-time'>03:45 PM</span>
        </div>
        <div class='prayer-row'>
            <span class='prayer-name'>Maghrib</span>
            <span class='prayer-time'>06:15 PM</span>
        </div>
        <div class='prayer-row'>
            <span class='prayer-name'>Isha</span>
            <span class='prayer-time'>07:45 PM</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Islamic Date
    st.markdown("""
    <div class='islamic-date'>
        <p style='color: #d4af37; font-size: 1.2rem; font-family: Amiri;'>15 Sha'aban 1445</p>
        <p style='color: #e8e8e8; font-size: 0.9rem;'>March 21, 2025</p>
    </div>
    """, unsafe_allow_html=True)

# ===== MAIN HEADER =====
st.markdown("""
<div class='main-header'>
    <h1 class='main-title'>🕌 NoorAI</h1>
    <p class='main-subtitle'>Bringing Light to Your Heart with Quranic Guidance</p>
</div>
""", unsafe_allow_html=True)

# ===== PAGE ROUTING =====
try:
    page = st.session_state.get('page', 'Home')
    if page == "Home":
        home.show()
    elif page == "Quran Reader":
        quran_reader.show()
    elif page == "Scholar Tafsir":
        scholar_tafsir.show()
    elif page == "Hadith Specialist":
        hadith_specialist.show()
    elif page == "How to Use":
        how_to_use.show()
except Exception as e:
    st.error(f"Error loading page: {str(e)}")

# ===== FOOTER =====
st.markdown("""
<div class='footer'>
    <p style='font-family: Amiri; color: #d4af37; margin-bottom: 0.5rem;'>وَقُل رَّبِّ زِدْنِي عِلْمًا</p>
    <p>© 2025 NoorAI - Islamic Guidance Platform</p>
</div>
""", unsafe_allow_html=True)