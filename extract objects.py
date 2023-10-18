#agasth

import cv2
img = cv2.imread("C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample1.jpg")
x, y = 100, 100
width, height = 200, 150
roi = img[y:y+height, x:x+width]
roi1=cv2.resize(roi,(100,100))
cv2.imshow('ROI', roi1)
cv2.waitKey(0)
cv2.destroyAllWindows()
