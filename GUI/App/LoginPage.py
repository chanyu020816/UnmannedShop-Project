import tkinter as tk
from PIL import ImageTk, Image
from ImageConvertResult import LoginFaceDetectPageBg
import base64
from io import BytesIO
from sys import platform
# if the operate system is macos, Button should be imported from tkmascos
if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button
from google.cloud import bigquery
from google.oauth2 import service_account
import uuid
from constant import *
import cv2
import cvzone
import face_recognition
import pickle
from numpy import argmin

# set up webcam
cap = cv2.VideoCapture(0)
# load face images encode file
file = open("./EncodeFile.p", "rb")
encodeListwithIDs = pickle.load(file)
encodeListKnow, IDs = encodeListwithIDs
file.close()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller

        # load background image
        byte_data = base64.b64decode(LoginFaceDetectPageBg)
        image_data = BytesIO(byte_data)

        # set windows size
        self.bg_frame = Image.open(image_data)
        desired_width = 1400
        desired_height = 800
        resized_bg = self.bg_frame.resize((desired_width, desired_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_bg)
        self.bg_panel = tk.Label(self, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # set up parameters
        self.user_not_found_label = None
        self.password_error = None
        self.FaceDetectUserID = None
        self.username_status = 0
        self.password_status = 0
        self.detect_status = 0

        # set up the frame's dimensions
        self.configure(width=1400, height=800)
        self.grid_propagate(False)
        self.grid()

        # DataBase connection
        credentials = service_account.Credentials.from_service_account_file('./unmannedshop-3444ca55864c.json')
        project_id = PROJECT_ID
        self.client = bigquery.Client(credentials=credentials, project=project_id)

        # main page
        self.create_login_page()

    def create_login_page(self):

        ## TITLE ##
        UserLogin_Title = tk.Label(self, text = "User    Login", font=("Canva Sans", 35, "bold"), bg="#FFF3F3", fg="#4f4e4d")
        UserLogin_Title.place(x=970, y=140)

        ## FaceRecog TITLE ##
        FaceRecog_Title = tk.Label(self, text="Facial    Login", font=("Canva Sans", 30, "bold"), bg="#FFFFFF",
                                   fg="#4f4e4d")
        FaceRecog_Title.place(x=280, y=170)
        canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, borderwidth = 0, border=0, relief="solid", width = 350, highlightthickness=0)
        canvas.place(x=180, y=220)

        self.UnDetectedLabel = tk.Label(self, text="In the process of facial recognition...",
                                        font=("yu gothic ui", 21, "bold"), bg="#FFFFFF", fg="#4f4e4d")
        if self.detect_status == 0:
            self.UnDetectedLabel.place(x=185, y=550)

        ## USERNAME ##
        username_label = tk.Label(self, text="Username / Email", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        username_label.place(x = 780, y = 210)
        username = tk.StringVar()
        self.username_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("Helvetica", 18, "bold"), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = username)
        self.username_entry.place(x=780, y=250, width=550, height=30)

        ## PASSWORD ##
        password_label = tk.Label(self, text="Password", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_label.place(x = 780, y = 290)
        password = tk.StringVar()
        self.password_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground='#6b6a69', borderwidth=7,
                                    textvariable=password, show="*")
        self.password_entry.place(x = 780, y = 330, width = 550, height = 30)

        create_account_button = Button(self, text="Create   Account", command=self.toCreateAccountPage, padx = 10, pady = 8,
            bg = "#DF3F3F", bd = 0, font = ("Open Sans", 20, "bold"), activebackground = "#FF3A3A",
            activeforeground = "white", fg = "white", highlightthickness = 0, borderwidth = 0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width = 250)
        create_account_button.place(x=780, y=600)

        submit_button = Button(self, text="Login", command= lambda: self.submit(username, password), padx=10, pady=8,
            bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground="white", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=250)
        submit_button.place(x=1080, y=600)

        resetFD_button = Button(self, text="Reset", command=self.resetFD,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
            activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0, borderwidth=0,
            highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=250, height=40)
        resetFD_button.place(x=235, y=600)
        # start the video capture
        self.show_frame(canvas)

    def submit(self, username, password):
        username_input = username.get()
        password_input = password.get()


        # if "@" in the username_input, it is email
        if "@" in username_input:
            # search by email
            query = f"SELECT password FROM unmannedshop.TestUserInfoFull WHERE email = '{username_input}';"
        else:
            # search by username
            query = f"SELECT password FROM unmannedshop.TestUserInfoFull WHERE username = '{username_input}';"

        query_job = self.client.query(query)
        result = query_job.result()

        # if username/email not found
        user_not_foundps = uuid.uuid1()
        true_password = str(user_not_foundps) + SECRET_CODE

        if result.total_rows == 0:
            # check if the "User not found" label already exists and forget it
            if self.user_not_found_label:
                self.user_not_found_label.place_forget()
            self.user_not_found_label = tk.Label(self, text="Username or Email not found, please try again.",
                bg="#FFF3F3", fg="red", font=("Open Sans", 18))
            self.user_not_found_label.place(x=783, y=360)
        else:
            # clear the "User not found" label if it exists
            if self.user_not_found_label:
                self.user_not_found_label.place_forget()
            for row in result:
                true_password = row.password

        if true_password != str(user_not_foundps) + SECRET_CODE:
            if password_input == true_password:
                self.controller.show_object_detection_page()
                if self.password_error:
                    self.password_error.place_forget()
                # If correctly login, remove password
                # self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')

                if self.detect_status == 1:
                    self.FaceDetectUserID.place_forget()
                    self.FaceDetectUserName.place_forget()
                    self.UnDetectedLabel.place(x=185, y=550)
                    self.detect_status = 0
                    self.username_status = 0
                    self.password_status = 0
                # self.UnDetectedLabel.place_forget()
            else:
                self.password_error = tk.Label(self, text="Incorrect password, please try again.", bg="#FFF3F3",
                                          fg="red", font=("Open Sans", 18))
                self.password_error.place(x=783, y=360)

    def show_frame(self, canvas):
        self.image_id = 0  # inform function to assign new value to global variable instead of local variable
        # get frame
        ret, frame = cap.read()
        video_width = 380
        video_height = 300

        if ret:
            # cv2 uses `BGR` but `GUI` needs `RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flipped_frame = cv2.flip(frame, 1)
            # convert to PIL image
            img = Image.fromarray(flipped_frame)
            img = img.resize((video_width, video_height), Image.ANTIALIAS)

            imgS = cv2.resize(flipped_frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                # matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)

                matchIndex = argmin(faceDis)
                if IDs[matchIndex]:
                    image_name = IDs[matchIndex].split("!@#$%")[0]
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    bbox = x1, y1, x2 - x1, y2 - y1
                    img_t = cvzone.cornerRect(flipped_frame, bbox, rt=0)
                    img = Image.fromarray(img_t)
                    img = img.resize((video_width, video_height), Image.ANTIALIAS)
                    self.UnDetectedLabel.place_forget()

                    # if this is the first time detected
                    if self.detect_status == 0:
                        query = f"SELECT user_id FROM unmannedshop.TestUserInfoFull WHERE username = '{image_name}';"

                        query_job = self.client.query(query)
                        result = query_job.result()
                        for row in result:
                            self.FDuserid = row.user_id
                        self.FaceDetectUserID = tk.Label(self, text=f"User ID:  {self.FDuserid}",
                                                    font=("yu gothic ui", 21, "bold"),
                                                    bg="#FFFFFF", fg="#000000")
                        self.FaceDetectUserID.place(x=185, y=530)

                        self.FDusername = "UnDetected"
                        self.FaceDetectUserName = tk.Label(self, text=f"User Name:  {image_name}",
                                                       font=("yu gothic ui", 21, "bold"),
                                                       bg="#FFFFFF", fg="#000000")
                        self.FaceDetectUserName.place(x=185, y=565)
                        self.detect_status = 1
                    if self.username_status == 0:
                        self.username_entry.delete(0, 'end')
                        self.username_entry.insert(0, image_name)
                        self.username_status = 1
                    if self.password_status == 0:
                        self.password_entry.delete(0, 'end')
                        query = f"SELECT password FROM unmannedshop.TestUserInfoFull WHERE username = '{image_name}';"

                        query_job = self.client.query(query)
                        result = query_job.result()
                        for row in result:
                            true_password = row.password
                        self.password_entry.insert(0, true_password)
                        self.password_status = 1

            photo = ImageTk.PhotoImage(image=img)
            canvas.photo = photo

            if self.image_id:
                # replace image in PhotoImage on canvas
                canvas.itemconfig(self.image_id, image=photo)
            else:
                # create first image on canvas and keep its ID
                self.image_id = canvas.create_image((0, 0), image=photo, anchor='nw')
                # resize canvas
                canvas.configure(width=photo.width(), height=photo.height())

            # run again after 20ms (0.02s)
            self.after(20, self.show_frame, canvas)

    def resetFD(self):
        if self.detect_status == 1:
            # if self.FaceDetectUserID:
            self.FaceDetectUserID.place_forget()
            self.FaceDetectUserName.place_forget()
            self.UnDetectedLabel.place(x=185, y=550)
            self.detect_status = 0
            self.username_status = 0
            self.password_status = 0
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def toCreateAccountPage(self):
        self.resetFD()
        self.controller.show_create_account_page()