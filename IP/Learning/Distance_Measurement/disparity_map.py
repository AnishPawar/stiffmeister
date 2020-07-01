import cv2
import matplotlib.pyplot as plt
import numpy as np

Left = cv2.imread('Left_Eg.png')
Left_Gray = cv2.cvtColor(Left,cv2.COLOR_BGR2GRAY)

print(Left_Gray.shape)

Right = cv2.imread('Right_Eg.png')
Right_Gray = cv2.cvtColor(Right,cv2.COLOR_BGR2GRAY)
Right_Gray = cv2.resize(Right_Gray,(363,273))
print(Right_Gray.shape)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

disparity = stereo.compute(Left_Gray,Right_Gray)
plt.imshow(disparity,'gray')
plt.show()