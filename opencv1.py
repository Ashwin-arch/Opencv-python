import cv2

# Read an image from disk
img = cv2.imread("/home/ashwin/Documents/Dataset/Dogs/Dog2.jpeg")

# Check if the image loaded properly
if img is None:
    print("Image not found or path incorrect")
else:
    print("Image loaded successfully")

# Display the image in a window
cv2.imshow("My Image", img)

# Wait for a key press (0 = wait indefinitely)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
