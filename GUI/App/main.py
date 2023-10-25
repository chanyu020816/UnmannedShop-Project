import tkinter as tk

from LoginPage import LoginPage
from CreateAccountPage import CreateAccountPage
from ObjectDetectionPage import ObjectDetectionPage

class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Unmanned Shop")
        self.geometry("1400x800")

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.pages = {
            "LoginPage": LoginPage(self.container, self),
            "CreateAccountPage": CreateAccountPage(self.container, self),
            "ObjectDetectionPage": ObjectDetectionPage(self.container, self)
        }

        self.show_login_page()

    def show_login_page(self):
        self.pages["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["CreateAccountPage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()

    def show_create_account_page(self):
        self.pages["CreateAccountPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()
        
    def show_object_detection_page(self):
        self.pages["ObjectDetectionPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()
        self.pages["CreateAccountPage"].grid_forget()

if __name__ == '__main__':
    app = MainView()
    app.mainloop()