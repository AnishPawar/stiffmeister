import cv2
import numpy as np

img = cv2.imread('Flower2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx_kernal=np.matrix([(-1,-1,-1),
                           (0,0,0),
                           (1,1,1)])

sobely_kernal=np.matrix([(-1,0,1),
                         (-1,0,1),
                         (-1,0,1)])

sharpening_kernel = np.array([(-1,-1,-1),
                              (-1,8,-1),
                              (-1,-1,-1)])

Sobelx = cv2.filter2D(gray,-1,sobelx_kernal)
Sobely = cv2.filter2D(gray,-1,sobely_kernal)

Sharpen = cv2.filter2D(gray,-1,sharpening_kernel)

canny = cv2.Canny(img,100,100)


cv2.imshow("Sobelx",Sobelx)
cv2.imshow("Sobely",gray)
cv2.imshow("Canny",Sharpen)

cv2.waitKey(0)