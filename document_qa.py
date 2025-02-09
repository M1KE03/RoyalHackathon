import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def show_document_qa_tab():
    st.subheader("❓ Ask Questions About Your Purrcuments")
    if st.session_state.vector_store is not None:
        query = st.text_input("What would you like to know about your documents?", key="doc_query")
        
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
                
                with st.spinner('Finding answer...'):
                    result = qa_chain({"question": query})
                    answer = result["answer"]
                    if "Use the following pieces of context" in answer:
                        answer = answer.split("Helpful Answer:")[-1].strip()
                    if "Question:" in answer:
                        answer = answer.split("Question:")[0].strip()
                    answer = answer.replace("Answer:", "").strip()
                    
                    st.write("### Answer:")
                    st.write(answer)
                    st.session_state.chat_history.append((query, answer))
                    
                    if st.session_state.chat_history:
                        st.subheader("💬 Document Chat History")
                        for q, a in st.session_state.chat_history:
                            st.write(f"**Q:** {q}")
                            st.write(f"**A:** {a}")
                            st.write("---")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.info("Please upload some documents in the 'Upload Documents' tab to get started!")