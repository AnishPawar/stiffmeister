import cv2
import numpy as np

mask1 = cv2.imread('Masking.png')
img1  = cv2.imread('Flower.jpg')
img2 = cv2.imread('Flower2.jpg')


new1 = cv2.resize(img1,mask1.shape[1::-1])
new2 = cv2.resize(img2,mask1.shape[1::-1])

print(new2.shape)

new_mask  = cv2.bitwise_not(mask1)
res = cv2.bitwise_and(new1,new2,mask = None)

cv2.imshow('res',res)
cv2.waitKey(0)