import cv2
import numpy as np

# Create a red image with dimensions 1280x720
image = np.zeros((720, 1280, 3), dtype=np.uint8)
image[:, :] = (0, 0, 255)  # Set all pixels to red (BGR format)

# Display the image
cv2.imshow("Red Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

