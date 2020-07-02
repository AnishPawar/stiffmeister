import cv2
import matplotlib.pyplot as plt
import numpy as np


Left = cv2.imread('Left_Cam.jpg')
Left_Gray = cv2.cvtColor(Left,cv2.COLOR_BGR2GRAY)

Right = cv2.imread('Right_Cam.jpg')
Right_Gray = cv2.cvtColor(Right,cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoSGBM_create(minDisparity=35,numDisparities=103,blockSize=6,P1=246 ,P2 =255,disp12MaxDiff=8,preFilterCap=0,uniquenessRatio=0,speckleWindowSize=0,speckleRange=0)
disparity = stereo.compute(Left_Gray,Right_Gray)
plt.imshow(disparity,'gray')
plt.show()

    # Golden_values  
    # minDisparity = 35 
    # numDisparities = 103 
    # blockSize = 6 
    # P1 = 246
    # P2 = 255
    # disp12MaxDiff = 8
    # preFilterCap = 0 
    # uniquenessRatio =0 
    # speckleWindowSize = 0 
    # speckleRange = 0
