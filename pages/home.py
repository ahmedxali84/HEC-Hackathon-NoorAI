# pages/home.py
import streamlit as st
from gemini_chat import fetch_ayah, translate_ayah, generate_tafsir, detect_emotion_with_gemini, detect_emotion

def show():
    # Page Header
    st.markdown("""
    <div class='card'>
        <h2 class='card-title'>💭 Emotional Quran Companion</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem;'>Share your feelings and receive personalized Quranic guidance. Let the words of Allah comfort your heart.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session states
    if "step" not in st.session_state:
        st.session_state.step = "emotion"
    if "current_ayah" not in st.session_state:
        st.session_state.current_ayah = None
    if "translation" not in st.session_state:
        st.session_state.translation = None
    if "detected_emotion" not in st.session_state:
        st.session_state.detected_emotion = None
    if "processing" not in st.session_state:
        st.session_state.processing = False
    
    # Main chat area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Quick emotion buttons with more options
        st.markdown("### How are you feeling?")
        emotions = [
            ("😊 Happy", "happiness"), 
            ("😢 Sad", "sadness"), 
            ("😨 Anxious", "anxiety"),
            ("😤 Angry", "anger"), 
            ("🤲 Grateful", "gratitude"),
            ("💫 Hopeful", "hope"),
            ("😰 Fearful", "fear"),
            ("🕊️ Peaceful", "peace"),
            ("💔 Heartbroken", "grief"),
            ("😕 Confused", "confusion"),
            ("🫂 Lonely", "loneliness"),
            ("💪 Stressed", "stress")
        ]
        
        # Create 4 columns for buttons
        cols = st.columns(4)
        for i in range(0, len(emotions), 4):
            for j in range(4):
                if i + j < len(emotions):
                    label, emotion = emotions[i + j]
                    with cols[j]:
                        if st.button(label, key=f"emo_{i+j}", use_container_width=True):
                            if not st.session_state.processing:
                                st.session_state.quick_emotion = emotion
                                st.rerun()
        
        st.markdown("<div style='height: 1px; background: linear-gradient(90deg, transparent, #c4a962, transparent); margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        # Chat input
        user_input = st.text_input(
            "Or type your feelings here:",
            placeholder="e.g., I'm feeling really sad today...",
            key="chat_input",
            disabled=st.session_state.processing
        )
        
        # Process input from button or text
        if 'quick_emotion' in st.session_state and not st.session_state.processing:
            process_emotion(st.session_state.quick_emotion)
            del st.session_state.quick_emotion
            
        elif user_input and st.button("Send", use_container_width=True, disabled=st.session_state.processing):
            process_emotion(user_input)
    
    with col2:
        # Information sidebar
        st.markdown("""
        <div class='card'>
            <h3 class='card-title'>How It Works</h3>
            <ol style='color: #e8e8e8; margin-left: 1.5rem;'>
                <li>Share your feelings</li>
                <li>Gemini AI detects emotion</li>
                <li>Unique Quranic verse appears</li>
                <li>Beautiful translation</li>
                <li>Ask for scholar's tafsir</li>
            </ol>
        </div>
        
        <div class='card'>
            <h3 class='card-title'>Popular Scholars</h3>
            <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>Ibn Kathir</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>Al-Tabari</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>Al-Qurtubi</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>Al-Sa'di</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>Al-Razi</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display conversation based on step
    if st.session_state.step == "scholar" and st.session_state.current_ayah:
        st.markdown("---")
        
        # Display the verse
        st.markdown("### 📖 Quranic Guidance")
        st.markdown(f"<div class='arabic-text'>{st.session_state.current_ayah}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #e8e8e8; font-style: italic; text-align: center;'>{st.session_state.translation}</p>", unsafe_allow_html=True)
        
        # Ask for scholar
        st.markdown("### Would you like tafsir from a specific scholar?")
        scholar = st.text_input("Enter scholar name:", placeholder="e.g., Ibn Kathir, Al-Tabari, Al-Qurtubi")
        
        if st.button("Get Tafsir", use_container_width=True) and scholar:
            with st.spinner(f"Generating tafsir from {scholar}..."):
                tafsir = generate_tafsir(st.session_state.current_ayah, scholar)
                
                st.markdown(f"""
                <div class='card'>
                    <h4 style='color: #d4af37;'>📚 Tafsir by {scholar}</h4>
                    <p style='color: #e8e8e8;'>{tafsir}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Reset for new conversation
                if st.button("New Conversation", use_container_width=True):
                    st.session_state.step = "emotion"
                    st.session_state.current_ayah = None
                    st.session_state.processing = False
                    st.rerun()

def process_emotion(input_text):
    """Process user emotion and fetch ayah - Pure Gemini, no hardcoded verses"""
    st.session_state.processing = True
    
    with st.spinner("🧠 Gemini AI is analyzing your feelings and selecting a unique Quranic verse..."):
        # Try Gemini emotion detection first, fall back to keyword
        try:
            emotion = detect_emotion_with_gemini(input_text)
        except:
            emotion = detect_emotion(input_text)
        
        # Show detected emotion
        st.info(f"Detected emotion: **{emotion.title()}**")
        
        # Fetch ayah from Gemini - NO HARDCODED VERSES
        ayah = fetch_ayah(emotion)
        translation = translate_ayah(ayah)
        
        # Store in session state
        st.session_state.current_ayah = ayah
        st.session_state.translation = translation
        st.session_state.detected_emotion = emotion
        st.session_state.step = "scholar"
        st.session_state.processing = False
        
        st.rerun()