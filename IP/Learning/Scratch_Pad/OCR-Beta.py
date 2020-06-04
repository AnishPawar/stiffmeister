import cv2
import numpy as np
import pytesseract
from pytesseract import Output
img = cv2.imread('invoice.png')


kernal = np.ones((1,1),np.uint8)

gray= cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

gaussian = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,3)
blur = cv2.GaussianBlur(gaussian,(11,11),0)

canny = cv2.Canny(gaussian,10,10)
# dilation = cv2.dilate(canny,kernal,iterations=1)
denoised = cv2.fastNlMeansDenoising(gaussian,None,10,7,21)
# opening = cv2.morphologyEx(canny,cv2.MORPH_OPEN,kernal)

contours,x = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



for areas in contours:
    max_index = np.argmax(areas)
    print(max_index)
    max=contours[max_index]
    cv2.drawContours(img, max, -1,(0,0,255),3) 

text = pytesseract.image_to_string(gaussian,lang='eng')
# test=pytesseract.image_to_pdf_or_hocr
d = pytesseract.image_to_data(gaussian,output_type=Output.DICT)

# Text Bounding Boxes
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 70:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(text)

cv2.imshow('image',img)
cv2.imshow('canny',gaussian)
cv2.waitKey(0)
