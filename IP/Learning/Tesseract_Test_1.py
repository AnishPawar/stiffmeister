import pytesseract
import cv2
warped = cv2.imread('Warped.jpg')
from pytesseract import Output

text = pytesseract.image_to_string(warped,lang='eng')
    # test=pytesseract.image_to_pdf_or_hocr
d = pytesseract.image_to_data(warped,output_type=Output.DICT)

    # Text Bounding Boxes
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 70:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        ocr_img = cv2.rectangle(warped, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(text)
cv2.imshow('OCR',warped)
cv2.waitKey(0)
