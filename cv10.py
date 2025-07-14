import cv2

img = cv2.imread("/home/ashwin/Documents/Dataset/Dogs/Dog2.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 7)
edges = cv2.Canny(median, 50, 150)
sketch = cv2.bitwise_not(edges)

cv2.imshow("Original", img)
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
