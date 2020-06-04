import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
cap = cv2.VideoCapture(0)


while True:
    ret, frame =cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)

    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    # frameno = frameno+1  
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #exit 
        break

cap.release()