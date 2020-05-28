import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    garbage,frame=cap.read()

    kernal = np.ones((25,25))/625
    Gaussian_blur = cv2.GaussianBlur(frame,(25,25),0)
    Mean_blur = cv2.filter2D(frame,-1,kernal)
    cv2.imshow('frame',Gaussian_blur)
    cv2.imshow('Mean Blur',Mean_blur)
    opacity=0.4
    img = cv2.imread('Flower.jpg')
    
    cv2.addWeighted(frame, opacity, img, 1 - opacity, 0, img)

    cv2.imshow('result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release    