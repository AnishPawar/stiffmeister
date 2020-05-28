import cv2
import numpy as np 
counter = 0
def mouse(event,x,y,z,w):
    pixel = hsv[y,x]
    
      
    if event == cv2.EVENT_LBUTTONDOWN:
        print(pixel)

        cv2.setTrackbarPos('Lower_Hue','Control',pixel[0]-25)
        cv2.setTrackbarPos('Lower_Saturation','Control',pixel[1]-50)
        cv2.setTrackbarPos('Lower_Value','Control',pixel[2]-50)
        cv2.setTrackbarPos('Upper_Hue','Control',pixel[0]+25)
        cv2.setTrackbarPos('Upper_Saturation','Control',pixel[1]+50)
        cv2.setTrackbarPos('Upper_Value','Control',pixel[2]+50)
    
    
    
def lol(self):
    pass


cap = cv2.VideoCapture(0)

#Trackbar Initialisation
cv2.namedWindow('Control')
cv2.createTrackbar('Lower_Hue','Control',0,180,lol)
cv2.createTrackbar('Lower_Saturation','Control',0,255,lol)
cv2.createTrackbar('Lower_Value','Control',0,255,lol)
cv2.createTrackbar('Upper_Hue','Control',0,180,lol)
cv2.createTrackbar('Upper_Saturation','Control',0,255,lol)
cv2.createTrackbar('Upper_Value','Control',0,255,lol)

#Mouse function
cv2.namedWindow('res')
cv2.setMouseCallback('res',mouse)

while True:
    xg,frame = cap.read()
    #cv2.imshow("frame",frame)
    

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv,(15,15),0)
    kernal = np.ones((15,15),np.uint8)
    #dilation = cv2.dilate(blur,kernal,iterations = 1) 
    #setting HSV values using slider
    LH = cv2.getTrackbarPos('Lower_Hue','Control')   
    UH = cv2.getTrackbarPos('Upper_Hue','Control')   
    LS = cv2.getTrackbarPos('Lower_Saturation','Control')
    US = cv2.getTrackbarPos('Upper_Saturation','Control')
    LV = cv2.getTrackbarPos('Lower_Value','Control')
    UV = cv2.getTrackbarPos('Upper_Value','Control')
    
    #lower and upper limit of 
    lower_colour=np.array([LH,LS,LV])
    upper_colour=np.array([UH,US,UV])       
    
    mask10 = cv2.inRange(blur,lower_colour,upper_colour) 
    

    contours,_=cv2.findContours(mask10,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: 
            cv2.drawContours(frame, contours, -1,(0,255,0),-1) 
    
    template = cv2.bitwise_and(frame,frame,mask = mask10) 
    template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    frame_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('Template.jpg',0)
    
    width = template.shape[0]
    height = template.shape[1]
    
    # res = cv2.matchTemplate(frame_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    # thershold = 0.5
    # loc = np.where(res>=thershold)
    
    # for pt in zip(*loc[::-1]):
    #     #print(pt)
    #     cv2.rectangle(frame,pt,(pt[0]+width,pt[1]+height),(0,255,0),2)
    
    
    cv2.imshow('res',frame)  
    cv2.imshow('mask',mask10)
    cv2.imshow('template',template)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
