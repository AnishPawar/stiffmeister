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
   
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #setting HSV values using slider
    H = cv2.getTrackbarPos('Hue','Control')   
    S = cv2.getTrackbarPos('Saturation','Control')
    V = cv2.getTrackbarPos('Value','Control')
    
    
    lowerred=np.array([H,S,V])
    upperred=np.array([180,255,255])       
    
    mask10 = cv2.inRange(hsv,lowerred,upperred) 
    
    kernal = np.ones((10,10),np.uint8)

    dilation = cv2.dilate(mask10,kernal,iterations = 1) 
    contours,_=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    
    areas = [cv2.contourArea(counter) for counter in contours]
    
    max_index = np.argmax(areas)
    print(max_index)
    max=contours[max_index]

    perimeter = cv2.arcLength(max,True)

    ROI = cv2.approxPolyDP(max,0.02*perimeter,True)

    cv2.drawContours(frame, ROI, -1,(0,255,0),3) 
 
    res = cv2.bitwise_and(frame,frame,mask = mask10) 
    
    
    #cv2.imshow('res',res)  
    cv2.imshow('dilated',dilation)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()