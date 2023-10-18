#agasth


import cv2 as c
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
image_path = "C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample1.jpg"
img = c.imread(image_path)
imggray = c.cvtColor(img, c.COLOR_BGR2GRAY)
imgblur = c.GaussianBlur(imggray,(7,7),0)
imgcanny = c.Canny(imgblur,100,200)
d_width = 800
d_height = 600
img_resized = c.resize(imgcanny,(d_width,d_height))
c.imshow("Image Canny",img_resized)
c.imshow("Original Image",img)
c.waitKey(0)
