# app.py
import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, quran_reader, scholar_tafsir, hadith_specialist, how_to_use
from datetime import datetime
import calendar

st.set_page_config(
    page_title="NoorAI - Islamic Guidance Platform",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="collapsed"
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
    
    /* Smooth scrolling for the whole page */
    html {
        scroll-behavior: smooth;
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu, footer, .stDeployButton, .stAppToolbar {
        display: none !important;
    }
    
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    header[data-testid="stHeader"] {
        background: transparent !important;
        border-bottom: none !important;
        box-shadow: none !important;
        height: 0 !important;
    }
    
    /* Completely hide sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Main content - full width centered */
    .main .block-container {
        padding: 2rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        width: 100% !important;
        scroll-margin-top: 100px;
    }
    
    /* Page sections with scroll targets */
    .page-section {
        scroll-margin-top: 100px;
        transition: opacity 0.3s ease;
    }
    
    /* ===== TOP NAVIGATION BAR ===== */
    .top-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #1a2a3a, #152238);
        border: 1px solid #c4a962;
        border-radius: 50px;
        padding: 0.5rem 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        flex-wrap: wrap;
        position: sticky;
        top: 10px;
        z-index: 1000;
        backdrop-filter: blur(10px);
    }
    
    .nav-links {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    
    .nav-link {
        background: transparent;
        border: 1px solid transparent;
        border-radius: 30px;
        padding: 0.6rem 1.2rem;
        color: #e8e8e8;
        font-size: 0.95rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
    }
    
    .nav-link:hover {
        border-color: #c4a962;
        background: rgba(196, 169, 98, 0.1);
        transform: translateY(-2px);
    }
    
    .nav-link.active {
        background: linear-gradient(135deg, #c4a962, #d4af37);
        color: #0a0f1c;
        font-weight: 600;
    }
    
    .logo-small {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.3rem 1rem;
        background: rgba(196, 169, 98, 0.1);
        border-radius: 30px;
        border: 1px solid #c4a962;
        cursor: pointer;
    }
    
    .logo-small span {
        font-size: 1.5rem;
    }
    
    .logo-small p {
        color: #d4af37;
        font-family: 'Amiri', serif;
        font-size: 1.2rem;
        font-weight: 700;
    }
    
    /* ===== PRAYER & DATE BAR ===== */
    .info-bar {
        background: linear-gradient(135deg, #1a2a3a, #152238);
        border: 1px solid #c4a962;
        border-radius: 20px;
        padding: 1rem 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .prayer-times {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    
    .prayer-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .prayer-item .name {
        color: #c4a962;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .prayer-item .time {
        color: #e8e8e8;
        font-weight: 600;
        font-size: 0.95rem;
        background: rgba(196, 169, 98, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 20px;
    }
    
    .date-section {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    
    .date-box {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(196, 169, 98, 0.1);
        padding: 0.4rem 1rem;
        border-radius: 30px;
        border: 1px solid rgba(196, 169, 98, 0.3);
    }
    
    .date-box .label {
        color: #c4a962;
        font-size: 0.85rem;
    }
    
    .date-box .value {
        color: #e8e8e8;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    .hijri-date {
        font-family: 'Amiri', serif;
        font-size: 1.1rem;
    }
    
    /* ===== ISLAMIC EVENTS SECTION ===== */
    .events-section {
        background: linear-gradient(135deg, #1a2a3a, #152238);
        border: 1px solid #c4a962;
        border-radius: 20px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 2rem;
    }
    
    .events-title {
        color: #d4af37;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        font-family: 'Amiri', serif;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .events-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .event-card {
        background: rgba(196, 169, 98, 0.05);
        border: 1px solid rgba(196, 169, 98, 0.2);
        border-radius: 15px;
        padding: 0.8rem 1.2rem;
        flex: 1 1 200px;
        transition: all 0.3s ease;
    }
    
    .event-card:hover {
        background: rgba(196, 169, 98, 0.1);
        border-color: #c4a962;
        transform: translateY(-2px);
    }
    
    .event-name {
        color: #d4af37;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }
    
    .event-date {
        color: #e8e8e8;
        font-size: 0.85rem;
        display: flex;
        justify-content: space-between;
    }
    
    .event-date .gregorian {
        color: #9ca3af;
    }
    
    /* ===== MAIN HEADER ===== */
    .main-header {
        background: linear-gradient(135deg, #1a2a3a, #0f1a2f);
        padding: 2.5rem;
        border-radius: 20px;
        border: 2px solid #c4a962;
        margin-bottom: 2rem;
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
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.2rem;
        }
    }
    
    .main-subtitle {
        color: #e8e8e8;
        text-align: center;
        font-size: 1.1rem;
        letter-spacing: 1px;
    }
    
    /* ===== PAGE CONTAINERS ===== */
    .page-container {
        animation: fadeIn 0.5s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
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
    
    /* Responsive */
    @media (max-width: 768px) {
        .top-navbar {
            flex-direction: column;
            gap: 1rem;
            border-radius: 20px;
        }
        
        .nav-links {
            justify-content: center;
        }
        
        .info-bar {
            flex-direction: column;
            text-align: center;
        }
        
        .prayer-times {
            justify-content: center;
        }
        
        .date-section {
            justify-content: center;
        }
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

# Current date
today = datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

# ===== ISLAMIC CALENDAR 2026 DATA =====
islamic_events_2026 = [
    {"event": "Al Isra' wal Mi'raj", "hijri": "27 Rajab 1447", "gregorian": "16 Jan 2026", "description": "Night Journey and Ascension"},
    {"event": "Shab-e-Barat", "hijri": "15 Shaban 1447", "gregorian": "3 Feb 2026", "description": "Night of Forgiveness"},
    {"event": "Ramadan Begins", "hijri": "1 Ramadan 1447", "gregorian": "18 Feb 2026", "description": "First day of fasting"},
    {"event": "Laylatul Qadr", "hijri": "27 Ramadan 1447", "gregorian": "17 Mar 2026", "description": "Night of Power"},
    {"event": "Eid al-Fitr", "hijri": "1 Shawwal 1447", "gregorian": "20 Mar 2026", "description": "Festival of Breaking Fast"},
    {"event": "Hajj Begins", "hijri": "8 Dhul Hijjah 1447", "gregorian": "25 May 2026", "description": "Day of Tarwiyah"},
    {"event": "Day of Arafah", "hijri": "9 Dhul Hijjah 1447", "gregorian": "26 May 2026", "description": "Standing at Arafat"},
    {"event": "Eid al-Adha", "hijri": "10 Dhul Hijjah 1447", "gregorian": "27 May 2026", "description": "Festival of Sacrifice"},
    {"event": "Islamic New Year", "hijri": "1 Muharram 1448", "gregorian": "16 Jun 2026", "description": "Hijri New Year"},
    {"event": "Day of Ashura", "hijri": "10 Muharram 1448", "gregorian": "25 Jun 2026", "description": "Day of Remembrance"},
    {"event": "Mawlid al-Nabi", "hijri": "12 Rabi' al-Awwal 1448", "gregorian": "25 Aug 2026", "description": "Birth of Prophet Muhammad (PBUH)"}
]

# Current Hijri date
current_hijri_month = "Ramadan"
current_hijri_day = 3
current_hijri_year = 1447

# JavaScript for smooth scrolling
st.markdown("""
<script>
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Function to handle page navigation with scroll
function navigateToPage(pageName) {
    // Scroll to top smoothly
    scrollToTop();
    
    // Small delay to let scroll complete before page change
    setTimeout(function() {
        // Trigger Streamlit page change
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: pageName
        }, '*');
    }, 300);
}

// Highlight active nav button based on current page
function setActiveNavButton() {
    const currentPage = "Home"; // This will be updated by Streamlit
    const navButtons = document.querySelectorAll('.nav-link');
    
    navButtons.forEach(btn => {
        if (btn.textContent.includes(currentPage)) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

// Smooth scroll to any element
function smoothScrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Run on load
window.addEventListener('load', function() {
    setActiveNavButton();
});
</script>
""", unsafe_allow_html=True)

# ===== TOP NAVIGATION BAR =====
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
    <div class='logo-small' onclick='scrollToTop()'>
        <span>🕌</span>
        <p>NoorAI</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Navigation links with custom HTML for better control
    nav_cols = st.columns(5)
    
    with nav_cols[0]:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.page = "Home"
            st.markdown("<script>scrollToTop();</script>", unsafe_allow_html=True)
            st.rerun()
    
    with nav_cols[1]:
        if st.button("📖 Quran", key="nav_quran", use_container_width=True):
            st.session_state.page = "Quran Reader"
            st.markdown("<script>scrollToTop();</script>", unsafe_allow_html=True)
            st.rerun()
    
    with nav_cols[2]:
        if st.button("👨‍🏫 Tafsir", key="nav_tafsir", use_container_width=True):
            st.session_state.page = "Scholar Tafsir"
            st.markdown("<script>scrollToTop();</script>", unsafe_allow_html=True)
            st.rerun()
    
    with nav_cols[3]:
        if st.button("📚 Hadith", key="nav_hadith", use_container_width=True):
            st.session_state.page = "Hadith Specialist"
            st.markdown("<script>scrollToTop();</script>", unsafe_allow_html=True)
            st.rerun()
    
    with nav_cols[4]:
        if st.button("ℹ️ Guide", key="nav_guide", use_container_width=True):
            st.session_state.page = "How to Use"
            st.markdown("<script>scrollToTop();</script>", unsafe_allow_html=True)
            st.rerun()

# ===== PRAYER TIMES & ISLAMIC DATE BAR =====
st.markdown(f"""
<div class='info-bar'>
    <div class='prayer-times'>
        <div class='prayer-item'><span class='name'>Fajr</span><span class='time'>05:12</span></div>
        <div class='prayer-item'><span class='name'>Dhuhr</span><span class='time'>12:30</span></div>
        <div class='prayer-item'><span class='name'>Asr</span><span class='time'>15:45</span></div>
        <div class='prayer-item'><span class='name'>Maghrib</span><span class='time'>18:15</span></div>
        <div class='prayer-item'><span class='name'>Isha</span><span class='time'>19:45</span></div>
    </div>
    <div class='date-section'>
        <div class='date-box'>
            <span class='label'>Hijri:</span>
            <span class='value hijri-date'>{current_hijri_day} {current_hijri_month} {current_hijri_year} AH</span>
        </div>
        <div class='date-box'>
            <span class='label'>Gregorian:</span>
            <span class='value'>{today.strftime("%d %b %Y")}</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== ISLAMIC EVENTS SECTION =====
st.markdown("""
<div class='events-section'>
    <div class='events-title'>
        <span>📅</span> Important Islamic Dates 2026 (1447-1448 AH)
    </div>
    <div class='events-grid'>
""", unsafe_allow_html=True)

# Create event cards in a grid
for event in islamic_events_2026:
    st.markdown(f"""
        <div class='event-card'>
            <div class='event-name'>{event['event']}</div>
            <div class='event-date'>
                <span>{event['hijri']}</span>
                <span class='gregorian'>{event['gregorian']}</span>
            </div>
            <div style='color: #9ca3af; font-size: 0.75rem; margin-top: 0.3rem;'>{event['description']}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ===== MAIN HEADER =====
st.markdown("""
<div class='main-header'>
    <h1 class='main-title'>🕌 NoorAI</h1>
    <p class='main-subtitle'>Bringing Light to Your Heart with Quranic Guidance</p>
</div>
""", unsafe_allow_html=True)

# ===== PAGE ROUTING with auto-scroll =====
st.markdown("<div class='page-container'>", unsafe_allow_html=True)

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
        
    # Auto-scroll to top after page load
    st.markdown("""
    <script>
        // Scroll to top smoothly after page loads
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    </script>
    """, unsafe_allow_html=True)
    
except Exception as e:
    st.error(f"Error loading page: {str(e)}")

st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown(f"""
<div class='footer'>
    <p style='font-family: Amiri; color: #d4af37; margin-bottom: 0.5rem;'>وَقُل رَّبِّ زِدْنِي عِلْمًا</p>
    <p>© {current_year} NoorAI - Islamic Guidance Platform</p>
</div>
""", unsafe_allow_html=True)
