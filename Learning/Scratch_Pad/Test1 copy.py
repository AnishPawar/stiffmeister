import cv2
import numpy as np 

counter = 0
pos1=()
pos2=()
cropped = np.zeros((), np.uint8,)
flag =0

def lol(self):
    pass

def mouse(event,x,y,z,w):
    
    global counter, pos1,pos2
    # pixel = frame[y,x]
    
    if pos1 and pos2:
        if event == cv2.EVENT_LBUTTONDOWN:
            global flag
            pixel=cropped[y,x]
            print(pixel)
            cv2.setTrackbarPos('Lower_Hue','Control',pixel[0]-25)
            cv2.setTrackbarPos('Lower_Saturation','Control',pixel[1]-50)
            cv2.setTrackbarPos('Lower_Value','Control',pixel[2]-50)
            cv2.setTrackbarPos('Upper_Hue','Control',pixel[0]+25)
            cv2.setTrackbarPos('Upper_Saturation','Control',pixel[1]+50)
            cv2.setTrackbarPos('Upper_Value','Control',pixel[2]+50)
            
            flag =1


    if event == cv2.EVENT_LBUTTONDOWN:
        counter = counter+1

        if counter%2 != 0:
            pos1=(y,x)
        
        if counter%2 == 0:
            pos2=(y,x)
            template1(pos1,pos2)   
            
            

def template1(pos1,pos2):       
    cv2.rectangle(frame,pos1,pos2,(0,255,0),2)    
    
    x1,y1=pos1
    x2,y2=pos2
    global cropped
    cropped = frame[x1:x2, y1:y2]
    

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
counter = 0
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

cv2.namedWindow('cropped')
cv2.setMouseCallback('cropped',mouse)

while True:


    _,frame = cap.read()
    
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    if pos1 and pos2 :        
        cv2.imshow('cropped',cropped)    
        cropped_gray=cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
    
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
    
        mask10 = cv2.inRange(cropped,lower_colour,upper_colour) 
        res1 = cv2.bitwise_and(cropped,cropped,mask = mask10)
        res1_gray= cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
        cv2.imshow('mask',res1)

        if flag==1:
            contours,_=cv2.findContours(mask10,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
            cv2.drawContours(res1, contours, -1,(0,0,255),3) 
            template = res1_gray
            cv2.imwrite('mask.jpg',res1)
            width = template.shape[0]
            height = template.shape[1]
            res = cv2.matchTemplate(frame_gray,template,cv2.TM_CCOEFF_NORMED)
        
            thershold = 0.8
            loc = np.where(res>=thershold)
    
            for pt in zip(*loc[::-1]):
            # print(pt)
                cv2.rectangle(frame,(pt),(pt[0]+height,pt[1]+width),(0,0,255),1)
    
    cv2.imshow('frame',frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows