import cv2
import matplotlib.pyplot as plt
import numpy as np

Left = cv2.imread('Left_Cam.jpg')
Left_Gray = cv2.cvtColor(Left,cv2.COLOR_BGR2GRAY)

print(Left_Gray.shape)

Right = cv2.imread('Right_Cam.jpg')
Right_Gray = cv2.cvtColor(Right,cv2.COLOR_BGR2GRAY)
print(Right_Gray.shape)

# stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM_create(numDisparities = 64,blockSize=7)

disparity = stereo.compute(Left_Gray,Right_Gray)



plt.imshow(disparity,'gray')
plt.show()
# import numpy as np
# import cv2
# import requests

# url_left = r"http://192.168.0.104:8080/shot.jpg"
# url_right = r"http://192.168.0.103:8080/shot.jpg"
# while True:

#     online_vid_left = requests.get(url_left)
#     online_vid_left_arr = np.array(bytearray(online_vid_left.content),dtype = np.uint8)
#     online_img_left = cv2.imdecode(online_vid_left_arr, -1)

#     online_vid_right = requests.get(url_right)
#     online_vid_right_arr = np.array(bytearray(online_vid_right.content),dtype = np.uint8)
#     online_img_right = cv2.imdecode(online_vid_right_arr, -1)
    

#     img_left = online_img_left 
#     img_left = cv2.flip(img_left,-1)
#     img_left_gray = cv2.cvtColor(img_left,cv2.COLOR_BGR2GRAY)
#     cv2.imwrite('Left_Cam.jpg',img_left_gray)
#     cv2.imshow('Left',img_left)
#     print(img_left.shape)
#     img_right = online_img_right 
#     img_right_gray = cv2.cvtColor(img_right,cv2.COLOR_BGR2GRAY)
#     cv2.imwrite('Right_Cam.jpg',img_right_gray)
#     cv2.imshow('Right',img_right)
#     print(img_right.shape)
    
#     stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

#     disparity = stereo.compute(img_left_gray,img_left_gray)



    

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break   

# cv2.destroyAllWindows()
# plt.imshow(disparity,'gray')
# plt.show()