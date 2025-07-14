import cv2
import numpy as np

img = cv2.imread("/home/ashwin/Documents/Dataset/Dogs/Dog2.jpeg")

# Translate
M_trans = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(img, M_trans, (img.shape[1], img.shape[0]))

# Rotate
(h, w) = img.shape[:2]
M_rot = cv2.getRotationMatrix2D((w // 2, h // 2), 30, 1.0)
rotated = cv2.warpAffine(img, M_rot, (w, h))

# Threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Translated", shifted)
cv2.imshow("Rotated", rotated)
cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
