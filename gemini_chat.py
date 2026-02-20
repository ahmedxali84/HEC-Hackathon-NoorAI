# gemini_chat.py
from google.genai import Client
import streamlit as st
import time

# Gemini API Client
client = Client(api_key = st.secrets["GEMINI_API_KEY"])

def fetch_ayah(emotion):
    """
    Gemini generates an Arabic ayah based on emotion - NO HARDCODED VERSES
    """
    try:
        prompt = f"""
        You are a Quranic scholar. Based on someone feeling **{emotion}**, provide an appropriate Quranic verse (Ayah) that would comfort or guide them.

        IMPORTANT INSTRUCTIONS:
        1. Select a verse that is DIRECTLY relevant to the emotion: {emotion}
        2. Return ONLY the Arabic text with the verse reference in parentheses
        3. DO NOT use the same verse for different emotions
        4. Make sure the verse is from the authentic Quran
        5. Include proper diacritical marks (tashkeel)
        6. Format: [Arabic text] (Surah:Verse)

        Examples of good responses:
        - For sadness: وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ (آل عمران:139)
        - For anxiety: أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (الرعد:28)
        - For happiness: قُلْ بِفَضْلِ اللَّهِ وَبِرَحْمَتِهِ فَبِذَٰلِكَ فَلْيَفْرَحُوا (يونس:58)

        Now provide a verse for someone feeling: {emotion}
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        arabic_text = response.text.strip()
        
        # Log what we got for debugging
        st.session_state.last_ayah = arabic_text
        st.session_state.last_emotion = emotion
        
        return arabic_text
            
    except Exception as e:
        st.error(f"Gemini API Error: {str(e)}")
        # Return a message that Gemini failed - no hardcoded verses
        return f"Error fetching verse. Please try again."

def translate_ayah(ayah_text):
    """
    Gemini translates Arabic ayah into beautiful English.
    """
    try:
        prompt = f"""
        Translate this Quranic verse into beautiful, poetic, and emotionally resonant English.
        
        Verse (Arabic): {ayah_text}
        
        Instructions:
        - Make the translation spiritually uplifting
        - Capture the emotional essence of the verse
        - Use eloquent English
        - Return ONLY the translation, no explanations or additional text
        - Do not include the Arabic text in your response
        
        Translation:
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
            
    except Exception as e:
        return f"Translation error: {str(e)}"

def generate_tafsir(ayah_text, scholar_name):
    """
    Gemini generates tafsir according to chosen scholar.
    """
    try:
        prompt = f"""
        Provide a detailed tafsir (explanation) of this Quranic verse according to the methodology of {scholar_name}.
        
        Verse: {ayah_text}
        Scholar: {scholar_name}
        
        Your response should include:
        1. Brief introduction to how {scholar_name} approaches tafsir
        2. The main interpretation according to {scholar_name}
        3. Key spiritual lessons and practical guidance
        4. Any unique insights from {scholar_name}'s methodology
        
        Style: Scholarly but accessible, spiritually uplifting
        Length: 3-4 paragraphs
        
        Tafsir:
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
            
    except Exception as e:
        return f"Tafsir error: {str(e)}"

def get_quran_by_reference(surah, ayah_start, ayah_end=None):
    """
    Gemini fetches Quranic verses by reference.
    """
    try:
        if ayah_end and ayah_end > ayah_start:
            verse_range = f"verses {ayah_start} to {ayah_end}"
        else:
            verse_range = f"verse {ayah_start}"
        
        prompt = f"""
        Provide Surah {surah}, {verse_range} from the Holy Quran.
        
        Format your response EXACTLY like this:
        
        📖 SURAH {surah}:{ayah_start}{'-' + str(ayah_end) if ayah_end and ayah_end > ayah_start else ''}
        
        🌙 ARABIC:
        [Write the Arabic text with proper diacritical marks here]
        
        📝 TRANSLATION:
        [Write the English translation here]
        
        💫 CONTEXT:
        [Write brief context of these verses here]
        
        ✨ KEY THEMES:
        [Write main themes addressed here]
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
            
    except Exception as e:
        return f"Error fetching verses from Surah {surah}"

def get_hadith_by_topic(topic):
    """
    Gemini fetches authentic hadith based on topic.
    """
    try:
        prompt = f"""
        Find an authentic hadith (Prophetic tradition) related to: {topic}
        
        IMPORTANT:
        - Use only authentic hadith from major collections (Bukhari, Muslim, Abu Dawud, Tirmidhi, Ibn Majah, Nasai)
        - The hadith must be directly relevant to: {topic}
        
        Format your response EXACTLY like this:
        
        📚 HADITH ON {topic.upper()}
        
        ARABIC:
        [Hadith in Arabic with diacritical marks]
        
        TRANSLATION:
        [English translation]
        
        SOURCE:
        Collection: [Bukhari/Muslim/etc.]
        Number: [Hadith number]
        Narrator: [Who narrated it]
        Grade: [Sahih/Hasan/etc.]
        
        EXPLANATION:
        [Brief spiritual explanation of the hadith]
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
            
    except Exception as e:
        return f"Error fetching hadith about {topic}"

def get_tafsir_by_reference(surah, ayah, scholar_name):
    """
    Gemini fetches verse and provides tafsir.
    """
    try:
        prompt = f"""
        First, provide Surah {surah}, verse {ayah} from the Quran.
        Then provide detailed tafsir according to {scholar_name}.
        
        Format your response EXACTLY like this:
        
        📖 SURAH {surah}:{ayah}
        
        🌙 ARABIC:
        [Arabic text with diacritical marks]
        
        📝 TRANSLATION:
        [English translation]
        
        📚 TAFSIR BY {scholar_name.upper()}:
        [Detailed tafsir explanation including:
        - Historical context
        - Linguistic analysis
        - Spiritual lessons
        - Practical applications
        - {scholar_name}'s unique perspective]
        
        ✨ KEY INSIGHTS:
        • [Insight 1]
        • [Insight 2]
        • [Insight 3]
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
            
    except Exception as e:
        return f"Error generating tafsir for Surah {surah}:{ayah}"

def detect_emotion(user_text):
    """
    Enhanced keyword-based emotion detection
    """
    user_text = user_text.lower()
    
    emotion_keywords = {
        "happiness": ["happy", "joy", "joyful", "delighted", "pleased", "glad", "cheerful", "excited"],
        "sadness": ["sad", "sadness", "grief", "grieving", "heartbroken", "depressed", "upset", "crying", "tears", "mourning"],
        "anxiety": ["anxious", "anxiety", "nervous", "worried", "stress", "stressed", "overwhelmed", "panic", "fearful"],
        "fear": ["fear", "scared", "afraid", "terrified", "frightened", "dread", "horror"],
        "anger": ["angry", "anger", "frustrated", "mad", "annoyed", "irritated", "furious", "rage"],
        "gratitude": ["grateful", "thankful", "blessed", "appreciate", "appreciation", "thank you", "shukr"],
        "hope": ["hope", "hopeful", "optimistic", "looking forward", "positive", "aspire"],
        "love": ["love", "loving", "affection", "care", "caring", "compassion", "mercy"],
        "forgiveness": ["forgive", "forgiveness", "sorry", "regret", "guilty", "repent", "taubah"],
        "patience": ["patient", "patience", "waiting", "sabar", "endurance", "perseverance"],
        "grief": ["grief", "loss", "died", "passed away", "death", "deceased", "janazah"],
        "stress": ["stress", "pressure", "burden", "tired", "exhausted", "burnout"],
        "peace": ["peace", "calm", "tranquil", "serene", "quiet", "relaxed", "sukoon"]
    }
    
    for emotion, words in emotion_keywords.items():
        for word in words:
            if word in user_text:
                return emotion
    
    return "hope"  # Default emotion

def detect_emotion_with_gemini(user_text):
    """
    Use Gemini for more accurate emotion detection
    """
    try:
        prompt = f"""
        Analyze this text and detect the primary emotion: "{user_text}"
        
        Return ONLY ONE WORD from this list:
        happiness, sadness, anxiety, fear, anger, gratitude, hope, love, forgiveness, patience, grief, stress, peace
        
        Just return the emotion word, nothing else.
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        emotion = response.text.strip().lower()
        
        # Validate emotion
        valid_emotions = ['happiness', 'sadness', 'anxiety', 'fear', 'anger', 'gratitude', 
                         'hope', 'love', 'forgiveness', 'patience', 'grief', 'stress', 'peace']
        
        if emotion in valid_emotions:
            return emotion
        else:
            return detect_emotion(user_text)  # Fallback to keyword-based
            
    except Exception as e:
        return detect_emotion(user_text)  # Fallback to keyword-based