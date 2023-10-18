import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\AGASTH PC\AGATHIYAN\M&I\\summah.jpeg')

# Define the transformation matrix
# For example, let's do a simple 2x scaling
scale_factor_x = 2
scale_factor_y = 2
affine_matrix = np.array([[scale_factor_x, 0, 0],
                          [0, scale_factor_y, 0]], dtype=np.float32)

# Apply the affine transformation
transformed_image = cv2.warpAffine(image, affine_matrix, (image.shape[1], image.shape[0]))

# Display the transformed image
cv2.imshow('Affine Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
