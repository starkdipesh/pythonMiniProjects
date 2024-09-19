# this practical we are going to convert image into binary or gray scale image 
import cv2 

# reading the image
img=cv2.imread("ex1.jpg")

# here we will change image color bgr to gray
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# now we will change this gray color image into gray-scale or treshold image
tresimg=cv2.threshold(grayimg,190,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresh_ex1.jpg",tresimg)
cv2.imshow("threshimg",tresimg)

cv2.waitKey(0)
cv2.destroyAllWindows()