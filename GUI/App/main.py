import tkinter as tk

from LoginPage import LoginPage
from CreateAccountPage import CreateAccountPage
from ObjectDetectionPage import ObjectDetectionPage
from FinishPurchasePage import FinishPurchasePage
from DonePurchasePage import DonePurchasePage

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
            "ObjectDetectionPage": ObjectDetectionPage(self.container, self),
            "FinishPurchasePage": FinishPurchasePage(self.container, self),
            "DonePurchasePage": DonePurchasePage(self.container, self)
        }

        self.test = 2
        self.Initial()


    def Initial(self):
        self.pages["LoginPage"].grid(row=0, column=0, sticky="nsew")

        #self.pages["LoginPage"].resume_show_frame()

    def show_create_account_page(self):
        self.pages["CreateAccountPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()
        self.pages["DonePurchasePage"].grid_forget()
        self.pages["FinishPurchasePage"].grid_forget()
        self.pages["LoginPage"].stop_show_frame()
        self.after(50, self.pages["CreateAccountPage"].resume_show_frame())

    def show_object_detection_page(self):
        self.pages["ObjectDetectionPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()
        self.pages["CreateAccountPage"].grid_forget()
        self.pages["DonePurchasePage"].grid_forget()
        self.pages["LoginPage"].stop_show_frame()
        #self.pages["ObjectDetectionPage"].resume_show_frame()
        self.after(50, self.pages["ObjectDetectionPage"].resume_show_frame())


    def show_finish_purchase_page(self):
        self.pages["FinishPurchasePage"].grid(row=0, column=0, sticky="nsew")
        self.pages["DonePurchasePage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()
        self.pages["ObjectDetectionPage"].stop_show_frame()

    def show_done_purchase_page(self):
        self.pages["DonePurchasePage"].grid(row=0, column=0, sticky="nsew")
        self.pages["LoginPage"].grid_forget()
        self.pages["FinishPurchasePage"].grid_forget()
        self.after(15000, self.show_login_page)

    def show_login_page(self):
        self.pages["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["CreateAccountPage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()
        self.pages["DonePurchasePage"].grid_forget()
        self.pages["FinishPurchasePage"].grid_forget()
        self.pages["ObjectDetectionPage"].stop_show_frame()
        self.pages["CreateAccountPage"].stop_show_frame()
        self.pages["LoginPage"].resume_show_frame()
        #self.after(3000, self.pages["LoginPage"].resume_show_frame())

    def AfterSignUpAccount_show_login_page(self):
        self.pages["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.pages["CreateAccountPage"].grid_forget()
        self.pages["ObjectDetectionPage"].grid_forget()
        self.pages["CreateAccountPage"].stop_show_frame()
        self.pages["LoginPage"].reloadModel()
        self.pages["LoginPage"].resume_show_frame()


if __name__ == '__main__':
    app = MainView()
    app.mainloop()