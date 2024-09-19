#object tracking by color : In this project we will code to track object by color and find direction were to go .
# cv2 use to take image frame by camera
import cv2 
# imutils use to resize image frame
import imutils 

YellowLower=(45,164,162)
YellowUpper=(45,232,255)
camera=cv2.VideoCapture(0)

while True:
    # reading camera image
    (grabbed,frame)=camera.read()
    # resizing image frame
    frame=imutils.resize(frame,width=600)
    blured=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blured,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,YellowLower,YellowUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"],int(M["m01"]/M["m00"])))
        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius >250:
                print("STOP")
            else:
                if (center[0]<150):
                    print("left")
                elif (center[0]>450):
                    print("Right")
                elif (center[0]>250):
                    print("Front")
                else:
                    print("Stop")
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
