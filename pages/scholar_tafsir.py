# pages/scholar_tafsir.py
import streamlit as st
from gemini_chat import get_tafsir_by_reference
from ai_logic import get_scholar_info

def show():
    # Page Header
    st.markdown("""
    <div class='card'>
        <h2 class='card-title'>📚 Scholar Tafsir</h2>
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
        <div class='card'>
            <h3 class='card-title'>🔍 Select Scholar & Verse</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Scholar selection with info
        selected_scholar = st.selectbox(
            "Choose Scholar:",
            ["Ibn Kathir", "Al-Tabari", "Al-Qurtubi", "Al-Sa'di", "Al-Razi", "Al-Baghawi", "Al-Shawkani"]
        )
        
        # Show scholar info
        scholar_info = get_scholar_info(selected_scholar)
        st.markdown(f"""
        <div style='background: rgba(196,169,98,0.05); padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
            <p style='color: #c4a962;'><strong>📅 Era:</strong> {scholar_info['era']}</p>
            <p style='color: #c4a962;'><strong>📚 Known for:</strong> {scholar_info['known_for']}</p>
            <p style='color: #c4a962;'><strong>💭 Style:</strong> {scholar_info['style']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Verse selection
        st.markdown("### 📖 Select Verse")
        
        input_method = st.radio(
            "Input method:",
            ["Surah & Verse", "Paste Arabic Text"],
            horizontal=True
        )
        
        if input_method == "Surah & Verse":
            surah = st.number_input("Surah Number:", min_value=1, max_value=114, value=1, step=1)
            ayah = st.number_input("Verse Number:", min_value=1, value=1, step=1)
            
            # Quick verse suggestions
            st.markdown("### Famous Verses")
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
                        surah = s
                        ayah = v
                        st.rerun()
            
            if st.button("📚 Get Tafsir", use_container_width=True, type="primary"):
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
                height=100
            )
            if st.button("📚 Get Tafsir", use_container_width=True, type="primary") and arabic_text:
                with st.spinner(f"Generating tafsir from {selected_scholar}..."):
                    st.info("Paste functionality coming soon! Please use Surah & Verse method.")
    
    with col2:
        # Display area
        if 'tafsir_result' in st.session_state and st.session_state.tafsir_result:
            # Reference header
            if 'current_ref' in st.session_state and 'current_scholar' in st.session_state:
                st.markdown(f"""
                <div class='card' style='text-align: center;'>
                    <h3 style='color: #d4af37;'>{st.session_state.current_ref}</h3>
                    <p style='color: #c4a962;'>Tafsir by {st.session_state.current_scholar}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Display tafsir
            st.markdown(f"""
            <div class='card'>
                <div style='color: #e8e8e8; white-space: pre-wrap;'>{st.session_state.tafsir_result}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("📋 Copy", use_container_width=True):
                    st.success("Copied to clipboard!")
            with col_b:
                if st.button("💾 Save", use_container_width=True):
                    st.info("Feature coming soon!")
            with col_c:
                if st.button("🔄 New Search", use_container_width=True):
                    del st.session_state.tafsir_result
                    del st.session_state.current_scholar
                    del st.session_state.current_ref
                    st.rerun()
        
        else:
            # Welcome message
            st.markdown("""
            <div class='card' style='text-align: center; padding: 3rem 2rem;'>
                <p style='font-size: 4rem; margin-bottom: 1rem;'>📚</p>
                <h3 style='color: #d4af37; margin-bottom: 1rem;'>Scholar Tafsir</h3>
                <p style='color: #e8e8e8;'>Select a scholar and verse to begin exploring deep Quranic insights.</p>
                
                <div style='margin-top: 2rem; text-align: left;'>
                    <h4 style='color: #d4af37;'>💡 Did You Know?</h4>
                    <p style='color: #e8e8e8;'>Tafsir Ibn Kathir is one of the most widely used explanations of the Quran, known for its reliance on authentic hadith and the interpretations of the early generations (Salaf).</p>
                </div>
            </div>
            """, unsafe_allow_html=True)