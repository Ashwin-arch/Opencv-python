import cv2

# Open original video
cap = cv2.VideoCapture("/home/ashwin/Downloads/12215493_1920_1080_30fps.mp4")

# Get properties
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

# Define codec for AVI (e.g. XVID)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter
out = cv2.VideoWriter(
    "/home/ashwin/Documents/output_video.avi",
    fourcc,
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Optionally modify frame, e.g. add text
    cv2.putText(frame, "OpenCV2", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2, cv2.LINE_AA)
    
    # Write the frame
    out.write(frame)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
