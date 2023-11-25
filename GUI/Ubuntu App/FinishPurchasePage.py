import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
from ImageConvertResult import FinishPurchasePageBg
import base64
from io import BytesIO
from tkinter import Button
import time

class FinishPurchasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        byte_data = base64.b64decode(FinishPurchasePageBg)
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
        ## TITLE ##
        FinishPurchase_Title = tk.Label(self, text="Purchase   Completed", font=("Canva Sans", 35, "bold"),
            bg="#FFF3F3", fg="#545454")
        FinishPurchase_Title.place(x=520, y=285)

        continue_purchase_button = Button(self, text="Continue   Purchasing", command=self.controller.show_object_detection_page,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground="white", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=250)
        continue_purchase_button.place(x=440, y=400)

        done_purchase_button = Button(self, text="Done   Purchasing", command=self.controller.show_done_purchase_page,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground="white", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=250)
        done_purchase_button.place(x=720, y=400)