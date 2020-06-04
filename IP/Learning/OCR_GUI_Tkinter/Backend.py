import cv2
import numpy as np


    
# img = cv2.imread('sheet_paper.JPEG')

counter = 0
pts = []
final_coor = []

img = np.zeros((), np.uint8)

warped = np.zeros((), np.uint8)

def Get_Image(image):
    global img
    img = image
    pass


def mouse(event,x,y,z,w):
    
    global counter,pts 
    
    if event == cv2.EVENT_LBUTTONDOWN:
        counter = counter+1

        if counter == 1:
            pos1=(y,x)
            pts.append(pos1)
            # cv2.circle(img,final_coor[0],60,(0,255,0),-1)
        if counter == 2:
            pos2=(y,x)
            pts.append(pos2)
            # cv2.circle(img,final_coor[1],60,(0,255,0),-1)

        if counter == 3:
            pos3=(y,x)
            pts.append(pos3)
            # cv2.circle(img,final_coor[2],60,(0,255,0),-1)

        if counter == 4:
            pos4=(y,x)        
            pts.append(pos4)
            xy_interchange(pts)
            # cv2.circle(img,final_coor[3],60,(0,255,0),-1)


def xy_interchange(pts):
    y,x = zip(*pts) 
    global final_coor
    final_coor = zip(x,y)
    final_coor = list(final_coor)
    print(final_coor)

    pts = np.array([final_coor], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],isClosed=True,color=(255,0,0),thickness=20,lineType=8,shift = 0)
    cv2.imshow('diagram',img)
    cv2.waitKey(0)
    warp_function(final_coor,img)





def warp_function(coor,img):
    pts1 = np.float32(coor)
    pts2 = np.float32([(0, 0), (500, 0), (0, 600), (500, 600)])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    warped = cv2.warpPerspective(img, matrix, (500,600))            
    cv2.imshow("image",warped)
    cv2.waitKey(0)
    return warped

# def polygon(img,input_pts):
    
#     cv2.imshow('img',img)
#     cv2.waitKey(0)



# while True:
#     cv2.imshow("Image",img)
#     if cv2.waitKey(0):
#         break

# print(final_coor)
# print(pts)

# warp_function(final_coor)

# cv2.imshow("Image",warped)