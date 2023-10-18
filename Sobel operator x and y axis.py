import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\AGASTH PC\AGATHIYAN\M&I\\summah.jpeg')

# Define the Sobel operators for x and y axes
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply the Sobel operators to the image to find gradients along x and y axes
edges_x = cv2.filter2D(image, -1, sobel_x)
edges_y = cv2.filter2D(image, -1, sobel_y)

# Combine the x and y gradient images to get the overall edge strength
edges = cv2.addWeighted(edges_x, 0.5, edges_y, 0.5, 0)

# Display the original image and the edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection (Sobel xy-axis)', edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
