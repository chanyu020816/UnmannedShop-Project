import tkinter as tk
import cv2
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.capturing = False
        self.captured_image = None

        # Create a label to display the webcam feed or captured image
        self.label = tk.Label(window)
        self.label.pack()

        # Create a button to capture a picture
        self.capture_button = tk.Button(window, text="Capture", command=self.capture)
        self.capture_button.pack()

        # Open the webcam
        self.cap = cv2.VideoCapture(0)

        # After initializing, start the webcam feed
        self.update()

        # Set a flag to capture an image
       
    def update(self):
        if self.captured_image is not None:
            # Display the captured image
            self.photo = ImageTk.PhotoImage(image=self.captured_image)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            ret, frame = self.cap.read()
            if ret:
                # Convert the OpenCV frame to a PhotoImage
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(img))
                self.label.config(image=self.photo)
                self.label.image = self.photo
            self.window.after(10, self.update)

    def capture(self):
        self.capturing = True

        # Capture a frame
        ret, frame = self.cap.read()
        if ret:
            # Convert the captured frame to a PhotoImage
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(img))

        self.capturing = False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root, "Webcam Capture App")
    app.run()

