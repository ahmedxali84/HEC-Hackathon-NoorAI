# pages/quran_reader.py
import streamlit as st
from gemini_chat import get_quran_by_reference

def show():
    # Page Header
    st.markdown("""
    <div class='card'>
        <h2 class='card-title'>📖 Al-Quran Al-Kareem</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem;'>Read and reflect upon the words of Allah. Enter a reference to access any verse.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Search panel
        st.markdown("""
        <div class='card'>
            <h3 class='card-title'>🔍 Search Quran</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Input method
        search_method = st.radio(
            "Search by:",
            ["Surah & Verse", "Keyword", "Topic"],
            horizontal=True
        )
        
        if search_method == "Surah & Verse":
            surah = st.number_input("Surah Number:", min_value=1, max_value=114, value=1, step=1)
            ayah_start = st.number_input("Start Verse:", min_value=1, value=1, step=1)
            ayah_end = st.number_input("End Verse (optional):", min_value=1, value=1, step=1)
            
            # Popular surahs quick access
            st.markdown("### Popular Surahs")
            popular_surahs = [
                ("Al-Fatiha", 1), ("Al-Baqarah", 2), ("Yaseen", 36),
                ("Ar-Rahman", 55), ("Al-Mulk", 67), ("Al-Ikhlas", 112)
            ]
            
            cols = st.columns(2)
            for i, (name, num) in enumerate(popular_surahs):
                with cols[i % 2]:
                    if st.button(f"{name} ({num})", key=f"surah_{num}", use_container_width=True):
                        surah = num
                        ayah_start = 1
                        st.session_state.surah_selected = num
                        st.rerun()
            
            if st.button("📖 Read Verses", use_container_width=True, type="primary"):
                with st.spinner("Fetching from the Noble Quran..."):
                    result = get_quran_by_reference(surah, ayah_start, ayah_end if ayah_end > ayah_start else None)
                    if result and "Error" not in result:
                        st.session_state.quran_result = result
                        st.session_state.current_ref = f"Surah {surah}:{ayah_start}" + (f"-{ayah_end}" if ayah_end > ayah_start else "")
                    else:
                        st.error("Could not fetch verses. Please try again.")
        
        elif search_method == "Keyword":
            keyword = st.text_input("Enter keyword:", placeholder="e.g., mercy, patience, heaven")
            if st.button("🔍 Search", use_container_width=True, type="primary") and keyword:
                with st.spinner(f"Searching for '{keyword}'..."):
                    # In production, implement keyword search
                    st.info("Keyword search coming soon! For now, try Surah & Verse search.")
        
        else:  # Topic
            topic = st.selectbox(
                "Select topic:",
                ["Mercy (Rahmah)", "Patience (Sabr)", "Forgiveness", "Paradise (Jannah)", 
                 "Hellfire", "Prophets", "Prayer", "Charity"]
            )
            if st.button("🔍 Search", use_container_width=True, type="primary"):
                with st.spinner(f"Finding verses about {topic}..."):
                    st.info("Topic search coming soon! For now, try Surah & Verse search.")
        
        # Bookmarks section
        st.markdown("""
        <div class='card'>
            <h3 class='card-title'>📌 Bookmarks</h3>
            <p style='color: #e8e8e8;'>Sign in to save your favorite verses</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Display area
        if 'quran_result' in st.session_state and st.session_state.quran_result:
            # Reference header
            if 'current_ref' in st.session_state:
                st.markdown(f"""
                <div class='card' style='text-align: center;'>
                    <h3 style='color: #d4af37;'>{st.session_state.current_ref}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            # Display the result
            st.markdown(f"""
            <div class='card'>
                <div style='color: #e8e8e8; white-space: pre-wrap;'>{st.session_state.quran_result}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("📋 Copy", use_container_width=True):
                    st.success("Copied to clipboard!")
            with col_b:
                if st.button("🔖 Bookmark", use_container_width=True):
                    st.info("Feature coming soon!")
            with col_c:
                if st.button("🔄 Clear", use_container_width=True):
                    del st.session_state.quran_result
                    if 'current_ref' in st.session_state:
                        del st.session_state.current_ref
                    st.rerun()
        
        else:
            # Welcome message
            st.markdown("""
            <div class='card' style='text-align: center; padding: 4rem 2rem;'>
                <p style='font-size: 5rem; margin-bottom: 1rem;'>📖</p>
                <h3 style='color: #d4af37; margin-bottom: 1rem;'>Welcome to Quran Reader</h3>
                <p style='color: #e8e8e8; font-size: 1.2rem; margin-bottom: 2rem;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</p>
                <p style='color: #c4a962;'>Enter a Surah and verse number to begin reading</p>
                <div style='background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px; margin-top: 2rem;'>
                    <p style='color: #e8e8e8;'><strong>Example:</strong> Surah 1, Verses 1-7 (Al-Fatiha)</p>
                    <p style='color: #e8e8e8;'><strong>Quick tip:</strong> Click on popular surahs for instant access</p>
                </div>
            </div>
            
            <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 2rem;'>
                <div class='card' style='text-align: center;'>
                    <p style='font-size: 2rem; margin-bottom: 0.5rem;'>📚</p>
                    <p style='color: #d4af37;'>114</p>
                    <p style='color: #e8e8e8;'>Surahs</p>
                </div>
                <div class='card' style='text-align: center;'>
                    <p style='font-size: 2rem; margin-bottom: 0.5rem;'>✨</p>
                    <p style='color: #d4af37;'>6,236</p>
                    <p style='color: #e8e8e8;'>Verses</p>
                </div>
                <div class='card' style='text-align: center;'>
                    <p style='font-size: 2rem; margin-bottom: 0.5rem;'>🕋</p>
                    <p style='color: #d4af37;'>30</p>
                    <p style='color: #e8e8e8;'>Juz</p>
                </div>
            </div>
            """, unsafe_allow_html=True)