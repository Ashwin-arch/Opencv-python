import cv2
import numpy as np

# Create a black background
img = np.zeros((400, 600, 3), dtype=np.uint8)

# Write text
cv2.putText(
    img,
    "Ghindra",                   # Text string
    (50, 200),                   # Bottom-left corner (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,    # Font
    3,                           # Font scale
    (0, 255, 0),                 # Color (Green)
    5,                           # Thickness
    cv2.LINE_AA                  # Line type
)

cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
