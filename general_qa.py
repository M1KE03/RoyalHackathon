import streamlit as st

def show_general_qa_tab():
    st.subheader("💭 Ask Meowntor Anything")
    try:
        # Center the image using columns
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown('<div class="center-image">', unsafe_allow_html=True)
            st.image("assets/general.png", width=200)  # Add your image here
            st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        pass  # Silently handle missing image
    
    
    general_query = st.text_input("Ask any question!", key="general_query")
    
    if general_query:
        try:
            with st.spinner('Thinking...'):
                prompt = f"""
                Question: {general_query}
                Please provide a clear and concise answer.
                """
                
                response = st.session_state.llm(prompt)
                answer = response.replace("Answer:", "").strip()
                
                st.write("### Answer:")
                st.write(answer)
                
                if 'general_chat_history' not in st.session_state:
                    st.session_state.general_chat_history = []
                st.session_state.general_chat_history.append((general_query, answer))
                
                if st.session_state.general_chat_history:
                    st.subheader("💬 General Chat History")
                    for q, a in st.session_state.general_chat_history:
                        st.write(f"**Q:** {q}")
                        st.write(f"**A:** {a}")
                        st.write("---")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")