import random
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox
from ImageConvertResult import ObjectDetectionBg
import base64
from io import BytesIO
from tkmacosx import Button
import cv2
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from camera import ObjectCamFront
from google.cloud import bigquery
from google.oauth2 import service_account
from constant import *
from numpy import array
from ultralytics import YOLO
import datetime
from uuid import uuid1
from DriveUpload import activateService, upload2Drive
model = YOLO("./weights/best.pt")

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
        self.TotalPrice = None
        self.purchase_button = None
        self.upload_count = 0
        self.purchase_image = None ##

        credentials = service_account.Credentials.from_service_account_file('./unmannedshop.json')
        project_id = PROJECT_ID
        self.client = bigquery.Client(credentials=credentials, project=project_id)

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
        self.table.column("#0", width=100, anchor="c")
        self.table.heading('item_id', text='Item ID')
        self.table.column("item_id", width=100, anchor="c")
        self.table.heading('item_name', text='Item Name')
        self.table.column("item_name", width=250)
        self.table.heading('item_num', text='Number')
        self.table.column("item_num", width=100, anchor="c")
        self.table.heading('total_price', text='Total Price')
        self.table.column("total_price", width=150, anchor="c")
        self.table.place(x=730, y=270)
        self.table.tag_configure("myfont", font=("Helvetica", 18, 'bold'))
        self.table.tag_configure("centered", anchor="center")

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

        logout_button = Button(self, text="Logout", command=self.logout, padx=10, pady=8,
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

        self.purchase_button = Button(self, text="Confirm   Purchase", command=self.ConfirmPurchase,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 25, "bold"),
            activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0, borderwidth=0,
            highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=280, height=50)


        #self.show_frame(canvas)

    def Display(self):

        from LoginPage import login_user_name, login_user_ID
        if self.showInfo_button:
            self.showInfo_button.place_forget()
        self.ShowUserInfoLabel = tk.Label(self, text=f"User   Information",
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
                self.nothing_found.place(x=880, y=220)
            else:
                self.upload_count += 1
                if self.nothing_found is not None:
                    self.nothing_found.place_forget()
                self.DisplayItems()


        else:
            if self.capture_result:
                self.capture_result.place_forget()
            if self.nothing_found:
                self.nothing_found.place_forget()
            # get frame
            ret, frame = ObjectCamFront.read()
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

                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

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
                        fontScale = 0.75
                        thickness = 2

                        img_t = cv2.putText(img_t, class_list[cls], org, font, fontScale, bgr_color, thickness)
                        img = Image.fromarray(img_t)
                        img = img.resize((video_width, video_height), Image.ANTIALIAS)
                        self.purchase_image = img ##

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
        ret, frame = ObjectCamFront.read()
        if ret:
            flipped_frame = cv2.flip(frame, 1)
            # Convert the captured frame to a PhotoImage
            img = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)
            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(img))

        self.capturing = False
        self.TakeImage_button.place_forget()
        self.retake_button.place(x=400, y=680)

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
        if self.TotalPrice is not None:
            self.TotalPrice.place_forget()
        self.upload_count = 0
        self.captured_image = None
        if self.nothing_found is not None:
            self.nothing_found.place_forget()
        if self.retake_button:
            self.retake_button.place_forget()
        self.TakeImage_button.place(x=400, y=680)
        self.resume_show_frame()
        if self.purchase_button is not None:
            self.purchase_button.place_forget()

    def upload_image(self):
        if self.nothing_found is not None:
            self.nothing_found.place_forget()
        if self.upload_count != 0:
            self.retake()
            if self.purchase_button is not None:
                self.purchase_button.place_forget()
        else:
            for item in self.table.get_children():
                self.table.delete(item)
            if self.TotalPrice is not None:
                self.TotalPrice.place_forget()
            self.upload_count += 1

        self.after(300)
        file_path = askopenfilename(filetypes=[('Jpg Files', '*.jpg'), ('PNG Files','*.png')])
        if file_path:

            # Open and display the selected image
            image = Image.open(file_path)
            image = image.resize((600, 540))
            #photo = ImageTk.PhotoImage(image)

            self.captured_image = ""
            self.TakeImage_button.place_forget()
            self.retake_button.place(x=400, y=680)

            ## Model Predict ##
            results = model(image, verbose=False, stream=True, device = "0")
            video_width = 600
            video_height = 540
            # Items' coordinates
            for r in results:
                boxes = r.boxes
                self.model_result = []
                for box in boxes:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    # Convert to int value
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Get class name
                    cls = int(box.cls[0])
                    self.model_result.append(class_list[cls])

                    # put box in cam
                    # Convert a hex color to BGR
                    hex_color = color_list[cls]
                    bgr_color = tuple(int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
                    img_t = cv2.rectangle(array(image), (x1, y1), (x2, y2), bgr_color, thickness=2)

                    # print("Class name ", class_list[cls])
                    org = [x1, y1]

                    img_t = cv2.putText(img_t, class_list[cls], org, cv2.FONT_HERSHEY_SIMPLEX, 0.75, bgr_color, 2)
                    img = Image.fromarray(img_t)
                    image = img.resize((video_width, video_height), Image.ANTIALIAS)
                    self.purchase_image = image ##

            photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, anchor="nw", image=photo)
            self.canvas.image = photo
            self.canvas.place(x=80, y=130)

    def DisplayItems(self):
        item_counts = {}
        for item in self.model_result:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        query = """
        SELECT item_name, item_id, item_price
        FROM unmannedshop.TestItemPrice
        WHERE item_name IN ({})
        """.format(", ".join(["'{}'".format(item) for item in item_counts]))

        query_job = self.client.query(query)
        results = query_job.result()
        self.total_price = 0
        self.full_result = []
        for row in results:
            item_name = row.item_name
            item_id = row.item_id
            item_price = row.item_price
            count = item_counts[item_name]
            item_price *= count
            data = (item_id, item_name, count, item_price)
            self.full_result.append(data)
            self.total_price += item_price
            self.table.insert(parent='', index='end', values=data, tags=("centered", "myfont"))

        self.TotalPrice = tk.Label(self, text=f"Total: $ {self.total_price}", font=("Canva Sans", 28, "bold"),
            bg="#FFF3F3", fg="#4f4e4d")
        self.TotalPrice.place(x=750, y=600)
        self.purchase_button.place(x=880, y=670)

    def ConfirmPurchase(self):
        from LoginPage import login_user_ID
        order_id = str(uuid1())
        today = datetime.datetime.now().date().strftime("%Y-%m-%d")
        add_order_query = f"""
        INSERT INTO unmannedshop.TestOrderHistory (order_id, user_id, order_date, total_price)
        SELECT '{order_id}' AS order_id, {login_user_ID} AS user_id, DATE('{today}') AS order_date,
        {self.total_price} AS total_amount;
        """
        add_order_query_job = self.client.query(add_order_query)

        add_order_item_query = "INSERT INTO unmannedshop.TestOrderItems (order_item_id, order_id, item_id, number, item_price)"
        i = 0
        for item in self.full_result:
            if i != 0:
                add_order_item_query = add_order_item_query + "UNION ALL"
            new_query = f"""
            SELECT '{str(uuid1())}' AS order_item_id, '{order_id}' AS order_id, {item[0]} AS item_id, 
            {item[2]} AS number, {item[3]} AS item_price
            """
            i += 1
            add_order_item_query = add_order_item_query + new_query
        add_order_item_query = add_order_item_query + ";"
        add_order_item_query_job = self.client.query(add_order_item_query)
        print(f"Order ID: {order_id} Complete")
        self.upload_count = 0
        self.TotalPrice.place_forget()
        self.purchase_image.save(f"./purchase_images/{order_id}_front.png", format = "PNG")
        upload2Drive(self.myservice, f"{order_id}_front")
        self.retake()
        self.controller.show_finish_purchase_page()

    def connect_drive(self):
        self.myservice = activateService()

    def logout(self):
        self.upload_count = 0
        self.retake()
        self.controller.show_login_page()