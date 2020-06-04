import cv2
import numpy as np 

def mouse(event,x,y,z,w):
    #print(x,y)
    pixel = res[y,x]
    print(pixel)
    
def lol(self):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('Control')
cv2.createTrackbar('Hue','Control',0,180,lol)
cv2.createTrackbar('Saturation','Control',0,255,lol)
cv2.createTrackbar('Value','Control',0,255,lol)

#Mouse function
cv2.namedWindow('res')
cv2.setMouseCallback('res',mouse)

while True:
    xg,frame = cap.read()
    #cv2.imshow("frame",frame)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #setting HSV values using slider
    H = cv2.getTrackbarPos('Hue','Control')   
    S = cv2.getTrackbarPos('Saturation','Control')
    V = cv2.getTrackbarPos('Value','Control')
    
    #lower and upper limit of 
    lowerred=np.array([H,S,V])
    upperred=np.array([180,255,255])       
    
    mask10 = cv2.inRange(hsv,lowerred,upperred) 
    
    res = cv2.bitwise_and(frame,frame,mask = mask10) #logical and of mask and image
    
    #print(res)
    cv2.imshow('res',res)  
    cv2.imshow('mask',mask10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
print(len(res))