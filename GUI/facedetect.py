import tkinter as tk
from tkinter import messagebox
import cv2

# Initialize variables for storing the detected face and username
detected_face = None
username_var = None  # Moved variable initialization to after root window creation

# Create the main window
root = tk.Tk()
root.title("Face Detection Login")
# Function to check if a face is detected
def check_face():
    global detected_face
    if detected_face is not None:
        messagebox.showinfo("Face Detection", "Face detected.")
        username_var.set("YourUsername")  # Set the username automatically
    else:
        messagebox.showinfo("Face Detection", "No face detected.")

# Function to handle login
def login():
    username = username_var.get()
    password = password_entry.get()

    # Add your login logic here

    if username == "YourUsername" and password == "your_password":
        messagebox.showinfo("Login", "Login successful.")
    else:
        messagebox.showinfo("Login", "Login failed. Please check your credentials.")

# Function to capture video frames and detect faces
def capture_and_detect():
    global detected_face

    video_capture = cv2.VideoCapture(0)  # Use the default camera (change to the desired camera if needed)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            detected_face = frame[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("Face Detection Login")

# Right side (Login interface)
frame_right = tk.Frame(root)
frame_right.grid(row=0, column=1, padx=10, pady=10)

login_label = tk.Label(frame_right, text="Login")
login_label.pack()

username_label = tk.Label(frame_right, text="Username")
username_label.pack()
username_entry = tk.Entry(frame_right, textvariable=username_var, state="readonly")
username_entry.pack()

password_label = tk.Label(frame_right, text="Password")
password_label.pack()
password_entry = tk.Entry(frame_right, show="*")
password_entry.pack()

login_button = tk.Button(frame_right, text="Login", command=login)
login_button.pack()

# Left side (Face detection)
frame_left = tk.Frame(root)
frame_left.grid(row=0, column=0, padx=10, pady=10)

face_label = tk.Label(frame_left, text="Face Detection")
face_label.pack()

capture_button = tk.Button(frame_left, text="Capture Face", command=capture_and_detect)
capture_button.pack()

check_face_button = tk.Button(frame_left, text="Check Face", command=check_face)
check_face_button.pack()

root.mainloop()
