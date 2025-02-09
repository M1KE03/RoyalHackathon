import streamlit as st
import random

def get_playlist_suggestions(preferences):
    """Get playlist suggestions based on user preferences"""
    playlists_db = {
        'classical': {
            'focus': [
                {'name': 'Bach Study Session', 'link': 'https://open.spotify.com/playlist/1gLdWsGiKPBg3zjgF9RoPB'},
                {'name': 'Classical Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0'},
                {'name': 'Piano Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX7K31D69s4M1'}
            ],
            'relaxed': [
                {'name': 'Peaceful Piano', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO'},
                {'name': 'Classical Sleep', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX8Sz1gsYZdwj'}
            ]
        },
        'lofi': {
            'focus': [
                {'name': 'lofi beats', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn'},
                {'name': 'Study Lofi', 'link': 'https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM'}
            ],
            'relaxed': [
                {'name': 'Chill Lofi', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn'},
                {'name': 'Coffee Shop Lofi', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX9RwfGbeGQwP'}
            ]
        },
        'jazz': {
            'focus': [
                {'name': 'Jazz for Study', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX2vYju3i0lNX'},
                {'name': 'Coffee Table Jazz', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWV7EzJMK2FUI'}
            ],
            'relaxed': [
                {'name': 'Jazz Vibes', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX0SM0LYsmbMT'},
                {'name': 'Late Night Jazz', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4wta20PHgwo'}
            ]
        },
        'ambient': {
            'focus': [
                {'name': 'Deep Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ'},
                {'name': 'Space Ambient', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX1n9whBbBKoL'}
            ],
            'relaxed': [
                {'name': 'Ambient Relaxation', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY'},
                {'name': 'Nature Sounds', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8'}
            ]
        },
        'electronic': {
            'focus': [
                {'name': 'Electronic Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX0jgyAiPl8Af'},
                {'name': 'Coding Electronic', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX5trt9i14X7j'}
            ],
            'relaxed': [
                {'name': 'Chill Electronic', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX0jgyAiPl8Af'},
                {'name': 'Electronic Ambient', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7'}
            ]
        },
        'nature sounds': {
            'focus': [
                {'name': 'Rain Sounds', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8'},
                {'name': 'Forest Ambience', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8'}
            ],
            'relaxed': [
                {'name': 'Ocean Waves', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8'},
                {'name': 'Peaceful Nature', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8'}
            ]
        },
        'instrumental rock': {
            'focus': [
                {'name': 'Instrumental Rock Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U'},
                {'name': 'Guitar Instrumentals', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX5rhFKrRmLYn'}
            ],
            'relaxed': [
                {'name': 'Chill Rock', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX2UgsUIg75Vg'},
                {'name': 'Acoustic Chill', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4E3UdUs7fUx'}
            ]
        },
        'world music': {
            'focus': [
                {'name': 'World Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DWUVpAXiEPK8P'},
                {'name': 'Global Meditation', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4KEPL6iKDpn'}
            ],
            'relaxed': [
                {'name': 'World Chill', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4KEPL6iKDpn'},
                {'name': 'Global Vibes', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4KEPL6iKDpn'}
            ]
        },
        'white noise': {
            'focus': [
                {'name': 'White Noise Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4DydzGCFY3q'},
                {'name': 'Study White Noise', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4DydzGCFY3q'}
            ],
            'relaxed': [
                {'name': 'Sleep White Noise', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4DydzGCFY3q'},
                {'name': 'Calm White Noise', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX4DydzGCFY3q'}
            ]
        },
        'meditation': {
            'focus': [
                {'name': 'Focus Meditation', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX9uKNf5jGX6m'},
                {'name': 'Zen Focus', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX9uKNf5jGX6m'}
            ],
            'relaxed': [
                {'name': 'Deep Meditation', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX9uKNf5jGX6m'},
                {'name': 'Mindfulness', 'link': 'https://open.spotify.com/playlist/37i9dQZF1DX9uKNf5jGX6m'}
            ]
        }
    }
    
    suggestions = []
    for genre in preferences['genres']:
        if genre in playlists_db:
            mood_playlists = playlists_db[genre][preferences['mood']]
            suggestions.extend(random.sample(mood_playlists, min(2, len(mood_playlists))))
    
    return suggestions

def show_playlist_tab():
    st.subheader("🎵 Study Music Suggestions")
    
    st.write("""
    Music can help you focus and maintain a productive study session. 
    Let's find the perfect playlist for your study mood!
    """)
    
    # Get user preferences
    col1, col2 = st.columns(2)
    
    with col1:
        genres = st.multiselect(
            "Select your preferred music genres:",
            ["classical", "lofi", "jazz", "ambient", "electronic", 
             "nature sounds", "instrumental rock", "world music", 
             "white noise", "meditation"],
            default=["lofi"]
        )
    
    with col2:
        mood = st.radio(
            "What's your study mood?",
            ["focus", "relaxed"],
            index=0
        )
    
    if st.button("Get Playlist Suggestions"):
        if not genres:
            st.warning("Please select at least one genre!")
            return
            
        preferences = {
            'genres': genres,
            'mood': mood
        }
        
        suggestions = get_playlist_suggestions(preferences)
        
        if suggestions:
            st.write("### 🎧 Here are your personalized playlist suggestions:")
            
            for i, playlist in enumerate(suggestions, 1):
                st.markdown(f"""
                <div style="
                    background-color: #f0f2f6;
                    padding: 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                    color: #0F1116;
                    font-weight: 500;
                    border-left: 4px solid #1e88e5;
                ">
                    <div style="font-size: 1.1em; margin-bottom: 5px;">{i}. {playlist['name']}</div>
                    <a href="{playlist['link']}" target="_blank" style="color: #1e88e5;">
                        Open in Spotify 🎵
                    </a>
                </div>
                """, unsafe_allow_html=True)
            
            st.write("""
            ### 🎵 Tips for Study Music:
            - Keep the volume at a moderate level
            - Use instrumental versions when studying with language
            - Try different genres to find what works best
            - Create a dedicated study playlist to build routine
            - Use noise-canceling headphones if available
            """)
            
            st.info("""
            💡 **Pro Tip**: Studies show that music between 60-80 BPM (beats per minute) 
            is optimal for focus and concentration!
            """)
        else:
            st.error("No playlists found matching your preferences. Try different options!")