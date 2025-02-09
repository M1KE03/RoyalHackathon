import streamlit as st
import os
from document_upload import show_upload_tab
from document_qa import show_document_qa_tab
from general_qa import show_general_qa_tab
from quiz_generator import show_quiz_tab
from study_technique import show_study_technique_tab
from roulette_game import show_roulette_tab
from snack_suggestions import show_snack_tab
from playlist_suggestions import show_playlist_tab
from langchain_community.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
import torch

# Check if CUDA is available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize Streamlit app
st.title("Purrsonal Meowntor 😺")

# Initialize HuggingFace
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize model
if 'llm' not in st.session_state:
    st.session_state.llm = HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        task="text-generation",
        model_kwargs={
            "temperature": 0.5,
            "max_length": 512,
            "top_p": 0.9
        }
    )

# Initialize embeddings
if 'embeddings' not in st.session_state:
    st.session_state.embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': DEVICE}
    )

# Initialize session states
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["📤 Pawload Documents", "📚 Document Q&A", "🎯 Generate Quiz", "🤖 General CatChat", "⏱️ Pawmodoro Timer", "🎰 Roulette Game", "🐟 Snacks", "🎵 Meowsic"])
# Show each tab
with tab1:
    show_upload_tab()
    
with tab2:
    show_document_qa_tab()

with tab3:
    show_quiz_tab()
    
with tab4:
    show_general_qa_tab()
    
with tab5:
    show_study_technique_tab()
    
with tab6:
    show_roulette_tab()
    
with tab7:
    show_snack_tab()
    
with tab8:
    show_playlist_tab()