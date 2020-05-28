import cv2
img = cv2.imread('bill.png')
#blocksize =11
#constant = 2
th1 = cv2.threshold(img,10,255 , cv2.THRESH_BINARY)
#cv2.THRESH_BINARY, block_size,constant
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#th2, image = cv2.threshold(grayimg,12,255 , cv2.THRESH_BINARY)
#print(th2)
th3 = cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51, 3)

#retval, th2 = cv2.adaptiveThreshold(grayimg,255 , cv2.ADAPTIVE_THRESH_BINARY_C)
#cv2.imshow('IMage', gaussian)
print(grayimg, th3)
cv2.imshow('IMage', th3)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# while True:
#     x, frame =cap.read()
#     #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
#     #cv2.imshow('frame', grayframe) 
#     th4 = cv2.adaptiveThreshold(grayframe,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51, 3)
#     cv2.imshow('frame ',th4 )

#     if cv2.waitKey(1) & 0xFF == ord('q'): #exit 
#         break

# cap.release()