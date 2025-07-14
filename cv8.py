import cv2
import numpy as np

img = cv2.imread("/home/ashwin/Documents/Dataset/Dogs/Dog2.jpeg")

# 1. Averaging
average = cv2.blur(img, (5, 5))

# 2. Gaussian
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median
median = cv2.medianBlur(img, 5)

# 4. Bilateral
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

# 5. Sharpening
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Average Blur", average)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
