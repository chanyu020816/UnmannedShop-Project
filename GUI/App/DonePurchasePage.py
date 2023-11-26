import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
from ImageConvertResult import DonePurchasePageBg
import base64
from io import BytesIO

class DonePurchasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        byte_data = base64.b64decode(DonePurchasePageBg)
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

        self.create_done_purchase_page()


    def create_done_purchase_page(self):

        UserLogin_Title = tk.Label(self, text="Return  to  Login  after  5  seconds...",
            font=("Canva Sans", 30, "bold"), bg="#FFF3F3", fg="#545454")
        UserLogin_Title.place(x=450, y=210)
