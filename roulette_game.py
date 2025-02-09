import streamlit as st
import random
import time
import pandas as pd  # Add this import for DataFrame functionality

def show_roulette_tab():
    st.subheader("🎰 Study Break Roulette")
    
    # Initialize session state for chips if not exists
    if 'chips' not in st.session_state:
        st.session_state.chips = 0
    
    # Initialize roulette game state
    if 'spinning' not in st.session_state:
        st.session_state.spinning = False
    if 'last_result' not in st.session_state:
        st.session_state.last_result = None
    if 'bet_history' not in st.session_state:
        st.session_state.bet_history = []
    
    # Display current chips
    st.write(f"### 💰 Your Chips: £{st.session_state.chips}")
    
    # Game instructions
    st.write("""
    **How to Play:**
    1. Place your bet (must have chips from completing quizzes)
    2. Choose even or odd numbers
    3. If you win, you double your bet!
    4. If you lose, you lose your bet
    5. Use your winnings for extra study breaks!
    """)
    
    # Betting interface
    if st.session_state.chips > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            bet_amount = st.number_input(
                "Place your bet:",
                min_value=1,
                max_value=st.session_state.chips,
                value=min(5, st.session_state.chips)
            )
        
        with col2:
            bet_type = st.selectbox(
                "Choose your bet:",
                ["Even", "Odd"]
            )
        
        if st.button("🎲 Spin the Wheel!"):
            st.session_state.spinning = True
            
            # Spinning animation
            with st.spinner("🎰 Wheel spinning..."):
                time.sleep(2)  # Add suspense
                
                # Generate result
                result = random.randint(0, 36)
                is_even = result % 2 == 0
                
                # Determine win/loss
                if (bet_type == "Even" and is_even) or (bet_type == "Odd" and not is_even):
                    st.session_state.chips += bet_amount
                    outcome = "won"
                    st.balloons()
                else:
                    st.session_state.chips -= bet_amount
                    outcome = "lost"
                
                # Store result
                st.session_state.last_result = {
                    "number": result,
                    "bet_amount": bet_amount,
                    "bet_type": bet_type,
                    "outcome": outcome
                }
                
                # Add to history
                st.session_state.bet_history.append(st.session_state.last_result)
                
                st.rerun()
    
    else:
        st.warning("🎯 Complete quizzes to earn chips for playing!")
    
    # Display last result
    if st.session_state.last_result:
        result = st.session_state.last_result
        if result["outcome"] == "won":
            st.success(f"🎉 You won! The wheel landed on {result['number']}. You earned £{result['bet_amount']}!")
        else:
            st.error(f"😢 You lost! The wheel landed on {result['number']}. You lost £{result['bet_amount']}.")
    
    # Display betting history
    if st.session_state.bet_history:
        st.write("### 📜 Betting History")
        history_df = pd.DataFrame(st.session_state.bet_history)
        history_df.index = range(1, len(history_df) + 1)
        st.dataframe(history_df)
    
    # Study break conversion
    if st.session_state.chips > 0:
        st.write("### 🕒 Convert Chips to Break Time")
        st.write("Every £5 in chips = 5 minutes of extra break time!")
        
        break_chips = st.number_input(
            "How many chips would you like to convert to break time?",
            min_value=5,
            max_value=st.session_state.chips - (st.session_state.chips % 5),
            step=5
        )
        
        if st.button("Convert to Break Time"):
            break_minutes = (break_chips // 5) * 5
            st.session_state.chips -= break_chips
            
            st.success(f"🎉 Converted £{break_chips} to {break_minutes} minutes of break time!")
            
            # Could integrate with the study timer here
            if 'break_time_earned' not in st.session_state:
                st.session_state.break_time_earned = 0
            st.session_state.break_time_earned += break_minutes
