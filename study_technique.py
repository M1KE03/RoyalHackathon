import streamlit as st
import time
from datetime import datetime, timedelta

def format_time(seconds):
    """Convert seconds to MM:SS format"""
    return str(timedelta(seconds=seconds))[2:7]

def show_study_technique_tab():
    st.subheader("⏱️ Study Techniques & Timer")
    
    # Pomodoro Timer Section
    st.write("### 🍅 Pomodoro Timer")
    st.write("""
    The Pomodoro Technique is a time management method that uses a timer to break work into intervals, 
    traditionally 25 minutes in length, separated by short breaks.
    
    **How it works:**
    1. Choose your study and break durations
    2. Work focused during study sessions
    3. Take short breaks between sessions
    4. After 4 sessions, take a longer break
    """)
    
    # Timer Settings
    col1, col2, col3 = st.columns(3)
    
    with col1:
        study_duration = st.number_input(
            "Study Duration (minutes)", 
            min_value=1, 
            max_value=60, 
            value=25
        )
    
    with col2:
        break_duration = st.number_input(
            "Break Duration (minutes)", 
            min_value=1, 
            max_value=30, 
            value=5
        )
    
    with col3:
        num_sessions = st.number_input(
            "Number of Sessions", 
            min_value=1, 
            max_value=10, 
            value=4
        )
    
    # Initialize session state variables
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    if 'current_session' not in st.session_state:
        st.session_state.current_session = 1
    if 'is_break' not in st.session_state:
        st.session_state.is_break = False
    if 'time_remaining' not in st.session_state:
        st.session_state.time_remaining = study_duration * 60
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    
    # Timer Controls
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Start Timer" if not st.session_state.timer_running else "Pause Timer"):
            st.session_state.timer_running = not st.session_state.timer_running
            if st.session_state.timer_running:
                st.session_state.start_time = time.time()
    
    with col2:
        if st.button("Reset Timer"):
            st.session_state.timer_running = False
            st.session_state.current_session = 1
            st.session_state.is_break = False
            st.session_state.time_remaining = study_duration * 60
            st.session_state.start_time = None
            st.rerun()
    
    # Timer Display
    if st.session_state.timer_running:
        progress_bar = st.progress(0)
        time_display = st.empty()
        session_display = st.empty()
        
        while st.session_state.timer_running:
            if st.session_state.is_break:
                total_time = break_duration * 60
                activity = "Break"
            else:
                total_time = study_duration * 60
                activity = "Study"
            
            elapsed_time = time.time() - st.session_state.start_time
            remaining = max(0, st.session_state.time_remaining - int(elapsed_time))
            
            # Update displays
            progress = min(1.0, max(0.0, 1 - (remaining / total_time)))  # Ensure progress stays between 0 and 1
            progress_bar.progress(progress)
            time_display.markdown(f"### ⏰ {activity} Time Remaining: {format_time(remaining)}")
            session_display.write(f"Session {st.session_state.current_session} of {num_sessions}")
            
            if remaining <= 0:
                # Session complete
                if st.session_state.is_break:
                    st.session_state.is_break = False
                    st.session_state.time_remaining = study_duration * 60
                else:
                    if st.session_state.current_session < num_sessions:
                        st.session_state.current_session += 1
                        st.session_state.is_break = True
                        st.session_state.time_remaining = break_duration * 60
                    else:
                        st.balloons()
                        st.success("🎉 All sessions completed! Great job!")
                        st.session_state.timer_running = False
                        break
                
                st.session_state.start_time = time.time()
                st.rerun()
            
            time.sleep(0.1)
    
    # Study Tips Section
    st.write("### 📚 Study Tips")
    st.write("""
    **Effective Study Techniques:**
    1. **Active Recall**: Test yourself instead of re-reading
    2. **Spaced Repetition**: Review material at increasing intervals
    3. **Mind Mapping**: Create visual connections between concepts
    4. **Feynman Technique**: Explain concepts in simple terms
    5. **Pomodoro Method**: Study in focused intervals
    
    **Environment Setup:**
    - Find a quiet, well-lit space
    - Remove distractions (phone, social media)
    - Keep water and healthy snacks nearby
    - Take regular breaks
    - Get enough sleep
    """)
