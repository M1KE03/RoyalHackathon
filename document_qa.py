import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def show_document_qa_tab():
    # Add custom styling for the Q&A section
    st.markdown("""
    <style>
        .qa-header {
            text-align: center;
            padding: 20px;
            margin-bottom: 30px;
        }
        
        .qa-logo {
            display: block;
            margin: auto;
            margin-bottom: 20px;
        }
        
        .qa-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .qa-question {
            background-color: #ffffff;
            padding: 15px;
            border-left: 4px solid #1e88e5;
            border-radius: 5px;
            margin: 10px 0;
        }
        
        .qa-answer {
            background-color: #e3f2fd;
            padding: 15px;
            border-left: 4px solid #4caf50;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Ask Questions About Your Purrcuments 📚</h2>", unsafe_allow_html=True)

    try:
        # Center the image using columns
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown('<div class="center-image">', unsafe_allow_html=True)
            st.image("assets/documentqa.png", width=200)  # Add your image here
            st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        pass  # Silently handle missing image
    
    
    if st.session_state.vector_store is not None:
        # Create a styled container for the Q&A interface
        st.markdown('<div class="qa-container">', unsafe_allow_html=True)
        
        query = st.text_input(
            "What would you like to know about your documents?",
            key="doc_query",
            placeholder="Ask me anything about your documents..."
        )
        
        if query:
            try:
                memory = ConversationBufferMemory(
                    memory_key="chat_history",
                    return_messages=True,
                    output_key="answer"
                )
                
                qa_chain = ConversationalRetrievalChain.from_llm(
                    llm=st.session_state.llm,
                    retriever=st.session_state.vector_store.as_retriever(
                        search_kwargs={"k": 3}
                    ),
                    memory=memory,
                    return_source_documents=False,
                    verbose=False
                )
                
                with st.spinner('😺 Searching through your documents...'):
                    result = qa_chain({"question": query})
                    answer = result["answer"]
                    if "Use the following pieces of context" in answer:
                        answer = answer.split("Helpful Answer:")[-1].strip()
                    if "Question:" in answer:
                        answer = answer.split("Question:")[0].strip()
                    answer = answer.replace("Answer:", "").strip()
                    
                    # Display the Q&A with styling
                    st.markdown('<div class="qa-question">', unsafe_allow_html=True)
                    st.markdown(f"**Q:** {query}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('<div class="qa-answer">', unsafe_allow_html=True)
                    st.markdown(f"**A:** {answer}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.session_state.chat_history.append((query, answer))
                    
                    if st.session_state.chat_history:
                        st.markdown("### 💬 Previous Questions & Answers")
                        for q, a in st.session_state.chat_history[:-1]:  # Skip the last one as it's already displayed
                            st.markdown('<div class="qa-question">', unsafe_allow_html=True)
                            st.markdown(f"**Q:** {q}")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            st.markdown('<div class="qa-answer">', unsafe_allow_html=True)
                            st.markdown(f"**A:** {a}")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            st.markdown("<hr>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Please upload some documents in the 'Upload Documents' tab to get started! 📤")