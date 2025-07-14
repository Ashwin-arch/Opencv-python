import cv2

# Read an image from disk
img = cv2.imread("/home/ashwin/Documents/Dataset/Dogs/Dog2.jpeg")

# Check if the image loaded properly
if img is None:
    print("Image not found or path incorrect")
else:
    print("Image loaded successfully")

    # Save as PNG
    result = cv2.imwrite("/home/ashwin/Documents/Dataset/Dogs/Dog2.png", img)

    if result:
        print("Image saved successfully!")
    else:
        print("Failed to save image.")
