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
from study_planner import show_planner_tab
from meowtivator import show_meowtivator_tab
from langchain_community.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
import torch

# Check if CUDA is available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize Streamlit app
col1, col2 = st.columns([0.15, 0.85])  # Adjust ratio for logo and title
with col1:
    st.image("assets/logo.png", width=80)  # Adjust width as needed
with col2:
    st.title("Purrsonal Meowntor")

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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10= st.tabs(["📤 Pawload Documents", "📚 Document Q&A", "🎯 Generate Quiz", "🤖 General CatChat", "⏱️ Pawmodoro Timer", "🎰 Roulette Game", "🐟 Snacks", "🎵 Meowsic", "📝 Clawendar", "😺 Meowtivator"])
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
    
with tab9:
    show_planner_tab()
    
with tab10:
    show_meowtivator_tab()

# Add custom background and styling
st.markdown("""
<style>
    /* Import local font files */
    @font-face {
        font-family: 'VCR OSD Mono';
        src: url('assets/fonts/VCR_OSD_MONO_1.001.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }
    
    /* Apply font globally */
    * {
        font-family: 'VCR OSD Mono', monospace !important;
        color: white !important;
        text-shadow: -1px -1px 0 #000,
                     1px -1px 0 #000,
                    -1px  1px 0 #000,
                     1px  1px 0 #000;
    }
    
    /* Main background */
    .stApp {
        background-color: #FF9899 !important;
    }
    
    /* Make the main content area slightly transparent */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Style headers */
    h1, h2, h3, .css-10trblm, .css-1q8dd3e {
        color: #1e1e1e;
    }
    
    /* Style text */
    .stMarkdown, p, span, div, label, .css-1vbkxwb {
        color: #2c3e50;
    }
    
    /* Style sidebar */
    .css-1d391kg, .css-1p05t8e {
        background-color: rgba(255, 255, 255, 0.92);
    }
    
    /* Override tab colors specifically */
    .stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] {
        background-color: #FFE5B4;
        color: white !important;
        text-shadow: -1px -1px 0 #000,
                     1px -1px 0 #000,
                    -1px  1px 0 #000,
                     1px  1px 0 #000;
    }
    
    .stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #FFE5B4;
        color: white !important;
        text-shadow: -1px -1px 0 #000,
                     1px -1px 0 #000,
                    -1px  1px 0 #000,
                     1px  1px 0 #000;
    }
    
    /* Style buttons */
    .stButton button {
        font-weight: normal;
    }
    
    /* Style input fields */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        font-weight: normal;
    }
    
    /* Additional Streamlit-specific elements */
    .css-1p05t8e, .css-1vbkxwb, .css-10trblm, .css-1q8dd3e {
        font-family: 'VCR OSD Mono', monospace !important;
    }
</style>
""", unsafe_allow_html=True)