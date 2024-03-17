import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(r"D:\photes\New folder\new.mp4")

while True:
    success, img = cap.read()
    
    # Check if frame is empty
    if not success:
        print("End of video or unable to read frame.")
        break
    
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
