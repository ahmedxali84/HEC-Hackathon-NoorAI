# ai_logic.py
import random

def get_emotion_meaning(emotion):
    """
    Returns Islamic perspective on different emotions.
    """
    meanings = {
        "sadness": "In Islam, sadness is recognized as a natural human emotion. The Quran teaches us that with hardship comes ease (94:5-6).",
        "anxiety": "Allah says in the Quran: 'Verily, in the remembrance of Allah do hearts find rest' (13:28). Turn to Him in your moments of anxiety.",
        "hope": "Hope is a beautiful part of faith. The Prophet Muhammad (ﷺ) said: 'The strong believer is better and more beloved to Allah than the weak believer, but there is good in both.'",
        "happiness": "True happiness comes from faith and gratitude. 'If you are grateful, I will surely increase you' (14:7).",
        "fear": "Fear can bring us closer to Allah. 'And fear Me, if you are believers' (3:175).",
        "anger": "The Prophet (ﷺ) advised: 'Do not get angry.' Control your anger and seek refuge in Allah.",
        "gratitude": "Gratitude is the key to increase. 'And remember when your Lord proclaimed: If you are grateful, I will surely increase you' (14:7).",
        "love": "Love for the sake of Allah is the highest form of love. The Prophet (ﷺ) said: 'You will not enter Paradise until you believe, and you will not believe until you love one another.'",
        "forgiveness": "Allah is Al-Ghafoor (The All-Forgiving). 'And let them pardon and overlook. Would you not like that Allah should forgive you?' (24:22).",
        "patience": "Patience (Sabr) is half of faith. 'Indeed, the patient will be given their reward without account' (39:10).",
        "grief": "Even Prophet Ya'qub (AS) experienced grief when he lost his son Yusuf (AS). Turn to Allah in your grief.",
        "stress": "The Prophet (ﷷ) taught us to say: 'Hasbunallah wa ni'mal wakeel' (Allah is sufficient for us, and He is the best disposer of affairs).",
        "peace": "The ultimate peace (Sakinah) comes from Allah. 'He it is who sent down tranquility into the hearts of the believers' (48:4)."
    }
    return meanings.get(emotion, "Turn to Allah in all your emotions. He is As-Sami' (The All-Hearing).")

def get_scholar_info(scholar_name):
    """
    Returns information about Islamic scholars.
    """
    scholars = {
        "Ibn Kathir": {
            "era": "701-774 AH (1301-1373 CE)",
            "known_for": "Famous for his Tafsir 'Al-Qur'an Al-Azim' which focuses on hadith and early interpretations",
            "style": "Comprehensive, relying heavily on hadith and the interpretations of the Salaf"
        },
        "Al-Tabari": {
            "era": "224-310 AH (839-923 CE)",
            "known_for": "Pioneer of Quranic exegesis, author of 'Jami' al-Bayan 'an Ta'wil ay al-Qur'an'",
            "style": "Detailed linguistic analysis, multiple narrations, scholarly rigor"
        },
        "Al-Qurtubi": {
            "era": "610-671 AH (1214-1273 CE)",
            "known_for": "Specialized in legal rulings derived from the Quran in his work 'Al-Jami' li Ahkam al-Qur'an'",
            "style": "Focus on fiqh (jurisprudence) and legal implications"
        },
        "Al-Sa'di": {
            "era": "1307-1376 AH (1889-1956 CE)",
            "known_for": "Modern scholar known for 'Taysir al-Karim al-Rahman', a clear and accessible tafsir",
            "style": "Simple, practical, focused on spiritual development"
        },
        "Al-Razi": {
            "era": "544-606 AH (1149-1209 CE)",
            "known_for": "Famous for 'Mafatih al-Ghayb', a philosophical and rational approach to tafsir",
            "style": "Deep philosophical analysis, theological discussions"
        },
        "Al-Baghawi": {
            "era": "433-516 AH (1041-1122 CE)",
            "known_for": "Known for 'Ma'alim al-Tanzil', combining hadith with tafsir",
            "style": "Concise, relying on authentic hadith and Salaf interpretations"
        },
        "Al-Shawkani": {
            "era": "1173-1250 AH (1760-1834 CE)",
            "known_for": "Yemeni scholar known for 'Fath al-Qadir', a balanced approach to tafsir",
            "style": "Combines traditional tafsir with critical analysis"
        }
    }
    return scholars.get(scholar_name, {"era": "Unknown", "known_for": "Renowned Islamic scholar", "style": "Traditional scholarly approach"})

def get_hadith_collections():
    """
    Returns information about major hadith collections.
    """
    return {
        "Sahih Bukhari": {
            "scholar": "Imam Muhammad al-Bukhari (194-256 AH)",
            "total": 7563,
            "description": "Most authentic book after the Quran",
            "grade": "Sahih (Authentic)"
        },
        "Sahih Muslim": {
            "scholar": "Imam Muslim ibn al-Hajjaj (204-261 AH)",
            "total": 7563,
            "description": "Second most authentic hadith collection",
            "grade": "Sahih (Authentic)"
        },
        "Sunan Abu Dawud": {
            "scholar": "Imam Abu Dawud Sulayman (202-275 AH)",
            "total": 5274,
            "description": "Focus on legal hadith (ahkam)",
            "grade": "Contains Sahih, Hasan, and Da'if"
        },
        "Jami At-Tirmidhi": {
            "scholar": "Imam Muhammad al-Tirmidhi (209-279 AH)",
            "total": 3956,
            "description": "Includes grading of hadith",
            "grade": "Contains Sahih, Hasan, and Da'if"
        },
        "Sunan Ibn Majah": {
            "scholar": "Imam Muhammad ibn Majah (209-273 AH)",
            "total": 4341,
            "description": "Final of the six major collections",
            "grade": "Contains Sahih, Hasan, and Da'if"
        },
        "Sunan An-Nasai": {
            "scholar": "Imam Ahmad an-Nasai (215-303 AH)",
            "total": 5758,
            "description": "Known for meticulous chain analysis",
            "grade": "Contains mostly Sahih hadith"
        }
    }

def get_prayer_times(city="Mecca"):
    """
    Returns prayer times for a given city.
    """
    # Sample prayer times - In production, use API
    times = {
        "Mecca": {"Fajr": "05:12", "Dhuhr": "12:30", "Asr": "15:45", "Maghrib": "18:15", "Isha": "19:45"},
        "Medina": {"Fajr": "05:15", "Dhuhr": "12:32", "Asr": "15:47", "Maghrib": "18:17", "Isha": "19:47"},
        "Jerusalem": {"Fajr": "05:20", "Dhuhr": "12:35", "Asr": "15:50", "Maghrib": "18:20", "Isha": "19:50"}
    }
    return times.get(city, times["Mecca"])

def get_islamic_date():
    """
    Returns current Islamic date.
    """
    # Sample date - In production, use API or calculation
    months = ['Muharram', 'Safar', 'Rabi\' al-Awwal', 'Rabi\' al-Thani', 
              'Jumada al-Awwal', 'Jumada al-Thani', 'Rajab', 'Sha\'ban', 
              'Ramadan', 'Shawwal', 'Dhul Qa\'dah', 'Dhul Hijjah']
    
    # Sample date: 15 Sha'aban 1445
    return {
        "day": 15,
        "month": "Sha'aban",
        "year": 1445,
        "gregorian": "March 21, 2025"
    }