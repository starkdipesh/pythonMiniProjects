# In this practical we are going to read image, copy image, show image and convert it into gray scale image
import cv2 

#1. this line of code is going to read image
img=cv2.imread("ex1.jpg")

#2. this line of code is going to copy that readed image
cv2.imwrite("ex1_1.png",img)

#3. this line of code is going to show image in window
# cv2.imshow("image",img)

#4. this line will change color of image bgr to gray
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimg",grayimg)

#5. this will stop window upto we don't click cross or 0 
cv2.waitKey(0)
#6. this will destroy window after clicking 
cv2.destroyAllWindows()