import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
from ImageConvertResult import LoginPageBg
import base64
from io import BytesIO
from sys import platform

if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button
import time

class FinishPurchasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        byte_data = base64.b64decode(LoginPageBg)
        image_data = BytesIO(byte_data)

        self.bg_frame = Image.open(image_data)
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

        self.create_finish_purchase_page()

    def create_finish_purchase_page(self):
        # ... Your create account page code ...
        back_to_login_button = tk.Button(self, text="Back to Login", command=self.controller.show_login_page)
        back_to_login_button.place(x=100, y=100)