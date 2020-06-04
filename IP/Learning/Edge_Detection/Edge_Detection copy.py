import cv2
import numpy as np

img = cv2.imread('Flower2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx_kernel=np.array([(-1,-2,-1),
                           (0,0,0),
                           (1,2,1)])

sobely_kernel=np.array([(-1,0,1),
                         (-2,0,2),
                         (-1,0,1)])

blur_kernel = np.ones((25,25))/625

Sobelx = cv2.filter2D(gray,-1,sobelx_kernel)
Sobely = cv2.filter2D(gray,-1,sobely_kernel)
canny = cv2.Canny(img,100,100)
blur = cv2.filter2D(img,-1,blur_kernel)

cv2.imshow("Sobelx",Sobelx)
cv2.imshow("Sobely",Sobely)
cv2.imshow("Canny",blur)

cv2.waitKey(0)