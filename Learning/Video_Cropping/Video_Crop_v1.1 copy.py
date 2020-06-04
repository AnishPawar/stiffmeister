import cv2

cap = cv2.VideoCapture(0)
n=int(input('Enter frame 1 size: '))
t=int(input('Enter frame 2 size: '))
frameno=0                   #counter initialisation
def crop(height,width):          
    x1=int(((width)/2)-n)       #image size 1
    x2=int(((width)/2)+n)
    y1=int(((height)/2)-n)
    y2=int(((height)/2)+n)
    
    x11=int(((width)/2)-t)
    x21=int(((width)/2)+t)
    y11=int(((height)/2)-t)
    y21=int(((height)/2)+t)
    
    cropped = frame[x1:x2, y1:y2]     #cropped image1
    croppedxl = frame[x11:x21, y11:y21 ] #cropped image1
    
    frameloop(cropped,croppedxl)        #calling frameloop for passing values

def frameloop(cropped,croppedxl):      #crop decision loop
    if frameno%2==0:
        cv2.imshow('frame',cropped)
    else:
        cv2.imshow('frame',croppedxl)

while True:                             #capture loop
    ret, frame = cap.read()
    
    frameno = frameno+1
    height, width, channels = frame.shape #reading height and width of frame
    crop(height,width)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()
