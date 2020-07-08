# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# def lol(self):
#     pass

# Left = cv2.imread('Left_Cam.jpg')
# Left_Gray = cv2.cvtColor(Left,cv2.COLOR_BGR2GRAY)

# print(Left_Gray.shape)

# Right = cv2.imread('Right_Cam.jpg')
# Right_Gray = cv2.cvtColor(Right,cv2.COLOR_BGR2GRAY)
# print(Right_Gray.shape)

# cv2.namedWindow('Controls')
# cv2.createTrackbar('minDisparity','Controls',0,255,lol)
# cv2.createTrackbar('numDisparities','Controls',0,255,lol)
# cv2.createTrackbar('blockSize','Controls',0,255,lol)
# cv2.createTrackbar('P1','Controls',0,255,lol)
# cv2.createTrackbar('P2','Controls',0,255,lol)
# cv2.createTrackbar('disp12MaxDiff','Controls',0,255,lol)
# cv2.createTrackbar('preFilterCap','Controls',0,255,lol)
# cv2.createTrackbar('uniquenessRatio','Controls',0,255,lol)
# cv2.createTrackbar('speckleRange','Controls',0,255,lol)
# cv2.createTrackbar('speckleWindowSize','Controls',0,255,lol)



# while True:
    
#     minDisparity = cv2.getTrackbarPos('minDisparity','Controls')
#     numDisparities = cv2.getTrackbarPos('numDisparities','Controls')
#     blockSize = cv2.getTrackbarPos('blockSize','Controls')
#     P1 = cv2.getTrackbarPos('P1','Controls')
#     P2 = cv2.getTrackbarPos('P2','Controls')
#     disp12MaxDiff = cv2.getTrackbarPos('disp12MaxDiff','Controls')
#     preFilterCap = cv2.getTrackbarPos('preFilterCap','Controls')
#     uniquenessRatio = cv2.getTrackbarPos('uniquenessRatio','Controls')
#     speckleWindowSize = cv2.getTrackbarPos('speckleWindowSize','Controls')
#     speckleRange = cv2.getTrackbarPos('speckleRange','Controls')
    
#     stereo = cv2.StereoSGBM_create(minDisparity=35,numDisparities=103,blockSize=6,P1=246 ,P2 =255,disp12MaxDiff=8,preFilterCap=0,uniquenessRatio=0,speckleWindowSize=0,speckleRange=0)
#     # stereo = cv2.StereoSGBM_create(minDisparity=minDisparity,numDisparities=numDisparities,blockSize=blockSize,P1=P1,P2=P2,disp12MaxDiff=disp12MaxDiff,preFilterCap=preFilterCap,uniquenessRatio=uniquenessRatio,speckleWindowSize=speckleWindowSize,speckleRange=speckleRange)
#     disparity = stereo.compute(Left_Gray,Right_Gray)

#     # Golden_values  
#     # minDisparity = 35 
#     # numDisparities = 103 
#     # blockSize = 6 
#     # P1 = 246
#     # P2 = 255
#     # disp12MaxDiff = 8
#     # preFilterCap = 0 
#     # uniquenessRatio =0 
#     # speckleWindowSize = 0 
#     # speckleRange = 0

#     plt.imshow(disparity,'gray')
#     print(minDisparity,numDisparities,blockSize,P1,P2,disp12MaxDiff,preFilterCap,uniquenessRatio,speckleWindowSize,speckleRange)
#     plt.show()
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
        


import numpy as np
import cv2
import requests
import matplotlib.pyplot as plt

url_left = r"http://192.168.0.104:8080/shot.jpg"
url_right = r"http://192.168.0.105:8080/shot.jpg"
while True:

    online_vid_left = requests.get(url_left)
    online_vid_left_arr = np.array(bytearray(online_vid_left.content),dtype = np.uint8)
    online_img_left = cv2.imdecode(online_vid_left_arr, -1)

    online_vid_right = requests.get(url_right)
    online_vid_right_arr = np.array(bytearray(online_vid_right.content),dtype = np.uint8)
    online_img_right = cv2.imdecode(online_vid_right_arr, -1)
    

    img_left = online_img_left 
    img_left = cv2.flip(img_left,-1)
    img_left_gray = cv2.cvtColor(img_left,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Left_Cam.jpg',img_left_gray)
    cv2.imshow('Left',img_left)
    print(img_left.shape)
    img_right = online_img_right 
    img_right_gray = cv2.cvtColor(img_right,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Right_Cam.jpg',img_right_gray)
    cv2.imshow('Right',img_right)
    print(img_right.shape)
    
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    disparity = stereo.compute(img_left_gray,img_left_gray)


    # plt.imshow(disparity,'gray')
    # plt.ion()
    # plt.show()
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cv2.destroyAllWindows()

