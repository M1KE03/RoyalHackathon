import streamlit as st
import os
from PyPDF2 import PdfReader
import docx
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

def process_file(file):
    """Process uploaded files (PDF, DOCX, TXT)"""
    text = ""
    file_extension = os.path.splitext(file.name)[1].lower()
    
    try:
        if file_extension == '.pdf':
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        elif file_extension == '.docx':
            doc = docx.Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file_extension == '.txt':
            text = file.getvalue().decode("utf-8")
        
        return text.strip()
    except Exception as e:
        st.error(f"Error processing {file.name}: {str(e)}")
        return None

def update_vector_store(text):
    """Update vector store with new document content"""
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        if st.session_state.vector_store is None:
            st.session_state.vector_store = FAISS.from_texts(chunks, st.session_state.embeddings)
        else:
            st.session_state.vector_store.add_texts(chunks)
            
        return True
    except Exception as e:
        st.error(f"Error updating vector store: {str(e)}")
        return False

def show_upload_tab():
    st.subheader("📄 Upload Study Materials")
    uploaded_files = st.file_uploader(
        "Upload your documents (PDF, DOCX, TXT)", 
        type=['pdf', 'docx', 'txt'],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            with st.spinner(f'Processing {file.name}...'):
                text = process_file(file)
                if text and update_vector_store(text):
                    st.success(f"{file.name} processed successfully!")