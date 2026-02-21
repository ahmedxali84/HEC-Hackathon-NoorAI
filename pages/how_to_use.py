# pages/how_to_use.py
import streamlit as st

def show():
    # Page Header
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem;'>
            <h2 style='color: #d4af37; font-size: 1.8rem; font-family: Amiri; margin-bottom: 0.5rem;'>📘 How to Use NoorAI</h2>
            <p style='color: #e8e8e8; font-size: 1.1rem;'>Your complete guide to the Islamic Guidance Platform</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Create tabs for different sections
    tabs = st.tabs(["🚀 Getting Started", "💭 Emotion Chat", "📖 Quran Reader", "📚 Scholar Tafsir", "📜 Hadith", "❓ FAQ"])
    
    with tabs[0]:  # Getting Started
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Welcome card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem; margin-bottom: 1rem;'>
                    <h3 style='color: #d4af37; margin-bottom: 1rem;'>🌟 Welcome to NoorAI</h3>
                    <p style='color: #e8e8e8; margin-bottom: 1rem;'>NoorAI (نور الذكاء الاصطناعي) is your intelligent companion for exploring Islamic knowledge. Our platform combines traditional scholarship with modern AI technology.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Quick tips card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                    <h4 style='color: #d4af37; margin-bottom: 1rem;'>🕌 Quick Tips</h4>
                    <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962;'>✓</span> Use the navigation menu at the top to switch between pages</p>
                    <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962;'>✓</span> Click emotion buttons for quick access</p>
                    <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962;'>✓</span> Bookmark your favorite verses (coming soon)</p>
                    <p style='color: #e8e8e8; margin-bottom: 0.5rem;'><span style='color: #c4a962;'>✓</span> Check prayer times in the info bar</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        with col2:
            # Statistics card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem; margin-bottom: 1rem;'>
                    <h4 style='color: #d4af37; margin-bottom: 1rem;'>📊 Platform Statistics</h4>
                    <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;'>
                        <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                            <h2 style='color: #d4af37; margin-bottom: 0.3rem;'>114</h2>
                            <p style='color: #e8e8e8;'>Surahs</p>
                        </div>
                        <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                            <h2 style='color: #d4af37; margin-bottom: 0.3rem;'>6,236+</h2>
                            <p style='color: #e8e8e8;'>Ayahs</p>
                        </div>
                        <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                            <h2 style='color: #d4af37; margin-bottom: 0.3rem;'>7+</h2>
                            <p style='color: #e8e8e8;'>Scholars</p>
                        </div>
                        <div style='text-align: center; background: rgba(196,169,98,0.1); padding: 1.5rem; border-radius: 15px;'>
                            <h2 style='color: #d4af37; margin-bottom: 0.3rem;'>40k+</h2>
                            <p style='color: #e8e8e8;'>Hadith</p>
                        </div>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Scholars card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                    <h4 style='color: #d4af37; margin-bottom: 1rem;'>🎓 Supported Scholars</h4>
                    <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Ibn Kathir</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Tabari</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Qurtubi</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Sa'di</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Razi</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Baghawi</span>
                        <span style='background: rgba(196,169,98,0.2); padding: 0.4rem 0.8rem; border-radius: 20px; color: #c4a962; font-size: 0.9rem;'>Al-Shawkani</span>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
    
    with tabs[1]:  # Emotion Chat
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <h3 style='color: #d4af37; margin-bottom: 1.5rem;'>💭 Using the Emotion Chat</h3>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Step-by-Step Guide:</h4>
                <ol style='color: #e8e8e8; margin-left: 1.5rem;'>
                    <li><strong>Navigate to Home</strong> - This is the main chat page</li>
                    <li><strong>Share your feelings</strong> - Type how you're feeling or use emotion buttons</li>
                    <li><strong>AI analyzes</strong> - Our AI detects your emotion (sadness, anxiety, hope, etc.)</li>
                    <li><strong>Receive guidance</strong> - Get a relevant Quranic verse with translation</li>
                    <li><strong>Deepen understanding</strong> - Ask for tafsir from specific scholars</li>
                </ol>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Supported Emotions:</h4>
                <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>😊 Happiness</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>😢 Sadness</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>😨 Anxiety</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>😤 Anger</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>🤲 Gratitude</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>💫 Hope</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>😰 Fear</span>
                    <span style='background: rgba(196,169,98,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #c4a962;'>🕊️ Peace</span>
                </div>
                
                <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
                    <p style='color: #c4a962;'><strong>💡 Tip:</strong> Be specific about your feelings for more accurate verses!</p>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with tabs[2]:  # Quran Reader
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <h3 style='color: #d4af37; margin-bottom: 1.5rem;'>📖 Quran Reader Guide</h3>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>How to Read Quran:</h4>
                <ul style='color: #e8e8e8; margin-left: 1.5rem;'>
                    <li><strong>By Reference:</strong> Enter Surah (1-114) and verse numbers</li>
                    <li><strong>By Keyword:</strong> Search for specific words (coming soon)</li>
                    <li><strong>By Topic:</strong> Browse verses by theme (coming soon)</li>
                </ul>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Quick Access:</h4>
                <p style='color: #e8e8e8; margin-bottom: 0.5rem;'>Click on popular surah buttons for instant access to:</p>
                <ul style='color: #e8e8e8; margin-left: 1.5rem;'>
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
            """, 
            unsafe_allow_html=True
        )
    
    with tabs[3]:  # Scholar Tafsir
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <h3 style='color: #d4af37; margin-bottom: 1.5rem;'>📚 Scholar Tafsir Guide</h3>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Available Scholars:</h4>
                <div style='overflow-x: auto;'>
                    <table style='width: 100%; color: #e8e8e8; border-collapse: collapse;'>
                        <tr style='border-bottom: 1px solid #c4a962;'>
                            <th style='padding: 0.5rem; text-align: left; color: #d4af37;'>Scholar</th>
                            <th style='padding: 0.5rem; text-align: left; color: #d4af37;'>Specialization</th>
                        </tr>
                        <tr>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Ibn Kathir</td>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Hadith-based interpretation</td>
                        </tr>
                        <tr>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Al-Tabari</td>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Linguistic analysis</td>
                        </tr>
                        <tr>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Al-Qurtubi</td>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Legal rulings</td>
                        </tr>
                        <tr>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Al-Sa'di</td>
                            <td style='padding: 0.5rem; border-bottom: 1px solid rgba(196,169,98,0.2);'>Contemporary explanation</td>
                        </tr>
                        <tr>
                            <td style='padding: 0.5rem;'>Al-Razi</td>
                            <td style='padding: 0.5rem;'>Philosophical approach</td>
                        </tr>
                    </table>
                </div>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>How to Use:</h4>
                <ol style='color: #e8e8e8; margin-left: 1.5rem;'>
                    <li>Select a scholar from the dropdown</li>
                    <li>Choose a surah and verse number</li>
                    <li>Click "Get Tafsir" to receive detailed explanation</li>
                    <li>Read the interpretation in the scholar's unique style</li>
                </ol>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with tabs[4]:  # Hadith
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <h3 style='color: #d4af37; margin-bottom: 1.5rem;'>📜 Hadith Specialist Guide</h3>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Major Hadith Collections:</h4>
                <ul style='color: #e8e8e8; margin-left: 1.5rem;'>
                    <li><strong>Sahih Bukhari</strong> - Most authentic, 7,563 hadith</li>
                    <li><strong>Sahih Muslim</strong> - Second most authentic, 7,563 hadith</li>
                    <li><strong>Sunan Abu Dawud</strong> - Legal hadith, 5,274 hadith</li>
                    <li><strong>Jami At-Tirmidhi</strong> - Includes grading, 3,956 hadith</li>
                    <li><strong>Sunan Ibn Majah</strong> - 4,341 hadith</li>
                    <li><strong>Sunan An-Nasai</strong> - 5,758 hadith</li>
                </ul>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 1rem 0;'>Search Methods:</h4>
                <ul style='color: #e8e8e8; margin-left: 1.5rem;'>
                    <li><strong>By Topic:</strong> Enter keywords like "prayer", "fasting", "charity"</li>
                    <li><strong>Quick Topics:</strong> Click on popular topic buttons</li>
                </ul>
                
                <div style='background: rgba(196,169,98,0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
                    <p style='color: #c4a962;'><strong>🔍 Example:</strong> Search "mercy" to find hadith about Allah's mercy</p>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with tabs[5]:  # FAQ
        st.markdown(
            """
            <div style='background: linear-gradient(135deg, #1a2a3a, #152238); border: 1px solid #c4a962; border-radius: 15px; padding: 1.5rem;'>
                <h3 style='color: #d4af37; margin-bottom: 1.5rem;'>❓ Frequently Asked Questions</h3>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: Is the content authentic?</h4>
                <p style='color: #e8e8e8; margin-bottom: 1rem;'>A: Yes! All Quranic verses and hadith are sourced from authentic references using AI trained on Islamic sources.</p>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: Do I need an account?</h4>
                <p style='color: #e8e8e8; margin-bottom: 1rem;'>A: No, NoorAI is completely free to use without registration.</p>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: Can I save my favorite verses?</h4>
                <p style='color: #e8e8e8; margin-bottom: 1rem;'>A: Bookmark feature is coming soon! For now, you can copy verses manually.</p>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: How accurate is emotion detection?</h4>
                <p style='color: #e8e8e8; margin-bottom: 1rem;'>A: We use Gemini AI for high accuracy, with keyword-based fallback for reliability.</p>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: Are prayer times accurate?</h4>
                <p style='color: #e8e8e8; margin-bottom: 1rem;'>A: Prayer times are samples. For accurate times, please check your local mosque.</p>
                
                <h4 style='color: #c4a962; margin: 1.5rem 0 0.5rem 0;'>Q: Can I request new features?</h4>
                <p style='color: #e8e8e8;'>A: Absolutely! We're constantly improving based on user feedback.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
