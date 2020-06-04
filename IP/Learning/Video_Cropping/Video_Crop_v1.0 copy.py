import cv2
import numpy as np


cap = cv2.VideoCapture(0)
n=int(input('Enter frame 1 size'))
t=int(input('Enter frame 2 size'))
def crop(height,width):
    x1=int(((width)/2)-n)
    x2=int(((width)/2)+n)
    y1=int(((height)/2)-n)
    y2=int(((height)/2)+n)
    cropped = frame[x1:x2, y1:y2]
    # cv2.imshow('video', cropped)
    return cropped  #returning crop to main function

while True:
    ret, frame = cap.read()     
    height, width, channels = frame.shape 
    print(height)
    print(width)
    #cv2.imshow('video', crop(height,width))  #jugaad
    cool = crop(height,width)                 #calling function and defining cropped 
    cv2.imshow('video', cool)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()