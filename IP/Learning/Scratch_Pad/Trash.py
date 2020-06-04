import cv2
import time

cap = cv2.VideoCapture(0)

# start_time = time.gmtime()
counter = 0

# # print(start_time.tm_sec)
# while True:
#     _,frame = cap.read()
#     new_time = time.gmtime()
#     flipped = cv2.flip(frame,-1)
#     counter +=1
#     diff = new_time.tm_sec-start_time.tm_sec
#     # print(diff)

#     if diff %6 == 0:
#         cv2.imshow('Frame',flipped)
#     else:
#         cv2.imshow('Frame',frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# print(counter/diff)

while True:
    _,frame = cap.read()
    
    flipped = cv2.flip(frame,-1)
    counter +=1
    
    if counter == 60:
        
        cv2.imshow('Frame',flipped)
        
    else:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break