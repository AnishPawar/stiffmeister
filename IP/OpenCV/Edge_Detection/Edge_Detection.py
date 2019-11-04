import cv2
import numpy as np

img = cv2.imread('Flower2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx_kernal=np.matrix([(-1,-2,-1),
                  (0,0,0),
                  (1,2,1)])

sobely_kernal=np.matrix([(-1,0,1),
                         (-2,0,2),
                         (-1,0,1)])



Sobelx = cv2.filter2D(gray,-1,sobelx_kernal)
Sobely = cv2.filter2D(gray,-1,sobely_kernal)
canny = cv2.Canny(img,100,100)

cv2.imshow("Sobelx",Sobelx)
cv2.imshow("Sobely",Sobely)
cv2.imshow("Canny",canny)

cv2.waitKey(0)