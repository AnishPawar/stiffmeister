import cv2
import numpy as np
img = cv2.imread('HP2.jpg')
 
kernal = np.ones((25,25),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
dilation = cv2.dilate(img,kernal,iterations = 1) 
erosion = cv2.erode(img,kernal,iterations = 1) 
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)

cv2.imshow('dilate',dilation)

print(dilation)
cv2.waitKey(0)