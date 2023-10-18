#agasth

import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\AGASTH PC\AGATHIYAN\M&I\\summah.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a Laplacian kernel with a negative central coefficient
laplacian_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

# Apply the Laplacian filter to the grayscale image
sharpened_image = cv2.filter2D(gray_image, -1, laplacian_kernel)

# Convert the sharpened image back to BGR if it was originally a color image
if len(image.shape) == 3:
    sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

# Display the original image and the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
