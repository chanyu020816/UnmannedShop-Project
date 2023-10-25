import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
import time

from sys import platform
if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        self.bg_frame = Image.open('images/LoginBg.png')
        desired_width = 1400
        desired_height = 800
        resized_bg = self.bg_frame.resize((desired_width, desired_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_bg)
        self.bg_panel = tk.Label(self, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Set up the frame's dimensions
        self.configure(width=1400, height=800)
        self.grid_propagate(False)
        self.grid()

        self.create_create_account_page()

    def create_create_account_page(self):
        # ... Your create account page code ...

        back_to_login_button = tk.Button(self, text="Back to Login", command=self.controller.show_login_page)
        back_to_login_button.place(x=100, y=100)
        back_to_object_detection_button = tk.Button(self, text="Object Page", command=self.controller.show_object_detection_page)
        back_to_object_detection_button.place(x=100, y=200)
        ## TITLE ##
        UserLogin_Title = tk.Label(self, text = "Create    Account", font=("yu gothic ui", 35, "bold"), bg="#FFF3F3", fg="firebrick3")
        UserLogin_Title.place(x = 930, y = 80)
        

        ## EMAIL ##
        email_label = tk.Label(self, text="Email", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        email_label.place(x = 780, y = 160)
        email = tk.StringVar()
        email_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = email)
        email_entry.place(x = 780, y = 200, width = 550, height = 30)
        
        ## USERNAME ##
        username_label = tk.Label(self, text="Username", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        username_label.place(x = 780, y = 240)
        username = tk.StringVar()
        username_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = username)
        username_entry.place(x = 780, y = 280, width = 550, height = 30)
        #username_line = tk.Canvas(self, width = 550, height = 2.0, bg="#bdb9b1", highlightthickness = 0)
        #username_line.place(x = 780, y = 225)

        ## PASSWORD ##
        password_label = tk.Label(self, text="Password", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_label.place(x = 780, y = 320)
        password = tk.StringVar()
        password_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = password, show = "*")
        password_entry.place(x = 780, y = 360, width = 550, height = 30)
        #password_line = tk.Canvas(self, width = 440, height = 2.0, bg="#bdb9b1", highlightthickness = 0)
        #password_line.place(x = 890, y = 300)

        ## PASSWORD CHECK##
        password_check_label = tk.Label(self, text="Enter Password Again", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_check_label.place(x = 780, y = 400)
        password_check = tk.StringVar()
        password_check = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = password_check, show = "*")
        password_check.place(x = 780, y = 440, width = 550, height = 30)
        #password_line = tk.Canvas(self, width = 440, height = 2.0, bg="#bdb9b1", highlightthickness = 0)
        #password_line.place(x = 890, y = 300)
        
        #test1 = tk.Label(self, textvariable = username)
        #test1.place(x = 750, y = 300)
        #test2 = tk.Label(self, textvariable = password)
        #test2.place(x = 750, y = 400)
        
        BacktoLogin_button = Button(self, text="Back to Login", command=self.controller.show_login_page, padx = 10, pady = 8,
            bg = "#DF3F3F", bd = 0, font = ("Open Sans", 20, "bold"), activebackground = "firebrick3",
            activeforeground = "white", fg = "white", highlightthickness = 0, borderwidth = 0, highlightcolor="#FFF3F3", 
            highlightbackground="#FFF3F3", width = 250)
        BacktoLogin_button.place(x=780, y=680)

        signup_button = Button(self, text="Signup", 
            command= lambda: self.signup(email, username, password, password_check), padx = 10, pady = 8,
            bg = "#DF3F3F", bd = 0, font = ("Open Sans", 20, "bold"), activebackground = "firebrick3",
            activeforeground = "white", fg = "white", highlightthickness = 0, borderwidth = 0, highlightcolor="#FFF3F3", 
            highlightbackground="#FFF3F3", width = 250)
        signup_button.place(x=1080, y=680)
        
    def signup(self, email, username, password, password_check, sex = 1, birthdate = 1):
        email_input = email.get()
        username_input = username.get()
        password_input = password.get()
        password_check_input = password_check.get()
        #sex_input = sex.get()
        #birtgdate_input = birthdate.get()
        
        if password_input != password_check_input:
            password_check_error = tk.Label(self, text = "Those passwords didn’t match. Try again.", bg = "#FFF3F3",
                fg="red", font = ("Open Sans", 18))
            password_check_error.place(x = 785, y = 470) 
        else:
            
            time.sleep(2)
            self.controller.show_login_page()
        