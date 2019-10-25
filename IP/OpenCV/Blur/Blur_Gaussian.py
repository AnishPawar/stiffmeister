import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    garbage,frame=cap.read()

    #kernal = np.ones((25,25))/625
    blur = cv2.GaussianBlur(frame,(25,25),0)

    cv2.imshow('frame',blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release    