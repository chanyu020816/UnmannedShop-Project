import random
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox
from ImageConvertResult import ObjectDetectionBg
import base64
from io import BytesIO
from sys import platform
if platform == "darwin":
    from tkmacosx import Button
else:
    from tkinter import Button
import cv2
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
cap = cv2.VideoCapture(0)

from numpy import array
from ultralytics import YOLO
model = YOLO("./best.pt")
class_list = ['Bak Kut Teh Flavor Noodles', 'Doritos', 'I MEI-Milk Puff', 'M-M-Crisp', 'M-M-Peanut', 'Oreo', 'Popconcern-Sweet-Salty', 'Pringles-Origin', 'PureTea-Black Tea', 'PureTea-LemonGreen Tea', 'Skittles', 'White Chocolate Ice Cream']
color_list = ["#FF5733", "#42A5F5", "#7B8D8C", "#E57373", "#FFD700", "#4CAF50", "#9C27B0", "#FF5722", "#607D8B", "#FFD600", "#795548", "#E91E63"]

class ObjectDetectionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#040405")
        self.window = parent
        self.controller = controller
        byte_data = base64.b64decode(ObjectDetectionBg)
        image_data = BytesIO(byte_data)

        self.bg_frame = Image.open(image_data)
        desired_width = 1400
        desired_height = 800
        resized_bg = self.bg_frame.resize((desired_width, desired_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_bg)
        self.bg_panel = tk.Label(self, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        self.showInfo_button = None
        self.running_object_detect_frame = False
        self.capturing = False
        self.captured_image = None
        self.capture_result = None
        self.nothing_found = None
        self.retake_button = None

        # Set up the frame's dimensions
        self.configure(width=1400, height=800)
        self.grid_propagate(False)
        self.grid()
        self.showUserInfo = 0
        self.create_object_detection_page()

    def create_object_detection_page(self):

        style = ttk.Style()
        # style.theme_use('clam')
        style.configure("Treeview", fieldbackground="#FFFFFF", foreground="#000000",
            background="#FFFFFF", rowheight=28)
        style.configure("Treeview.Heading", font=("Open Sans", 20, 'bold'), background="#ECD7AA", foreground="#4f4e4d")

        # Object Detection Result
        self.table = ttk.Treeview(self, columns=('item_id', 'item_name', 'item_num', 'total_price'), show='headings',
            style="Treeview")
        self.table.heading("#0", text="qwer")
        self.table.column("#0", width=100)
        self.table.heading('item_id', text='Item ID')
        self.table.column("item_id", width=100)
        self.table.heading('item_name', text='Item Name')
        self.table.column("item_name", width=250)
        self.table.heading('item_num', text='Number')
        self.table.column("item_num", width=100)
        self.table.heading('total_price', text='Total Price')
        self.table.column("total_price", width=150)
        self.table.place(x=730, y=300)

        ## FaceRecog TITLE ##
        ObjectDetect_Title = tk.Label(self, text="Object   Detection", font=("Canva Sans", 35, "bold"),
                                   bg="#FFFFFF", fg="#4f4e4d")
        ObjectDetect_Title.place(x=220, y=65)
        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, borderwidth=0, border=0, relief="solid", width=350,
                           highlightthickness=0)
        #self.canvas.place(x=50, y=150)

        self.TakeImage_button = Button(self, text="Detect   Items", command=self.capture,
             padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
             activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0,
             borderwidth=0, highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=280, height=40)
        self.TakeImage_button.place(x=400, y=680)

        self.showInfo_button = Button(self, text="Show User Info", command=self.Display, padx=10, pady=8,
            bg="#DF3F3F", bd = 0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground = "#FF3A3A", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=250)
        self.showInfo_button.place(x=900, y=80)

        logout_button = Button(self, text="Logout", command=self.controller.show_login_page, padx=10, pady=8,
            bg="#DF3F3F", bd=0, font=("Open Sans", 15, "bold"), activebackground="#FF3A3A",
            activeforeground="#FF3A3A", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=100, height=30)
        logout_button.place(x=1265, y=40)

        self.retake_button = Button(self, text="ReDetect   Items", command=self.retake,
             padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
             activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0,
             borderwidth=0,
             highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=280, height=40)

        upload_button = Button(self, text="Upload   Image", command=self.upload_image,
             padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
             activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0,
             borderwidth=0,
             highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=280, height=40)
        upload_button.place(x=80, y=680)

        self.purchase_button = Button(self, text="Confirm   Purchase", command=self.controller.show_finish_purchase_page,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 25, "bold"),
            activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0, borderwidth=0,
            highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=280, height=50)


        #self.show_frame(canvas)

    def Display(self):

        from LoginPage import login_user_name, login_user_ID
        if self.showInfo_button:
            self.showInfo_button.place_forget()
        self.ShowUserInfoLabel = tk.Label(self, text=f"User Information",
                                         font=("yu gothic ui", 25, "bold"),
                                         bg="#FFF3F3", fg="#4f4e4d")
        self.ShowUserInfoLabel.place(x=930, y=80)
        self.FaceDetectUserID = tk.Label(self, text=f"User ID: {login_user_ID}",
                                         font=("yu gothic ui", 20, "bold"),
                                         bg="#FFF3F3", fg="#4f4e4d")
        self.FaceDetectUserID.place(x=800, y=120)

        self.FDusername = "UnDetected"
        self.FaceDetectUserName = tk.Label(self, text=f"User Name:  {login_user_name}",
                                           font=("yu gothic ui", 20, "bold"),
                                           bg="#FFF3F3", fg="#4f4e4d")
        self.FaceDetectUserName.place(x=800, y=150)

    def show_frame(self, canvas):
        if not self.running_object_detect_frame:
            return
        self.image_id = 0  # inform function to assign new value to global variable instead of local variable
        if self.captured_image is not None:

            if len(self.model_result) == 0:
                self.nothing_found = tk.Label(self, text="No Item Detected", font=("Canva Sans", 35, "bold"),
                    bg="#FFF3F3", fg="#DF3F3F")
                self.nothing_found.place(x=880, y=250)
            else:

                if self.nothing_found is not None:
                    self.nothing_found.place_forget()

                for item in self.model_result:
                    data = (1, item, 2, 20)
                    self.table.insert(parent='', index=0, values=data)
                self.purchase_button.place(x=880, y=650)

        else:
            if self.capture_result:
                self.capture_result.place_forget()
            if self.nothing_found:
                self.nothing_found.place_forget()
            # get frame
            ret, frame = cap.read()
            # Set the desired capture width and height
            video_width = 600
            video_height = 540

            # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 350)  # 3 corresponds to CV_CAP_PROP_FRAME_WIDTH
            # cap.set(4, video_height)  # 4 corresponds to CV_CAP_PROP_FRAME_HEIGHT

            if ret:

                # cv2 uses `BGR` but `GUI` needs `RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flipped_frame = cv2.flip(frame, 1)
                # convert to PIL image
                img = Image.fromarray(flipped_frame)

                img = img.resize((video_width, video_height), Image.ANTIALIAS)
                # Convert to Tkinter image

                ## Model Predict ##
                results = model(img, verbose=False, stream=True)

                # coordinates
                for r in results:
                    # print(random.randint(1, 1))
                    boxes = r.boxes
                    self.model_result = []
                    for box in boxes:
                        # bounding box
                        x1, y1, x2, y2 = box.xyxy[0]

                        x1, y1, x2, y2 = (int(round(int(x1) * 1.1)), int(round(int(y1) * 1.1)),
                            int(round(int(x2) * 0.9)), int(round(int(y2) * 0.9))) # convert to int values

                        # class name
                        cls = int(box.cls[0])
                        self.model_result.append(class_list[cls])
                        # put box in cam
                        # Convert a hex color to BGR
                        hex_color = color_list[cls]
                        bgr_color = tuple(int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
                        img_t = cv2.rectangle(array(img), (x1, y1), (x2, y2), bgr_color, thickness=2)

                        # print("Class name ", class_list[cls])
                        org = [x1, y1]
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 1
                        thickness = 2

                        img_t = cv2.putText(img_t, class_list[cls], org, font, fontScale, bgr_color, thickness)
                        img = Image.fromarray(img_t)
                        img = img.resize((video_width, video_height), Image.ANTIALIAS)

                photo = ImageTk.PhotoImage(image=img)
                # solution for bug in `PhotoImage`
                self.canvas.photo = photo

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

    def capture(self):
        self.capturing = True

        # Capture a frame
        ret, frame = cap.read()
        if ret:
            flipped_frame = cv2.flip(frame, 1)
            # Convert the captured frame to a PhotoImage
            img = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)

            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(img))

        self.capturing = False
        self.TakeImage_button.place_forget()
        self.retake_button.place(x=400, y=680)

    def run(self):
        self.window.mainloop()

    def stop_show_frame(self):
        self.running_object_detect_frame = False
        self.canvas.place_forget()

    def resume_show_frame(self):
        self.running_object_detect_frame = True
        self.show_frame(self.canvas)
        self.canvas.place(x=80, y=130)

    def retake(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.captured_image = None
        if self.nothing_found is not None:
            self.nothing_found.place_forget()
        if self.retake_button:
            self.retake_button.place_forget()
        self.TakeImage_button.place(x=400, y=680)
        self.resume_show_frame()
        self.purchase_button.place_forget()

    def upload_image(self):
        if self.nothing_found is not None:
            self.nothing_found.place_forget()
        self.retake()
        self.after(500)
        file_path = askopenfilename(filetypes=[('Jpg Files', '*.jpg'), ('PNG Files','*.png')])
        if file_path:
            #
            # Open and display the selected image
            image = Image.open(file_path)
            image = image.resize((600, 540))
            #photo = ImageTk.PhotoImage(image)

            self.captured_image = ""
            self.TakeImage_button.place_forget()
            self.retake_button.place(x=400, y=680)
            ## Model Predict ##
            results = model(image, verbose=False, stream=True)
            video_width = 600  # Change this to your preferred width
            video_height = 540
            # coordinates
            for r in results:
                # print(random.randint(1, 1))
                boxes = r.boxes
                self.model_result = []
                for box in boxes:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]

                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                    # class name
                    cls = int(box.cls[0])
                    self.model_result.append(class_list[cls])

                    # put box in cam
                    # Convert a hex color to BGR
                    hex_color = color_list[cls]
                    bgr_color = tuple(int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
                    img_t = cv2.rectangle(array(image), (x1, y1), (x2, y2), bgr_color, thickness=2)

                    # print("Class name ", class_list[cls])
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    thickness = 2
                    # self.captured_image = ""
                    img_t = cv2.putText(img_t, class_list[cls], org, font, fontScale, bgr_color, thickness)
                    img = Image.fromarray(img_t)
                    image = img.resize((video_width, video_height), Image.ANTIALIAS)
            #if self.nothing_found is not None:
            #    self.nothing_found.place_forget()
            photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, anchor="nw", image=photo)
            self.canvas.image = photo
            self.canvas.place(x=80, y=110)

    def DisplayItems(self):
        ...