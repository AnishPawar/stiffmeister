import cv2
import numpy as np
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')
a_cascade = cv2.CascadeClassifier('a_cascade.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
# envolope = np.array()


while True:
    _,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    a = a_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in a:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,0),5)
        cv2.putText(frame,'a',((x+20),y+20),font,1,(0,255,0),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break