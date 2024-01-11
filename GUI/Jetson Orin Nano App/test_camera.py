import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error")
    exit()

while True:
    ret, frame = cap.read()
    cv2.imshow("camera test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
