# In this practical we will try to use camera for detection

import cv2

# initializing the camera
vs = cv2.VideoCapture(0)

while True:
    # storing the frame from the camera
    ret, img = vs.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("video_stream", img)
# the video capturing will stop after pressing q key
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# releasing the camera and closing all windows
vs.release()
cv2.destroyAllWindows()
