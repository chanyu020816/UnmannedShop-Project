import tkinter as tk
from PIL import ImageTk, Image


from sys import platform
# if the operate system is macos, Button should be imported from tkmascos
if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        self.bg_frame = Image.open('images/LoginPageBg.png')
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
        self.create_login_page()

    def create_login_page(self):

        
        ## LOGIN BACKGROUND ##
        #LoginBackGround = tk.Canvas(self, width = 650, height= 700, background = "#FFFAFD", borderwidth = 5, highlightthickness=0)  # 加入 Canvas 畫布
        #LoginBackGround.place(x = 700, y = 50)
        
        
        ## TITLE ##
        UserLogin_Title = tk.Label(self, text = "User    Login", font=("yu gothic ui", 35, "bold"), bg="#FFF3F3", fg="firebrick3")
        UserLogin_Title.place(x = 970, y = 140)
        
        ## USERNAME ##
        username_label = tk.Label(self, text="Username", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        username_label.place(x = 780, y = 210)
        username = tk.StringVar()
        username_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = username)
        username_entry.place(x = 780, y = 250, width = 550, height = 30)
        #username_line = tk.Canvas(self, width = 550, height = 2.0, bg="#bdb9b1", highlightthickness = 0)
        #username_line.place(x = 780, y = 225)

        ## PASSWORD ##
        password_label = tk.Label(self, text="Password", bg="#FFF3F3", fg="#4f4e4d",
                                    font=("yu gothic ui", 20, "bold"))
        password_label.place(x = 780, y = 290)
        password = tk.StringVar()
        password_entry = tk.Entry(self, highlightthickness=0, relief='flat', bg="#F89B9B", fg="#000000",
                                    font=("yu gothic ui ", 18), insertbackground = '#6b6a69', borderwidth=7,
                                    textvariable = password, show = "*")
        password_entry.place(x = 780, y = 330, width = 550, height = 30)
        #password_line = tk.Canvas(self, width = 440, height = 2.0, bg="#bdb9b1", highlightthickness = 0)
        #password_line.place(x = 890, y = 300)

        
        #test1 = tk.Label(self, textvariable = username)
        #test1.place(x = 750, y = 300)
        #test2 = tk.Label(self, textvariable = password)
        #test2.place(x = 750, y = 400)
        
        create_account_button = Button(self, text="Create   Account", command=self.controller.show_create_account_page, padx = 10, pady = 8,
            bg = "#DF3F3F", bd = 0, font = ("Open Sans", 20, "bold"), activebackground = "firebrick3",
            activeforeground = "white", fg = "white", highlightthickness = 0, borderwidth = 0, highlightcolor="#FFF3F3", 
            highlightbackground="#FFF3F3", width = 250)
        create_account_button.place(x=780, y=600)

        submit_button = Button(self, text="Submit", command= lambda: self.submit(username, password), padx = 10, pady = 8,
            bg = "#DF3F3F", bd = 0, font = ("Open Sans", 20, "bold"), activebackground = "firebrick3",
            activeforeground = "white", fg = "white", highlightthickness = 0, borderwidth = 0, highlightcolor="#FFF3F3", 
            highlightbackground="#FFF3F3", width = 250)
        submit_button.place(x=1080, y=600)
        
    def submit(self, username, password):
        username_input = username.get()
        password_input = password.get()
        
        true_password = "pass"

        if password_input == true_password:
            self.controller.show_create_account_page()
        else:
            password_error = tk.Label(self, text = "Incorrect password, please try again.", bg = "#FFF3F3",
                fg="red", font = ("Open Sans", 18))
            password_error.place(x = 785, y = 310)   
    