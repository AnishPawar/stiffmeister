import cv2
import numpy as np 
      
counter = 0
pos1=()

def lol(self):
    pass

def mouse1(event,x,y,z,w):
    
    global counter, pos1#,pos2
    pixel = frame[y,x]
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.setTrackbarPos('Lower_Hue','Control',pixel[0]-25)
        cv2.setTrackbarPos('Lower_Saturation','Control',pixel[1]-50)
        cv2.setTrackbarPos('Lower_Value','Control',pixel[2]-50)
        cv2.setTrackbarPos('Upper_Hue','Control',pixel[0]+25)
        cv2.setTrackbarPos('Upper_Saturation','Control',pixel[1]+50)
        cv2.setTrackbarPos('Upper_Value','Control',pixel[2]+50)


def mouse(event,x,y,z,w):
    
    global counter, pos1#,pos2
    pixel = frame[y,x]
    
    if event == cv2.EVENT_LBUTTONDOWN:
        counter = counter+1

        if counter%2 != 0:
            pos1=(y,x)
        
        if counter%2 == 0:
            pos2=(y,x)
            template1(pos1,pos2)   
            cv2.namedWindow('cropped')
            cv2.setMouseCallback('cropped',mouse1)
            cv2.namedWindow('Control')
            cv2.createTrackbar('Lower_Hue','Control',0,180,lol)
            cv2.createTrackbar('Lower_Saturation','Control',0,255,lol)
            cv2.createTrackbar('Lower_Value','Control',0,255,lol)
            cv2.createTrackbar('Upper_Hue','Control',0,180,lol)
            cv2.createTrackbar('Upper_Saturation','Control',0,255,lol)
            cv2.createTrackbar('Upper_Value','Control',0,255,lol)
            
            cropped1=cv2.imread('template.jpg')
            hsv = cv2.cvtColor(cropped1,cv2.COLOR_BGR2HSV)
            blur = cv2.GaussianBlur(hsv,(15,15),0)
            kernal = np.ones((15,15),np.uint8)
            LH = cv2.getTrackbarPos('Lower_Hue','Control')   
            UH = cv2.getTrackbarPos('Upper_Hue','Control')   
            LS = cv2.getTrackbarPos('Lower_Saturation','Control')
            US = cv2.getTrackbarPos('Upper_Saturation','Control')
            LV = cv2.getTrackbarPos('Lower_Value','Control')
            UV = cv2.getTrackbarPos('Upper_Value','Control')

            lower_colour=np.array([LH,LS,LV])
            upper_colour=np.array([UH,US,UV])       
            mask10 = cv2.inRange(blur,lower_colour,upper_colour)
            cv2.imshow('mask',mask10)
            

            
    
    #lower and upper limit of 
            

def template1(pos1,pos2):       
    # print(pos1,pos2)
    # print(max(pos1,pos2))
    cv2.rectangle(frame,min(pos1,pos2),max(pos1,pos2),(0,255,0),2)    
    
    x1,y1=pos1
    x2,y2=pos2
    cropped = frame[x1:x2, y1:y2]
    cv2.imshow('cropped',cropped)
    # return cropped
    cv2.imwrite('template.jpg',cropped)


    # video_loop()

cap = cv2.VideoCapture(0)

#Mouse function
counter = 0
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

while True:
    
    _,frame = cap.read()
    
    # cropped=template1(pos1,pos2)    
    # print(cropped)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)  
    
    template = cv2.imread('template.jpg',0)
    width = template.shape[0]
    height = template.shape[1]
    
    res = cv2.matchTemplate(frame_gray,template,cv2.TM_CCOEFF_NORMED)
 
    thershold = 0.8
    loc = np.where(res>=thershold)
    
    for pt in zip(*loc[::-1]):
    
        cv2.rectangle(frame,(pt[0],pt[1]),(pt[0]+height,pt[1]+width),(0,255,0),1)
    cv2.imshow('frame',frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows