# import numpy as np
# import matplotlib.pyplot as plt
# apparent = []
# actual = np.array([])
# # for i in range(-10000,1000):
# #     x.append(i/100)
# #     y.append(i/100)

# # plt.plot(x,y)
# # plt.xscale("log")
# # plt.show()

# for i in range(0,1000):
#     apparent.append(i)

# j= 5
# while j > 0 :
#     j -= 1/200
#     np.append(actual,j)

# np.reshape(actual,(1000))
# plt.plot(apparent,actual)
# plt.xscale("log")
# plt.show()

import cv2
frames = []

cap = cv2.VideoCapture(0)

while True:
    x , frame = cap.read()
    frames.append(frame)
    cv2.imshow('Video Capture', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print(len(frames))

def nothing(arg): pass
cv2.namedWindow('Video Playback')
cv2.createTrackbar('Frame Number', 'Video Playback', 0,len(frames), nothing)

while True:
    frame_number = cv2.getTrackbarPos('Frame Number', 'Video Playback')
    print(frame_number)
    try:
        img = frames[frame_number]
    except :
        print('Frames Completed')
    cv2.imshow('Video Playback', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()