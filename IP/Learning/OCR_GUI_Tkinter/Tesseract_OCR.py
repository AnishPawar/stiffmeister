import pytesseract
from pytesseract import Output
import cv2
base = cv2.imread('WOW.jpg')

text = pytesseract.image_to_string(base,lang='eng')
    
data = pytesseract.image_to_data(base,output_type=Output.DICT)

n_boxes = len(data['text'])

for i in range(n_boxes):
    if int(data['conf'][i]) > 60:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        ocr_img = cv2.rectangle(base, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('image',base)
# print(text)
print(data['text'])
cv2.waitKey(0)
