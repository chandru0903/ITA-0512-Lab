import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\AGASTH PC\AGATHIYAN\M&I\\summah.jpeg')

# Define the Sobel operator for y-axis
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply the Sobel operator to the image
edges_y = cv2.filter2D(image, -1, sobel_y)

# Display the original image and the edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection (Sobel y-axis)', edges_y)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
