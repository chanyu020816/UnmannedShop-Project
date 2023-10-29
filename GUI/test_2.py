import tkinter as tk
import cv2
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Create a label to display the webcam feed
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
        self.capturing = False

    def update(self):
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
            # Save the captured frame as an image file
            cv2.imwrite("captured_image.png", frame)
            print("Image captured as 'captured_image.png'")

        self.capturing = False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root, "Webcam Capture App")
    app.run()

