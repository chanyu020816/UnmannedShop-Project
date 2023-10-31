import cv2
import face_recognition
import pickle
import os
import shutil

folderpath = "./new_faces_images"

def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def EncodeImages():
    file = open("./EncodeFile.p", "rb")
    encodeListwithIDs = pickle.load(file)
    encodeListKnown, IDs = encodeListwithIDs

    imgList = []
    imgID = []
    if os.path.exists(os.path.join(folderpath, ".DS_Store")):
        os.remove(os.path.join(folderpath, ".DS_Store"))
    for path in os.listdir(folderpath):
        imgList.append(cv2.imread(os.path.join(folderpath, path)))
        imgID.append(os.path.splitext(path)[0])
        destination_file = os.path.join("./faces_imgaes", path)
        shutil.move(os.path.join(folderpath, path), destination_file)
        print(os.path.splitext(path)[0], "Complete")

    NewEncodeListKnown = findEncoding(imgList)
    encodeListKnown = encodeListKnown + NewEncodeListKnown
    IDs = IDs + imgID
    encodeListKnowWithIds = [encodeListKnown, IDs]

    file = open("./EncodeFile.p", "wb")
    pickle.dump(encodeListKnowWithIds, file)
    file.close()



if __name__ == "__main__":
    EncodeImages()