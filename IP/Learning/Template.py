import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    # red_channel= frame[:,:,2]
    # red_img = np.array(frame.shape)

    # red_img[:,:,2]=red_channel
    frame_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    template = cv2.imread('Template.jpg',0)
    
    width = template.shape[0]
    height = template.shape[1]
    
    res = cv2.matchTemplate(frame_gray,template,cv2.TM_CCOEFF_NORMED)
 
    thershold = 0.8
    loc = np.where(res>=thershold)
    print(loc)
    for pt in zip(*loc[::-1]):
        #print(pt)
        cv2.rectangle(frame,pt,(pt[0]+width,pt[1]+height),(0,255,0),2)
    cv2.imshow('frame',frame)   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

