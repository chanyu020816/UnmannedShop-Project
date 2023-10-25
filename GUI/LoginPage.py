import tkinter as tk
from PIL import ImageTk, Image

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller

        # Set up the frame's dimensions
        self.configure(width=1166, height=718)
        self.grid_propagate(False)
        self.grid()

        self.create_login_page()

    def create_login_page(self):
        # ... Your login page code ...

        create_account_button = tk.Button(self, text="Create Account", command=self.controller.show_create_account_page)
        create_account_button.place(x=100, y=100)

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller

        # Set up the frame's dimensions
        self.configure(width=1166, height=718)
        self.grid_propagate(False)
        self.grid()

        self.create_create_account_page()

    def create_create_account_page(self):
        # ... Your create account page code ...

        back_to_login_button = tk.Button(self, text="Back to Login", command=self.controller.show_login_page)
        back_to_login_button.place(x=100, y=100)

class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Authentication App")
        self.geometry("1166x718")

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.pages = {
            "LoginPage": LoginPage(self.container, self),
            "CreateAccountPage": CreateAccountPage(self.container, self)
        }

        self.show_login_page()

    def show_login_page(self):
        self.pages["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["CreateAccountPage"].grid_forget()

    def show_create_account_page(self):
        self.pages["CreateAccountPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()

if __name__ == '__main__':
    app = MainView()
    app.mainloop()
