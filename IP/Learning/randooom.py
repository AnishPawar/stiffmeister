import cv2
import numpy as np

img = cv2.imread('IMG_3879.JPG')

aspect_ratio = img.shape[1]/img.shape[0]

height = int(1500/aspect_ratio)

# print()

new_img = cv2.resize(img, (1500, height))

print(aspect_ratio)

# pre processing

blur = cv2.GaussianBlur(new_img,(5,5),0)

gray  = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

th4 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,3)

closing = cv2.morphologyEx(th4,cv2.MORPH_CLOSE,np.ones((11,11)),iterations= 1)

canny = cv2.Canny(closing,0,200,3)

# Finding area of image
img_area = new_img.shape[0]*new_img.shape[1]

contours,_ = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# To prevent from detecting the whole page as ROI
for x in contours:
    if cv2.contourArea(x) > 0.9*img_area:
        contours.remove(x)

areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
max=contours[max_index]

# approximating polygon
perimeter = cv2.arcLength(max,True) 
ROI = cv2.approxPolyDP(max,0.02*perimeter,True)


if len(ROI)==4:
    reshaped = ROI.reshape(4,2)

    summation = [(x+y) for x,y in reshaped]
    difference = [(x-y) for x,y in reshaped]

    br_index = np.argmax(summation)
    tl_index = np.argmin(summation)
    tr_index = np.argmax(difference)
    bl_index = np.argmin(difference)

    tl = reshaped[tl_index]
    tr = reshaped[tr_index]
    bl = reshaped[bl_index]
    br = reshaped[br_index]

    # Warping
    pts1 = np.float32([tl,tr,bl,br])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    warped = cv2.warpPerspective(new_img, matrix, (500,600))            
    
    cv2.imshow("image",warped)


cv2.drawContours(new_img,[ROI],-1,(0,255,0),3)

print(len(ROI))

cv2.imshow('img',new_img)
cv2.waitKey(0)
