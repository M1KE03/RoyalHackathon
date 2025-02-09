import tkinter as tk
from tkinter import messagebox
import random
import os

# Initialize the window
root = tk.Tk()
root.title("Meowtivator")

# Set window size
root.geometry("500x500")

# Function to load images (supports PNG, GIF)
def load_images(image_folder):
    # Get the list of image files in the folder (support PNG, GIF)
    images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.gif'))]
    if not images:
        messagebox.showerror("Error", "Meowtivator is having some Cat'astrophes!")
        return None
    return images

# Path to the folder containing images
image_folder = r"F:\Python Files\Cat Pics"  # Use raw string to handle backslashes

# Load images from the folder
cat_images = load_images(image_folder)

# If no images were loaded, exit the program
if cat_images is None:
    root.quit()

# Function to display a random cat image
def meowtivate_me():
    # Choose a random image from the list
    random_cat_image = random.choice(cat_images)
    
    # Ensure the full path to the image is used
    img_path = os.path.join(image_folder, random_cat_image)
    
    try:
        # Open the image with Tkinter's PhotoImage
        img_tk = tk.PhotoImage(file=img_path)
        
        # Get the image's width and height
        img_width = img_tk.width()
        img_height = img_tk.height()
        
        # Set the maximum width and height for the image to fit in the window
        max_width = 400
        max_height = 400
        
        # Calculate the resizing scale
        if img_width > max_width or img_height > max_height:
            scale_factor = min(max_width / img_width, max_height / img_height)
            new_width = int(img_width * scale_factor)
            new_height = int(img_height * scale_factor)
            
            # Resize the image proportionally
            img_tk = img_tk.subsample(int(img_width / new_width), int(img_height / new_height))
        
        # Update the label with the new image
        label.config(image=img_tk)
        label.image = img_tk  # Keep a reference to the image
    except Exception as e:
        # In case of any error loading the image
        messagebox.showerror("Error", "Purrdon me! Something went wrong with loading the image.")

# Create the "Meowtivate Me" button
button = tk.Button(root, text="Meowtivate Me", command=meowtivate_me)
button.pack(pady=20)

# Create a label to display the cat image
label = tk.Label(root)
label.pack()

# Run the Tkinter event loop
root.mainloop()
