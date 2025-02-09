import streamlit as st
import random
import os
from PIL import Image

def show_meowtivator_tab():
    try:
        st.markdown("<h2 style='text-align: center;'>😺 Meowtivator 😺</h2>", unsafe_allow_html=True)
        
        # Path to the folder containing images
        image_folder = "assets/catpics"
        
        # Get list of image files
        cat_images = [f for f in os.listdir(image_folder) 
                     if f.lower().endswith(('.png', '.gif', '.jpg', '.jpeg'))]
        
        if not cat_images:
            st.error("No cat pictures found! Please add some pictures to assets/catpics folder.")
            return
        
        # Center the content
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            # Select and display random image
            if 'current_image' not in st.session_state:
                st.session_state.current_image = random.choice(cat_images)
            
            image_path = os.path.join(image_folder, st.session_state.current_image)
            try:
                image = Image.open(image_path)
                st.image(image, width=400)  # Display image with fixed width
            except Exception as e:
                st.error("Error loading image!")
            
            # Add meowtivate button
            if st.button("🐱 Meowtivate Me! 🐱"):
                st.session_state.current_image = random.choice(cat_images)
                st.rerun()
    except Exception as e:
        st.error(f"Error in show_meowtivator_tab: {e}") 