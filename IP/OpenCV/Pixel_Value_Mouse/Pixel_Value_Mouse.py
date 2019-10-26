import cv2
import numpy as np 

def mouse(event,x,y,z,w):
    print(x,y)
    pixel = img[y,x]
    #print(pixel)
    

#Mouse function
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse)

   
img = cv2.imread('lambo.jpg')
cv2.imshow('image',img)
#print(img[1200,60])
cv2.waitKey(0)
#print(len(img))