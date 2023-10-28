import cv2
import pickle
import face_recognition
from numpy import argmin
import time
import cvzone

file = open("./EncodeFile.p", "rb")
encodeListwithIDs = pickle.load(file)
file.close()

encodeListKnow, IDs = encodeListwithIDs

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
Detecting = True
if __name__ == "__main__":
    while Detecting:
        success, img = cap.read()

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)
            #print("matches", matches)
            #print("faceDis", faceDis)

            matchIndex = argmin(faceDis)
            if IDs[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = x1, y1, x2 - x1, y2 - y1
                cvzone.cornerRect(img, bbox, rt = 0)
                #time.sleep(5)  # 等待5秒
                #Detecting = False

        cv2.imshow("Webcam", img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break