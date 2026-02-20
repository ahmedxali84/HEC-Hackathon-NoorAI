# NoorAI (نور الذكاء الاصطناعي) – Islamic Guidance Platform

![NoorAI Banner](https://via.placeholder.com/800x200.png?text=NoorAI+Islamic+Guidance+Platform)

---

## 📋 Project Overview

**NoorAI** is an intelligent Islamic guidance platform that combines traditional Islamic scholarship with modern AI technology. The application provides:

- Personalized Quranic verses based on emotional states  
- Access to Tafsir from renowned scholars  
- Authentic Hadith collections  
- A comprehensive Quran reader  

All content is presented in a **stunning dark Islamic theme** with gold accents.  

The platform leverages **Google Gemini 2.5 Flash AI** to generate contextually appropriate Quranic verses, translations, and scholarly interpretations in real-time, ensuring each interaction is **unique and meaningful**.

---

## ✨ Core Features

### 🤖 Emotion-Based Quranic Guidance
- AI-powered emotion detection from user input  
- Real-time generation of relevant Quranic verses  
- Beautiful English translations  
- Dynamic Tafsir generation from multiple scholars  

### 📖 Comprehensive Quran Reader
- Access any verse by Surah and Ayah numbers  
- Quick access to popular Surahs  
- Arabic text with proper diacritical marks  
- Contextual information and thematic analysis  

### 👨‍🏫 Multi-Scholar Tafsir System
- Interpretations from 7+ renowned scholars:  
  **Ibn Kathir | Al-Tabari | Al-Qurtubi | Al-Sa'di | Al-Razi | Al-Baghawi | Al-Shawkani**  
- Scholar biographies and methodologies  
- Verse context and key themes  

### 📚 Authentic Hadith Database
- Search by topic across 6 major collections:  
  **Bukhari, Muslim, Abu Dawud, Tirmidhi, Ibn Majah, Nasai**  
- Arabic text with English translation  
- Source, narrator, and authentication grade  

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.9+ | Core programming language |
| Streamlit | Web application framework |
| Google Gemini AI | AI-powered content generation |
| Streamlit-Option-Menu | Professional navigation |
| CSS3 / HTML5 | Custom dark Islamic theme |

---

## 🏗️ Project Architecture
noorai/
│
├── app.py # Main application entry point
├── gemini_chat.py # Gemini AI integration
├── ai_logic.py # Supporting AI logic
├── requirements.txt # Dependencies
│
└── pages/ # Multi-page architecture
├── init.py
├── home.py # Emotion chat interface
├── quran_reader.py # Quran browsing
├── scholar_tafsir.py # Scholar interpretations
├── hadith_specialist.py # Hadith search
└── how_to_use.py # User guide


---

## 🎨 Design Philosophy
- **Dark Islamic Theme:** Deep blues and gold accents reflecting Islamic art  
- **Glass Morphism:** Modern blur effects with traditional patterns  
- **Responsive Design:** Seamless experience across all devices  
- **Arabic Calligraphy:** Beautiful rendering of Arabic text  
- **Professional UI:** Clean, intuitive, and accessible interface  

---

## 🔑 Key Differentiators
- **Pure AI Generation:** No hardcoded verses – every response is uniquely generated  
- **Real-time Scholar Tafsir:** Instant interpretations from multiple scholars  
- **Emotional Intelligence:** AI-powered emotion detection for personalized guidance  
- **Authentic Sources:** All content based on verified Islamic sources  
- **Modern UI/UX:** Traditional knowledge meets contemporary design  

---

## 📊 Platform Capabilities

| Feature | Description |
|---------|-------------|
| Quranic Verses | 114 Surahs, 6,236+ Ayahs |
| Scholars | 7+ renowned mufassireen |
| Hadith Collections | 6 major books, 40,000+ hadith |
| Emotions Detected | 15+ emotional states |
| Languages | Arabic text, English translation |
| Response Time | 2–5 seconds (AI-generated) |

---

## 🔒 Security & Privacy
- No user data storage  
- Anonymous interactions  
- Secure API key management  
- Environment variable configuration  

---

## 🚀 Target Audience
- Muslims seeking spiritual guidance  
- Quranic study circles  
- Islamic scholars and students  
- New Muslims learning about Islam  
- Anyone interested in Islamic teachings  

---

## 📌 Version Information
**Status:** MVP Hackathon Ready  

---

## 🤝 Contributors
- **Team Lead:** Ahmed Ali  
- **Team Members:** Muhammad Shaheer Khan, Huzaifa Akhter, Hiban Siddique  

---

## 💻 How to Run

1. Clone the repository:  
```bash
git clone <repository-url>
cd noorai

pip install -r requirements.txt
client = Client(api_key="YOUR_VALID_GEMINI_KEY")

streamlit run app.py

