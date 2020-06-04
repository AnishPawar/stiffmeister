import cv2
import numpy as np

img = cv2.imread('Barca1.jpg')

kernel = np.ones((15,15))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(41,41),0)
canny = cv2.Canny(blur,25,25)

dilation = cv2.dilate(canny,kernel,iterations = 1)

opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

contours,_=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
areas = [cv2.contourArea(counter) for counter in contours]
    
max_index = np.argmax(areas)
print(max_index)
max=contours[max_index]
print(max)    
# cv2.drawContours(img, contours, -1,(0,0,255),3) 


cv2.drawContours(img,max,-1,(255,255,0),10)

cv2.imshow('frame',img)
cv2.waitKey(0)