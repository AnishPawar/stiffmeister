import cv2
import numpy as np 
import random
counter = 0
pos1=()
pos2=()
cropped = np.zeros((), np.uint8)
def mouse(event,x,y,z,w):
    
    global counter, pos1,pos2
    pixel = frame[y,x]
    
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

#Mouse function
counter = 0
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

while True:
    

    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)  
    if pos1 and pos2 :        
        cv2.imshow('cropped',cropped)    
        cropped_gray=cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
        template = cropped_gray
        
        width = template.shape[0]
        height = template.shape[1]
        res = cv2.matchTemplate(frame_gray,template,cv2.TM_CCOEFF_NORMED)
        
        thershold = 0.7
        loc = np.where(res>=thershold)
        

        # print(loc)    

        for pt in zip(*loc[::-1]):
            # print(pt)
            cv2.rectangle(frame,(pt),(pt[0]+height,pt[1]+width),(0,0,255),1)
    
    cv2.imshow('frame',frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows