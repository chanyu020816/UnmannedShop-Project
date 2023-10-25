import tkinter as tk  # PEP8: `import *` is not preferred
from PIL import Image, ImageTk
import cv2


# --- functions ---

def show_frame():
    global image_id  # inform function to assign new value to global variable instead of local variable

    # get frame
    ret, frame = cap.read()

    if ret:
        # cv2 uses `BGR` but `GUI` needs `RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # convert to PIL image
        img = Image.fromarray(frame)

        # convert to Tkinter image
        photo = ImageTk.PhotoImage(image=img)

        # solution for bug in `PhotoImage`
        canvas.photo = photo

        # check if image already exists
        if image_id:
            # replace image in PhotoImage on canvas
            canvas.itemconfig(image_id, image=photo)
        else:
            # create first image on canvas and keep its ID
            image_id = canvas.create_image((0, 0), image=photo, anchor='nw')
            # resize canvas
            canvas.configure(width=photo.width(), height=photo.height())

    # run again after 20ms (0.02s)
    root.after(20, show_frame)


# --- main ---

image_id = None  # default value at start (to create global variable)

cap = cv2.VideoCapture(0)

root = tk.Tk()

# create a Label to display frames
canvas = tk.Canvas(root)
canvas.pack(fill='both', expand=True)

# start function which shows frame
show_frame()

root.mainloop()

cap.release()