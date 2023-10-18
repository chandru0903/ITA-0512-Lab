#agasth

import cv2
import numpy as np

# Load the two images you want to transform
image1 = cv2.imread('summah.jpeg')
image2 = cv2.imread('Agasth.jpeg')

# Define corresponding points in the two images
# You need at least 4 corresponding points to calculate the homography matrix
points_image1 = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)
points_image2 = np.array([[x1_prime, y1_prime], [x2_prime, y2_prime], [x3_prime, y3_prime], [x4_prime, y4_prime]], dtype=np.float32)

# Calculate the homography matrix using the corresponding points
homography_matrix, _ = cv2.findHomography(points_image1, points_image2, cv2.RANSAC, 5.0)

# Apply the homography transformation to image1
transformed_image = cv2.warpPerspective(image1, homography_matrix, (image2.shape[1], image2.shape[0]))

# Display the original and transformed images
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Transformed Image 1', transformed_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
