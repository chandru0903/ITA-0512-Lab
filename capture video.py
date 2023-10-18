#agasth

import cv2 
import numpy as np
cap = cv2.VideoCapture("c:\\Movies\\Farzi_(2023)_S01_EP_(01-08)_HQ_HDRip_-_x264_-_[Tel_+_Tam]_ESub.mkv.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'): #waitkey value changes the speed 
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


