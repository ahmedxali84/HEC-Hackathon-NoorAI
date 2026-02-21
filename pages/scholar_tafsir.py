# pages/scholar_tafsir.py
import streamlit as st
from gemini_chat import get_tafsir_by_reference
from ai_logic import get_scholar_info

def show():
    # Page Header
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #d4af37; font-size: 1.8rem; font-family: Amiri; margin-bottom: 0.5rem;'>📚 Scholar Tafsir</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem;'>Deep dive into Quranic exegesis from renowned scholars across Islamic history.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Scholar profiles at the top
    scholars_list = [
        ("Ibn Kathir", "🎓", "Hadith-based interpretation"),
        ("Al-Tabari", "📜", "Linguistic analysis"),
        ("Al-Qurtubi", "⚖️", "Legal rulings"),
        ("Al-Sa'di", "💫", "Contemporary approach"),
        ("Al-Razi", "🧠", "Philosophical insight")
    ]
    
    cols = st.columns(5)
    for i, (name, emoji, desc) in enumerate(scholars_list):
        with cols[i]:
            st.markdown(f"""
            <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 15px; text-align: center; border: 1px solid #c4a962;'>
                <p style='font-size: 2rem; margin-bottom: 0.5rem;'>{emoji}</p>
                <p style='color: #d4af37; font-weight: bold;'>{name}</p>
                <p style='color: #e8e8e8; font-size: 0.8rem;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Selection panel
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem; margin-bottom: 1rem;'>
            <h3 style='color: #d4af37; font-size: 1.3rem; font-family: Amiri; margin-bottom: 1rem;'>🔍 Select Scholar & Verse</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Scholar selection with info
        selected_scholar = st.selectbox(
            "Choose Scholar:",
            ["Ibn Kathir", "Al-Tabari", "Al-Qurtubi", "Al-Sa'di", "Al-Razi", "Al-Baghawi", "Al-Shawkani"],
            key="scholar_select"
        )
        
        # Show scholar info
        scholar_info = get_scholar_info(selected_scholar)
        st.markdown(f"""
        <div style='background: rgba(196,169,98,0.05); padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
            <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962; font-weight: 600;'>📅 Era:</span> {scholar_info['era']}</p>
            <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962; font-weight: 600;'>📚 Known for:</span> {scholar_info['known_for']}</p>
            <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962; font-weight: 600;'>💭 Style:</span> {scholar_info['style']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Verse selection
        st.markdown("<h4 style='color: #d4af37; margin: 1rem 0;'>📖 Select Verse</h4>", unsafe_allow_html=True)
        
        input_method = st.radio(
            "Input method:",
            ["Surah & Verse", "Paste Arabic Text"],
            horizontal=True,
            key="input_method"
        )
        
        if input_method == "Surah & Verse":
            surah = st.number_input("Surah Number:", min_value=1, max_value=114, value=1, step=1, key="surah_input")
            ayah = st.number_input("Verse Number:", min_value=1, value=1, step=1, key="ayah_input")
            
            # Quick verse suggestions
            st.markdown("<h4 style='color: #d4af37; margin: 1rem 0 0.5rem 0;'>Famous Verses</h4>", unsafe_allow_html=True)
            famous_verses = [
                ("Ayat-ul-Kursi", 2, 255),
                ("Surah Yaseen", 36, 1),
                ("Surah Ar-Rahman", 55, 1),
                ("Surah Al-Mulk", 67, 1),
                ("Surah Al-Ikhlas", 112, 1)
            ]
            
            cols = st.columns(3)
            for i, (name, s, v) in enumerate(famous_verses[:3]):
                with cols[i]:
                    if st.button(name, key=f"famous_{i}", use_container_width=True):
                        st.session_state.surah_input = s
                        st.session_state.ayah_input = v
                        st.rerun()
            
            if st.button("📚 Get Tafsir", key="get_tafsir_btn", use_container_width=True, type="primary"):
                with st.spinner(f"Retrieving tafsir from {selected_scholar}..."):
                    tafsir = get_tafsir_by_reference(surah, ayah, selected_scholar)
                    if tafsir and "Error" not in tafsir:
                        st.session_state.tafsir_result = tafsir
                        st.session_state.current_scholar = selected_scholar
                        st.session_state.current_ref = f"Surah {surah}:{ayah}"
                    else:
                        st.error("Could not fetch tafsir. Please try again.")
        
        else:  # Paste Arabic
            arabic_text = st.text_area(
                "Paste Arabic text:",
                placeholder="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                height=100,
                key="arabic_text_input"
            )
            if st.button("📚 Get Tafsir", key="get_tafsir_arabic", use_container_width=True, type="primary") and arabic_text:
                with st.spinner(f"Generating tafsir from {selected_scholar}..."):
                    st.info("Paste functionality coming soon! Please use Surah & Verse method.")
    
    with col2:
        # Display area
        if 'tafsir_result' in st.session_state and st.session_state.tafsir_result:
            # Reference header
            if 'current_ref' in st.session_state and 'current_scholar' in st.session_state:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1rem; margin-bottom: 1rem; text-align: center;'>
                    <h3 style='color: #d4af37; margin: 0;'>{st.session_state.current_ref}</h3>
                    <p style='color: #c4a962; margin: 0.3rem 0 0 0;'>Tafsir by {st.session_state.current_scholar}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Display tafsir
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <div style='color: #e8e8e8; white-space: pre-wrap; line-height: 1.6;'>{st.session_state.tafsir_result}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("📋 Copy", key="copy_btn", use_container_width=True):
                    st.success("Copied to clipboard!")
            with col_b:
                if st.button("💾 Save", key="save_btn", use_container_width=True):
                    st.info("Feature coming soon!")
            with col_c:
                if st.button("🔄 New Search", key="new_search_btn", use_container_width=True):
                    del st.session_state.tafsir_result
                    if 'current_scholar' in st.session_state:
                        del st.session_state.current_scholar
                    if 'current_ref' in st.session_state:
                        del st.session_state.current_ref
                    st.rerun()
        
        else:
            # Welcome message
            st.markdown("""
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 2rem; text-align: center;'>
                <p style='font-size: 4rem; margin-bottom: 1rem;'>📚</p>
                <h3 style='color: #d4af37; margin-bottom: 1rem;'>Scholar Tafsir</h3>
                <p style='color: #e8e8e8; margin-bottom: 1.5rem;'>Select a scholar and verse to begin exploring deep Quranic insights.</p>
            </div>
            """, unsafe_allow_html=True)
