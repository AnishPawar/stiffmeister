import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# def mouse_left(event,x,y,params,flags):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#         cv2.line(Left,(int(width/2),height),(x,y),(0,255,0),10)
#         m1 = (y-height)/(x-width/2)
#         alpha = math.atan(m1)
#         print(m1)

# def mouse_right(event,x,y,params,flags):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#         cv2.line(Right,(int(width/2),height),(x,y),(0,255,0),10)
#         m2 = (y-height)/(x-width/2)
#         beta = math.atan(m2)
#         print(m2)

# cv2.namedWindow('Left')
# cv2.setMouseCallback('Left',mouse_left)

# cv2.namedWindow('Right')
# cv2.setMouseCallback('Right',mouse_right)

# Left = cv2.imread('Left.JPG')
# Right = cv2.imread('Right.JPG')

# while True:

#     cv2.imshow('Left',Left)
#     height = Left.shape[0]
#     width = Left.shape[1]

#     cv2.imshow('Right',Right)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# intermidiate = 0.3*math.tan(1.0954085731866416)*math.tan(1.038467415357244+1.57079632679)
# final_distance = intermidiate/(math.tan(1.0954085731866416)+math.tan(1.038467415357244+1.57079632679))
# print(final_distance)

final_distance = (30*1.9328358208955223*1.6950053134962806)/(1.9328358208955223+1.6950053134962806)
print(final_distance)