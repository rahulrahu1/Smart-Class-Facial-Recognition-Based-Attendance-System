import cv2
import face_recognition
import pickle
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://smartclass-a14a0-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket' : "smartclass-a14a0.appspot.com"
})

#importing the students images
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentsIds = []
for path in PathList:
      imgList.append(cv2.imread(os.path.join(folderPath,path)))
      studentsIds.append(os.path.splitext(path)[0])

      fileName=f'{folderPath}/{path}'
      bucket = storage.bucket()
      blob = bucket.blob(fileName)
      blob.upload_from_filename(fileName)


      #print(path)
      #print(os.path.splitext(path)[0])
      print(studentsIds)

      def findEncodings(ImagesList) :
          encodeList = []
          for img in ImagesList:
              cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
              encode = face_recognition.face_encodings(img)[0]
              encodeList.append(encode)

          return encodeList
print("encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentsIds]
print(encodeListKnown)
print("encoding complete")

file =open("EncodeFile.p" , 'wb' )
pickle.dump(encodeListKnownWithIds , file)
file.close()
print("File Saved")