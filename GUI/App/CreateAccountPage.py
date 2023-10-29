import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox
import time
from ImageConvertResult import LoginBg
import base64
from io import BytesIO
from sys import platform
if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button

from google.cloud import bigquery
from google.oauth2 import service_account
from constant import *
import datetime

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller

        byte_data = base64.b64decode(LoginBg)
        image_data = BytesIO(byte_data)

        self.bg_frame = Image.open(image_data)
        desired_width = 1400
        desired_height = 800
        resized_bg = self.bg_frame.resize((desired_width, desired_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_bg)
        self.bg_panel = tk.Label(self, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        self.email_check_error = None
        self.username_check_error = None
        self.password_check_error = None
        self.birthdate_check_error = None

        # Set up the frame's dimensions
        self.configure(width=1400, height=800)
        self.grid_propagate(False)
        self.grid()

        self.create_create_account_page()

    def create_create_account_page(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="#F89B9B", foreground="#000000",
            selectforeground="#000000", selectbackground="#F89B9B", padx=30, padding = "#000000")


        ## TITLE ##
        UserLogin_Title = tk.Label(self, text = "Create    Account", font=("Canva Sans", 35, "bold"), bg="#FFF3F3", fg="#FF3A3A")
        UserLogin_Title.place(x = 930, y = 80)

        ## EMAIL ##
        email_label = tk.Label(self, text="Email", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        email_label.place(x=780, y=140)
        email = tk.StringVar()
        self.email_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = email)
        self.email_entry.place(x=780, y=180, width=550, height=30)
        
        ## USERNAME ##
        username_label = tk.Label(self, text="Username", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        username_label.place(x = 780, y = 220)
        username = tk.StringVar()
        self.username_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = username)
        self.username_entry.place(x = 780, y = 260, width = 550, height = 30)

        ## PASSWORD ##
        password_label = tk.Label(self, text="Password", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_label.place(x=780, y=300)
        password = tk.StringVar()
        self.password_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = password, show="*")
        self.password_entry.place(x = 780, y=340, width=550, height=30)

        ## PASSWORD CHECK ##
        password_check_label = tk.Label(self, text="Enter Password Again", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_check_label.place(x = 780, y=380)
        password_check = tk.StringVar()
        self.password_check_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable=password_check, show="*")
        self.password_check_entry.place(x=780, y=420, width=550, height=30)

        # Sex Label and Combobox
        sex_label = tk.Label(self, text="Sex", bg="#FFF3F3", fg="#4f4e4d",
                             font=("yu gothic ui", 20, "bold"))
        sex_label.place(x=780, y=460)
        sex = tk.StringVar()
        self.sex_combobox = ttk.Combobox(self, textvariable=sex, values=[" Male", " Female", " Other"],
            font=("Helvetica", 18), style="TCombobox")
        self.sex_combobox.place(x=780, y=500, width=550, height=35)

        # Birthdate Label and Entry
        birthdate_label = tk.Label(self, text="Birthdate (YYYY-MM-DD)", bg="#FFF3F3", fg="#4f4e4d",
                                   font=("yu gothic ui", 20, "bold"))
        birthdate_label.place(x=780, y=540)
        birthdate = tk.StringVar()
        self.birthdate_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                   font=("yu gothic ui ", 18), insertbackground='#6b6a69', borderwidth=7,
                                   textvariable=birthdate)
        self.birthdate_entry.place(x=780, y=580, width=550, height=30)

        BacktoLogin_button = Button(self, text="Back to Login", command=self.controller.show_login_page, padx=10,
            pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground = "#FF3A3A", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width = 250)
        BacktoLogin_button.place(x=780, y=680)

        signup_button = Button(self, text="Signup", 
            command= lambda: self.signup(email, username, password, password_check, sex, birthdate), padx = 10, pady=8,
            bg="#DF3F3F", bd = 0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground = "#FF3A3A", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width = 250)
        signup_button.place(x=1080, y=680)
        
    def signup(self, email, username, password, password_check, sex, birthdate):
        email_input = email.get()
        username_input = username.get()
        password_input = password.get()
        password_check_input = password_check.get()
        sex_input = sex.get()
        birthdate_input = birthdate.get()
        today = datetime.datetime.now().date().strftime("%Y-%m-%d")

        credentials = service_account.Credentials.from_service_account_file('./unmannedshop-3444ca55864c.json')
        project_id = PROJECT_ID
        client = bigquery.Client(credentials=credentials, project=project_id)

        ### if email already exists ###
        email_check_query = f""" \
        SELECT COUNT(*) as count \
        FROM unmannedshop.TestUserInfoFull \
        WHERE email = '{email_input}'; \
        """
        email_check_query_job = client.query(email_check_query)
        email_check_result = email_check_query_job.result()
        email_check_row = next(email_check_result)
        email_check_count = email_check_row['count']
        if email_check_count > 0:
            if self.email_check_error:
                self.email_check_error.place_forget()
            self.email_check_error = tk.Label(self, text="Email already exists. Try again.", bg="#FFF3F3",
                                                 fg="red", font=("Open Sans", 18))
            self.email_check_error.place(x=1080, y=215)
            return ""
        else:
            if self.email_check_error:
                self.email_check_error.place_forget()

        ### if username already exists ###
        username_check_query = f""" \
        SELECT COUNT(*) as count \
        FROM unmannedshop.TestUserInfoFull \
        WHERE username = '{username_input}'; \
        """
        username_check_query_job = client.query(username_check_query)
        username_check_result = username_check_query_job.result()
        username_check_row = next(username_check_result)
        username_check_count = username_check_row['count']
        if username_check_count > 0:
            if self.username_check_error:
                self.username_check_error.place_forget()
            self.username_check_error = tk.Label(self, text="Username already exists. Try again.", bg="#FFF3F3",
                                                 fg="red", font=("Open Sans", 18))
            self.username_check_error.place(x=1030, y=295)
            return ""
        else:
            if self.username_check_error:
                self.username_check_error.place_forget()

        if password_input != password_check_input:
            if self.password_check_error:
                self.password_check_error.place_forget()
            self.password_check_error = tk.Label(self, text="Those passwords didn’t match. Try again.", bg="#FFF3F3",
                fg="red", font = ("Open Sans", 18))
            self.password_check_error.place(x=990, y=455)
        elif self.is_valid_bigquery_date(birthdate_input):
            if self.birthdate_check_error:
                self.birthdate_check_error.place_forget()
            self.birthdate_check_error = tk.Label(self, text="Enter correct Birthdate format", bg="#FFF3F3",
                fg="red", font = ("Open Sans", 18))
            self.birthdate_check_error.place(x=780, y=610)
        else:
            if self.password_check_error:
                self.password_check_error.place_forget()


            # SQL query to find the maximum user ID
            max_user_id = 0
            max_query = f"""\
            SELECT MAX(user_id) AS max_user_id \
            FROM unmannedshop.TestUserInfoFull \
            """
            max_query_job = client.query(max_query)
            max_results = max_query_job.result()
            for row in max_results:
                max_user_id = row.max_user_id
            new_user_id = max_user_id + 1

            # SQL query to create new user
            create_new_query = f""" \
            INSERT INTO unmannedshop.TestUserInfoFull (user_id, username, email, password, Sex, BirthDate, registration_date) \
            SELECT {new_user_id} AS user_id, '{username_input}' AS username, '{email_input}'AS email, \
            '{password_input}' AS password, '{sex_input}' AS Sex, DATE('{birthdate_input}') AS BirthDate, \
            DATE('{today}') AS registration_date; \
            """
            create_new_query_job = client.query(create_new_query)

            self.email_entry.delete(0, 'end')
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.password_check_entry.delete(0, 'end')
            self.sex_combobox.set('')
            self.birthdate_entry.delete(0, 'end')
            self.after(5000, self.controller.show_login_page())


    def is_valid_bigquery_date(self, input_date):
        try:
            datetime.datetime.strptime(input_date, '%Y-%m-%d')
            return False
        except ValueError:
            return True