# pages/hadith_specialist.py
import streamlit as st
from gemini_chat import get_hadith_by_topic

def show():
    st.markdown("""
    <div class='card'>
        <h2 class='card-title'>📚 Hadith Specialist</h2>
        <p style='color: #e8e8e8;'>Authentic Prophetic traditions from major collections</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 class='card-title'>Search Hadith</h3>
        </div>
        """, unsafe_allow_html=True)
        
        topic = st.text_input("Enter topic:", placeholder="e.g., prayer, fasting, charity")
        
        # Popular topics
        st.markdown("**Popular Topics:**")
        topics = ["Prayer", "Fasting", "Charity", "Kindness", "Patience", "Forgiveness"]
        cols = st.columns(3)
        for i, t in enumerate(topics):
            with cols[i % 3]:
                if st.button(t, key=f"topic_{i}"):
                    topic = t.lower()
        
        if st.button("🔍 Search Hadith", use_container_width=True) and topic:
            with st.spinner("Searching authentic hadith..."):
                hadith = get_hadith_by_topic(topic)
                if hadith and "Error" not in hadith:
                    st.session_state.hadith_result = hadith
                else:
                    st.error("Could not fetch hadith. Please try again.")
    
    with col2:
        if 'hadith_result' in st.session_state:
            st.markdown(f"""
            <div class='card'>
                <h3 style='color: #d4af37;'>Result</h3>
                <div style='color: #e8e8e8;'>{st.session_state.hadith_result}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Clear"):
                del st.session_state.hadith_result
                st.rerun()
        else:
            st.markdown("""
            <div class='card' style='text-align: center;'>
                <p style='font-size: 3rem;'>📚</p>
                <p style='color: #e8e8e8;'>Enter a topic to search for hadith</p>
            </div>
            """, unsafe_allow_html=True)