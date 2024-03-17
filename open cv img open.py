import cv2

# Load image
img = cv2.imread("D:\photes\photo_2024-03-09_17-37-53.jpg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display original and grayscale images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
