import cv2 
# access model file
algo="haarcascade_frontalface_default.xml"
# to load casecade file
haarcascade=cv2.CascadeClassifier(algo)
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haarcascade.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",img)
    # press esc to stop detection 
    key=cv2.waitKey(1) & 0xFF 
    if key ==27:
        break
cam.release()
cv2.destroyAllWindows()