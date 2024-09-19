# this project is to detect moving object from camera
#  
import cv2  #for image

import time #for delay 

import imutils  #for resize

# to take live video from camera (0 for default camera)
cam=cv2.VideoCapture(0)
time.sleep(1)
firstFrame=None
# this will take area for scanning
area=1000

while True:
    # this will read each frame of image and store it to img variable
    _,img=cam.read()
    text="Normal"

    # here we have resized the image
    img=imutils.resize(img,width=500)

    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # color 2 gray scale img

    gaussianImg=cv2.GaussianBlur(grayimg,(21,21),0) #smoothened image
    if firstFrame is None:
        firstFrame=gaussianImg  #capturing first frame on 1st iteration
        continue
    imgDiff=cv2.absdiff(firstFrame,gaussianImg) #absolute difference between 1st & current frame
    threshImg=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] #threshold
    threshImg=cv2.dilate(threshImg,None,iterations=2)
    cnts=cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+y,w+h),(0,255,0),2)
        text="Moving object Detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,225),2)
    cv2.imshow("Camera Feed",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

