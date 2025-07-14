import cv2
import numpy as np

# Create a black background
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a rectangle:
# Top-left corner (50, 50)
# Bottom-right corner (300, 150)
# Rectangle width = 250, height = 100 → NOT a square!
cv2.rectangle(img, (50, 50), (300, 150), (0, 255, 0), 5)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
