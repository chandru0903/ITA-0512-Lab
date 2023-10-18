import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\AGASTH PC\AGATHIYAN\M&I\\summah.jpeg')

# Define the Sobel operator for x-axis
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Apply the Sobel operator to the image
edges_x = cv2.filter2D(image, -1, sobel_x)

# Display the original image and the edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection (Sobel x-axis)', edges_x)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
