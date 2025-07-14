import cv2
import numpy as np

# Black canvas
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a blue filled circle
cv2.circle(img, (200, 200), 50, (255, 0, 0), -1)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
