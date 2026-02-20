# pages/how_to_use.py
import streamlit as st

def show():
    # Page Header
    st.markdown("""
    <div class='card'>
        <h2 class='card-title'>📘 How to Use NoorAI</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem;'>Your complete guide to the Islamic Guidance Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for different sections
    tabs = st.tabs(["🚀 Getting Started", "💭 Emotion Chat", "📖 Quran Reader", "📚 Scholar Tafsir", "📜 Hadith", "❓ FAQ"])
    
    with tabs[0]:  # Getting Started
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class='card'>
                <h3 style='color: #d4af37;'>🌟 Welcome to NoorAI</h3>
                <p style='color: #e8e8e8;'>NoorAI (نور الذكاء الاصطناعي) is your intelligent companion for exploring Islamic knowledge. Our platform combines traditional scholarship with modern AI technology.</p>
                
                <h4 style='color: #d4af37; margin-top: 1.5rem;'>🎯 Key Features</h4>
                <ul style='color: #e8e8e8;'>
                    <li><strong>🤖 Emotion Chat:</strong> Share feelings, receive Quranic verses</li>
                    <li><strong>📖 Quran Reader:</strong> Read Quran with AI-powered context</li>
                    <li><strong>👨‍🏫 Scholar Tafsir:</strong> Deep interpretations from 7+ scholars</li>
                    <li><strong>📚 Hadith Database:</strong> Access 40,000+ authentic hadith</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='card'>
                <h4 style='color: #d4af37;'>🕌 Quick Tips</h4>
                <p style='color: #c4a962;'>✓ Use the sidebar to navigate between pages</p>
                <p style='color: #c4a962;'>✓ Click emotion buttons for quick access</p>
                <p style='color: #c4a962;'>✓ Bookmark your favorite verses</p>
                <p style='color: #c4a962;'>✓ Check prayer times in sidebar</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='card'>
                <h4 style='color: #d4af37;'>📊 Platform Statistics</h4>
                <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;'>
                    <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                        <h2 style='color: #d4af37;'>114</h2>
                        <p style='color: #e8e8e8;'>Surahs</p>
                    </div>
                    <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                        <h2 style='color: #d4af37;'>6,236+</h2>
                        <p style='color: #e8e8e8;'>Ayahs</p>
                    </div>
                    <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                        <h2 style='color: #d4af37;'>7+</h2>
                        <p style='color: #e8e8e8;'>Scholars</p>
                    </div>
                    <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                        <h2 style='color: #d4af37;'>40k+</h2>
                        <p style='color: #e8e8e8;'>Hadith</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='card'>
                <h4 style='color: #d4af37;'>🎓 Supported Scholars</h4>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Ibn Kathir</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Tabari</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Qurtubi</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Sa'di</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Razi</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Baghawi</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.3rem 0.8rem; border-radius: 20px; color: #c4a962;'>Al-Shawkani</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:  # Emotion Chat
        st.markdown("""
        <div class='card'>
            <h3 style='color: #d4af37;'>💭 Using the Emotion Chat</h3>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Step-by-Step Guide:</h4>
            <ol style='color: #e8e8e8;'>
                <li><strong>Navigate to Home</strong> - This is the main chat page</li>
                <li><strong>Share your feelings</strong> - Type how you're feeling or use emotion buttons</li>
                <li><strong>AI analyzes</strong> - Our AI detects your emotion (sadness, anxiety, hope, etc.)</li>
                <li><strong>Receive guidance</strong> - Get a relevant Quranic verse with translation</li>
                <li><strong>Deepen understanding</strong> - Ask for tafsir from specific scholars</li>
            </ol>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Supported Emotions:</h4>
            <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>😊 Happiness</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>😢 Sadness</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>😨 Anxiety</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>😤 Anger</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>🤲 Gratitude</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>💫 Hope</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>😰 Fear</span>
                <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px;'>🕊️ Peace</span>
            </div>
            
            <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
                <p style='color: #c4a962;'><strong>💡 Tip:</strong> Be specific about your feelings for more accurate verses!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:  # Quran Reader
        st.markdown("""
        <div class='card'>
            <h3 style='color: #d4af37;'>📖 Quran Reader Guide</h3>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>How to Read Quran:</h4>
            <ul style='color: #e8e8e8;'>
                <li><strong>By Reference:</strong> Enter Surah (1-114) and verse numbers</li>
                <li><strong>By Keyword:</strong> Search for specific words (coming soon)</li>
                <li><strong>By Topic:</strong> Browse verses by theme (coming soon)</li>
            </ul>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Quick Access:</h4>
            <p style='color: #e8e8e8;'>Click on popular surah buttons for instant access to:</p>
            <ul style='color: #e8e8e8;'>
                <li>Al-Fatiha (The Opening) - Surah 1</li>
                <li>Al-Baqarah (The Cow) - Surah 2</li>
                <li>Yaseen - Surah 36</li>
                <li>Ar-Rahman (The Beneficent) - Surah 55</li>
                <li>Al-Mulk (The Sovereignty) - Surah 67</li>
                <li>Al-Ikhlas (Sincerity) - Surah 112</li>
            </ul>
            
            <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
                <p style='color: #c4a962;'><strong>📌 Note:</strong> All verses are fetched in real-time using AI from authentic sources.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:  # Scholar Tafsir
        st.markdown("""
        <div class='card'>
            <h3 style='color: #d4af37;'>📚 Scholar Tafsir Guide</h3>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Available Scholars:</h4>
            <table style='width: 100%; color: #e8e8e8; border-collapse: collapse;'>
                <tr style='border-bottom: 1px solid #c4a962;'>
                    <th style='padding: 0.5rem; color: #d4af37;'>Scholar</th>
                    <th style='padding: 0.5rem; color: #d4af37;'>Specialization</th>
                </tr>
                <tr>
                    <td style='padding: 0.5rem;'>Ibn Kathir</td>
                    <td style='padding: 0.5rem;'>Hadith-based interpretation</td>
                </tr>
                <tr>
                    <td style='padding: 0.5rem;'>Al-Tabari</td>
                    <td style='padding: 0.5rem;'>Linguistic analysis</td>
                </tr>
                <tr>
                    <td style='padding: 0.5rem;'>Al-Qurtubi</td>
                    <td style='padding: 0.5rem;'>Legal rulings</td>
                </tr>
                <tr>
                    <td style='padding: 0.5rem;'>Al-Sa'di</td>
                    <td style='padding: 0.5rem;'>Contemporary explanation</td>
                </tr>
                <tr>
                    <td style='padding: 0.5rem;'>Al-Razi</td>
                    <td style='padding: 0.5rem;'>Philosophical approach</td>
                </tr>
            </table>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>How to Use:</h4>
            <ol style='color: #e8e8e8;'>
                <li>Select a scholar from the dropdown</li>
                <li>Choose a surah and verse number</li>
                <li>Click "Get Tafsir" to receive detailed explanation</li>
                <li>Read the interpretation in the scholar's unique style</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[4]:  # Hadith
        st.markdown("""
        <div class='card'>
            <h3 style='color: #d4af37;'>📜 Hadith Specialist Guide</h3>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Major Hadith Collections:</h4>
            <ul style='color: #e8e8e8;'>
                <li><strong>Sahih Bukhari</strong> - Most authentic, 7,563 hadith</li>
                <li><strong>Sahih Muslim</strong> - Second most authentic, 7,563 hadith</li>
                <li><strong>Sunan Abu Dawud</strong> - Legal hadith, 5,274 hadith</li>
                <li><strong>Jami At-Tirmidhi</strong> - Includes grading, 3,956 hadith</li>
                <li><strong>Sunan Ibn Majah</strong> - 4,341 hadith</li>
                <li><strong>Sunan An-Nasai</strong> - 5,758 hadith</li>
            </ul>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Search Methods:</h4>
            <ul style='color: #e8e8e8;'>
                <li><strong>By Topic:</strong> Enter keywords like "prayer", "fasting", "charity"</li>
                <li><strong>Quick Topics:</strong> Click on popular topic buttons</li>
            </ul>
            
            <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
                <p style='color: #c4a962;'><strong>🔍 Example:</strong> Search "mercy" to find hadith about Allah's mercy</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[5]:  # FAQ
        st.markdown("""
        <div class='card'>
            <h3 style='color: #d4af37;'>❓ Frequently Asked Questions</h3>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: Is the content authentic?</h4>
            <p style='color: #e8e8e8;'>A: Yes! All Quranic verses and hadith are sourced from authentic references using AI trained on Islamic sources.</p>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: Do I need an account?</h4>
            <p style='color: #e8e8e8;'>A: No, NoorAI is completely free to use without registration.</p>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: Can I save my favorite verses?</h4>
            <p style='color: #e8e8e8;'>A: Bookmark feature is coming soon! For now, you can copy verses manually.</p>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: How accurate is emotion detection?</h4>
            <p style='color: #e8e8e8;'>A: We use Gemini AI for high accuracy, with keyword-based fallback for reliability.</p>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: Are prayer times accurate?</h4>
            <p style='color: #e8e8e8;'>A: Prayer times are samples. For accurate times, please check your local mosque.</p>
            
            <h4 style='color: #c4a962; margin-top: 1.5rem;'>Q: Can I request new features?</h4>
            <p style='color: #e8e8e8;'>A: Absolutely! We're constantly improving based on user feedback.</p>
        </div>
        """, unsafe_allow_html=True)