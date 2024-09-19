# In this project we will resize image,Blurring image 
import cv2
import imutils
# reading image
img=cv2.imread("ex1.jpg")

# resizing image by width according to user 
resize=imutils.resize(img,width=300)

# saving resized image
# cv2.imwrite("resized_img.png",resize)
# cv2.imshow("resizedImg",resize)

# blurring the image using gaussian blur
blurImg=cv2.GaussianBlur(img,(25,25),0)
cv2.imwrite("blurImg.png",blurImg)
cv2.imshow("Blurred image",blurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()