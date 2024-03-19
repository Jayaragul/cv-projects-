import cv2
# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it if you have multiple cameras

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Camera", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
