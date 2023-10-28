import cv2
import face_recognition
import pickle
import os

folderpath = "./faces_images"

def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def EncodeImages():
    imgList = []
    imgID = []
    for path in os.listdir(folderpath):
        imgList.append(cv2.imread(os.path.join(folderpath, path)))
        imgID.append(os.path.splitext(path)[0])
        print(imgID, "Complete")

    encodeListKnown = findEncoding(imgList)
    encodeListKnowWithIds = [encodeListKnown, imgID]

    file = open("../GUI/App/EncodeFile.p", "wb")
    pickle.dump(encodeListKnowWithIds, file)
    file.close()

if __name__ == "__main__":
    EncodeImages()