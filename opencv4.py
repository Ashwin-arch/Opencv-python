import cv2
import numpy as np

# Black canvas
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a white line from top-left to bottom-right
cv2.line(img, (50, 50), (350, 350), (255, 255, 255), 2)

cv2.imshow("Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
