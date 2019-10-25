import cv2
cap = cv2.VideoCapture(0)
frameno = 0
n =int(input("Enter value: ")) 
n=n-1

def flipfunction(frameno):
    
 if frameno%n==0:       #flip decision loop
    cv2.imshow('frame',flipVertical)
 else:
    cv2.imshow('frame',frame)



while True:
    ret, frame =cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      
    flipVertical = cv2.flip(frame, -1) #frame flip

    frameno = frameno+1  
    flipfunction(frameno) 

    if cv2.waitKey(1) & 0xFF == ord('q'): #exit 
        break

cap.release()
