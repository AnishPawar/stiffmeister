# lowerred=np.array([69,171,64])

import cv2
import numpy as np
# import requests
    
# url = r"http://192.168.0.101:8080/shot.jpg"

# while True:
#     online_vid = requests.get(url)
#     online_vid_arr = np.array(bytearray(online_vid.content),dtype = np.uint8)
#     online_img = cv2.imdecode(online_vid_arr, -1)

#     frame = online_img 
   
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#     lowerred=np.array([69,171,64])
#     # lowerred = np.array([0,0,0])
#     upperred=np.array([180,255,255])        
    
#     mask10 = cv2.inRange(hsv,lowerred,upperred) 
    
#     kernal = np.ones((10,10),np.uint8)

#     dilation = cv2.dilate(mask10,kernal,iterations = 1) 
#     res = cv2.bitwise_and(frame,frame,mask = mask10) 
#     contours,_=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    
#     areas = [cv2.contourArea(counter) for counter in contours]
    
#     if np.any(areas):
#         max_index = np.argmax(areas)
#         print(max_index)
#         max_contour=contours[max_index]
#         x,y,w,h = cv2.boundingRect(max_contour)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
#         print(w,h)
     
#     #cv2.imshow('res',res)  
#     cv2.imshow('dilated',dilation)
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

disparity_map = cv2.imread('Disparity_Map_Updated.png')
Left = cv2.imread('Left_Cam.jpg')
Right = cv2.imread('Right_Cam.jpg')
cv2.imshow('DM',disparity_map)
# median_blur = cv2.medianBlur(disparity_map,3)
# cv2.imshow('median',median_blur)
opened = cv2.morphologyEx(disparity_map,cv2.MORPH_OPEN,np.ones((5,5)))
cv2.imshow('opened',opened)
cv2.imshow('Left',Left)
cv2.imshow('Right',Right)
cv2.waitKey(0)