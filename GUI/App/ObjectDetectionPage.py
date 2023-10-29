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
cap = cv2.VideoCapture(0)
#cap.set(3, 0)
#cap.set(4, 550)
import random
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

        # Set up the frame's dimensions
        self.configure(width=1400, height=800)
        self.grid_propagate(False)
        self.grid()
        self.showUserInfo = 0
        self.create_object_detection_page()

    def create_object_detection_page(self):
        # data
        #first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
        #last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

        # treeview
        #table = ttk.Treeview(self, columns=('first', 'last', 'email'), show='headings')
        #table.heading('first', text='First name')
        #table.heading('last', text='Surname')
        #table.heading('email', text='Email')
        #table.place(x = 200, y = 200)

        # insert values into a table
        # table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))
        #for i in range(100):
        #    first = choice(first_names)
        #    last = choice(last_names)
        #    email = f'{first[0]}{last}@email.com'
        #    data = (first, last, email)
        #    table.insert(parent='', index=0, values=data)
        ## FaceRecog TITLE ##
        ObjectDetect_Title = tk.Label(self, text="Object   Detection", font=("Canva Sans", 30, "bold"),
                                   bg="#FFF3F3", fg="#4f4e4d")
        ObjectDetect_Title.place(x=280, y=80)
        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, borderwidth=0, border=0, relief="solid", width=350,
                           highlightthickness=0)
        #self.canvas.place(x=50, y=150)

        TakeImage_button = Button(self, text="Detect   Items", command=self.capture,
             padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
             activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0,
             borderwidth=0,
             highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=250, height=40)
        TakeImage_button.place(x=1080, y=380)


        self.showInfo_button = Button(self, text="Show User Info", command=self.Display, padx = 10, pady=8,
            bg="#DF3F3F", bd = 0, font=("Open Sans", 20, "bold"), activebackground="#FF3A3A",
            activeforeground = "#FF3A3A", fg="white", highlightthickness=0, borderwidth=0, highlightcolor="#FFF3F3",
            highlightbackground="#FFF3F3", width=250)
        self.showInfo_button.place(x=970, y=80)




        # table.insert(parent='', index=tk.END, values=('XXXXX', 'YYYYY', 'ZZZZZ'))

        back_to_login_button = tk.Button(self, text="Back to Login", command=self.controller.show_login_page)
        back_to_login_button.place(x=100, y=80)

        retake_button = tk.Button(self, text="Back to Login", command=self.retake)
        retake_button.place(x=200, y=80)

        purchase_button = Button(self, text="Confirm Purchase", command=self.controller.show_finish_purchase_page,
            padx=10, pady=8, bg="#DF3F3F", bd=0, font=("Open Sans", 20, "bold"),
            activebackground="#FF3A3A", activeforeground="white", fg="white", highlightthickness=0, borderwidth=0,
            highlightcolor="#FFF3F3", highlightbackground="#FFF3F3", width=250, height=40)
        purchase_button.place(x=1080, y=680)

        #self.show_frame(canvas)

    def Display(self):

        from LoginPage import login_user_name, login_user_ID
        if self.showInfo_button:
            self.showInfo_button.place_forget()
        self.ShowUserInfoLabel = tk.Label(self, text=f"User Information",
                                         font=("yu gothic ui", 35, "bold"),
                                         bg="#FFF3F3", fg="#4f4e4d")
        self.ShowUserInfoLabel.place(x=900, y=80)
        self.FaceDetectUserID = tk.Label(self, text=f"User ID: {login_user_ID}",
                                         font=("yu gothic ui", 25, "bold"),
                                         bg="#FFF3F3", fg="#4f4e4d")
        self.FaceDetectUserID.place(x=800, y=140)

        self.FDusername = "UnDetected"
        self.FaceDetectUserName = tk.Label(self, text=f"User Name:  {login_user_name}",
                                           font=("yu gothic ui", 25, "bold"),
                                           bg="#FFF3F3", fg="#4f4e4d")
        self.FaceDetectUserName.place(x=800, y=180)

    def show_frame(self, canvas):
        if not self.running_object_detect_frame:
            return

        self.image_id = 0  # inform function to assign new value to global variable instead of local variable
        if self.captured_image is not None:
            print(self.model_result)
            if len(self.model_result) == 0:
                self.nothing_found = tk.Label(self, text="No Item Detected", font=("Canva Sans", 35, "bold"),
                    bg="#FFF3F3", fg="#4f4e4d")
                self.nothing_found.place(x=1000, y=600)
            else:
                if self.nothing_found:
                    self.nothing_found.place_forget()
                initial_height = 300
                for item in self.model_result:
                    self.capture_result = tk.Label(self, text=item, font=("Canva Sans", 35, "bold"),
                    bg="#FFF3F3", fg="#4f4e4d")
                    self.capture_result.place(x=1000, y=initial_height)
                    initial_height += 50
            # photo = ImageTk.PhotoImage(image=self.captured_image)
            # solution for bug in `PhotoImage`
            #self.canvas.photo = self.captured_image
        else:
            if self.capture_result:
                self.capture_result.place_forget()
            # get frame
            ret, frame = cap.read()
            # Set the desired capture width and height
            video_width = 640  # Change this to your preferred width
            video_height = 640  # Change this to your preferred height

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
                    print(random.randint(1, 1))
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

            cv2.imwrite("./test.jpg", flipped_frame)

            self.captured_image = ImageTk.PhotoImage(image=Image.fromarray(img))

        self.capturing = False

    def run(self):
        self.window.mainloop()
    def stop_show_frame(self):
        self.running_object_detect_frame = False
        self.canvas.place_forget()

    def resume_show_frame(self):
        self.running_object_detect_frame = True
        self.show_frame(self.canvas)
        self.canvas.place(x=120, y=150)

    def retake(self):
        self.captured_image = None
        self.resume_show_frame()