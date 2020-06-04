import cv2
import numpy as np

import pytesseract
from pytesseract import Output

counter = 0
# pts = []
final_coor = []

img = np.zeros((), np.uint8)

scanned = np.zeros((), np.uint8)

flag = 0 

def Get_Image(image):
    global img
    img = image
    pass

def blur_function():
    blur_base = img 
    blur = cv2.GaussianBlur(blur_base,(25,25),0)
    cv2.imshow('image',blur)
    # cv2.waitKey(0)

def ocr_function():
    if flag == 0:
        base = img
    else :
        base = scanned

    text = pytesseract.image_to_string(base,lang='eng')
    # test=pytesseract.image_to_pdf_or_hocr
    d = pytesseract.image_to_data(base,output_type=Output.DICT)

    # Text Bounding Boxes
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 50:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            ocr_img = cv2.rectangle(base, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # print(text)        
    # return(1,text)            
    cv2.imshow('image',base)
    return(text)

def mouse(event,x,y,z,w):
    
    global counter,final_coor 
    marked = img
    if event == cv2.EVENT_LBUTTONDOWN:
        counter = counter+1

        if counter == 1:
            pos1=(y,x)
            pos1_flip = (x,y)
            
            final_coor.append(pos1_flip)
            
            cv2.circle(marked,pos1_flip,60,(0,255,0),-1)
            cv2.imshow('image',marked)

        if counter == 2:
            pos2=(y,x)
            pos2_flip = (x,y)
            
            final_coor.append(pos2_flip)
            
            cv2.circle(marked,pos2_flip,60,(0,255,0),-1)
            cv2.imshow('image',marked)

        if counter == 3:
            pos3=(y,x)
            pos3_flip = (x,y)
            
            final_coor.append(pos3_flip)

            cv2.circle(marked,pos3_flip,60,(0,255,0),-1)
            cv2.imshow('image',marked)

        if counter == 4:
            pos4=(y,x)      
            pos4_flip = (x,y)
            
            final_coor.append(pos4_flip)
            
            cv2.circle(marked,pos4_flip,60,(0,255,0),-1)
            print(final_coor)
            warp_function(final_coor,img)

            
def warp_function(coor,img):
    pts1 = np.float32(coor)
    pts2 = np.float32([(0, 0), (500, 0), (0, 600), (500, 600)])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    # global warped
    warped = cv2.warpPerspective(img, matrix, (500,600))            
    cv2.imshow("image",warped)
    cv2.imwrite('Warped.jpg',warped)
    scan(warped)
    global flag
    flag = 1


def scan(crop):
    global scanned
    scanned = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3,3))
    scanned = cv2.adaptiveThreshold(scanned,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,45,11)
    # closing = cv2.morphologyEx(scanned, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('image',scanned)
    save_img(scanned)
    # cv2.imshow('closing',closing)

def save_img(final):
    cv2.imwrite('Scanned.jpg',final)
    