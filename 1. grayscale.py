#agasth
import cv2 as c
import numpy as np
kernal = np.ones((5,5),np.uint8)
print(kernal)
path ="C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample.jpg"
img = c.imread(path)
imgG = c.cvtColor(img,c.COLOR_BGR2GRAY)
imgB = c.GaussianBlur(imgG,(7,7),0)
imgC = c.Canny(imgB,100,200)
imgD = c.dilate(imgC,kernal,iterations = 10)
d_w = 800
d_h = 600
imgR = c.resize(imgD,(d_w,d_h))
c.imshow('Image Dilate',imgR)
c.waitKey(0)
