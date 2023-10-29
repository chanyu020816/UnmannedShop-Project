import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create a Tkinter window
root = tk.Tk()
root.title("Image Upload and Display")

# Create a Canvas to display the image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Function to upload and display an image
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm")])
    
    if file_path:
        # Open and display the selected image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo  # Keep a reference to the image to prevent it from being garbage collected

# Create an "Upload Image" button
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Run the Tkinter main loop
root.mainloop()

