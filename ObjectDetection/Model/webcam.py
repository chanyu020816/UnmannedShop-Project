from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("./runs/detect/train20/weights/best.pt")

# object classes
class_list = ['Bak Kut Teh Flavor Noodles', 'Doritos', 'I MEI-Milk Puff', 'M-M-Crisp', 'M-M-Peanut', 'Oreo', 'Popconcern-Sweet-Salty', 'Pringles-Origin', 'PureTea-Black Tea', 'PureTea-LemonGreen Tea', 'Skittles', 'White Chocolate Ice Cream']
color_list = ["#FF5733", "#42A5F5", "#7B8D8C", "#E57373", "#FFD700", "#4CAF50", "#9C27B0", "#FF5722", "#607D8B", "#FFD600", "#795548", "#E91E63"]


while True:
    success, img = cap.read()
    results = model(img, stream=True, verbose=False)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            #print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            #print("Class name -->", class_list[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = color_list[cls]
            thickness = 2

            cv2.putText(img, class_list[cls], org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()