# this program is to detect face data using frontalface algorithm

import cv2 
import os 
dataset="Dataset"
name="manav"
path=os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) =(130,100)
algo="haarcascade_frontalface_default.xml"
haarCasecade=cv2.CascadeClassifier(algo)
cam=cv2.VideoCapture(0)
count=1
while count<50:
    print(count)
    _,img=cam.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haarCasecade.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        face_only=grayimg[y:y+h,x:x+w]
        resizeimg=cv2.resize(face_only,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeimg)
        count+=1
    cv2.imshow("Face Detection ",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
print("Image Captured Succesfully")
cam.release()
cv2.destroyAllWindows()
