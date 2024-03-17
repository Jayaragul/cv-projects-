import cv2
import numpy as np
img1 = cv2.imread(r"D:\photes\photo_2024-03-09_17-37-55.jpg")
img = np.zeros((512,512,3),np.uint8)

cv2.line(img1,(0,0),(img.shape[1],img.shape[0]),(255,255,0),3)
cv2.rectangle(img1,(0,0),(250,350),(0,0,255),2)
cv2.circle(img1,(400,50),30,(255,255,0),5)
cv2.putText(img1," njr ",(300,200),cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),3)
cv2.imshow("Image",img1)

cv2.waitKey(0)
