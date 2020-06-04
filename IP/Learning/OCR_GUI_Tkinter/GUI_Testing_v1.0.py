from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text

from Backend import mouse,xy_interchange,warp_function,Get_Image

import pytesseract
from pytesseract import Output

import cv2
import numpy as np

og_img = np.zeros((), np.uint8,)

# counter = 0
# pts = []
final_coor = []
# warped = np.zeros((), np.uint8)



def open_btn_clicked():
    filename= filedialog.askopenfilename(initialdir="/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning",title = "Select Image",filetypes=(("images","*.jpg"),("all files","*.*")))
    print(filename)
    filename = filename.strip("/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning/")
    filename = filename + "pg"
    print(filename)
    global og_img
    og_img = cv2.imread(filename)
    # img = og_img
    cv2.imshow('image',og_img)
    

def blur_btn_clicked():
    blur_base = og_img 
    blur = cv2.GaussianBlur(blur_base,(25,25),0)
    cv2.imshow('image',blur)

def show_btn_clicked():
    cv2.imshow('image',og_img)


def ocr_btn_clicked():
    # OCR
    text = pytesseract.image_to_string(og_img,lang='eng')
    # test=pytesseract.image_to_pdf_or_hocr
    d = pytesseract.image_to_data(og_img,output_type=Output.DICT)

    # Text Bounding Boxes
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 70:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            ocr_img = cv2.rectangle(og_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('image',ocr_img)
            print(text)

def mcrop_btn_clicked():
    mcrop = og_img
    Get_Image(mcrop)
    cv2.imshow('image',mcrop)
    cv2.setMouseCallback('image',mouse)


# GUI
root = tk.Tk()

canvas = tk.Canvas(root,height=600,width = 600,bg="orange")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

filename = PhotoImage(file = "/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning/Bill.png")
background_label = Label(frame, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons
open_btn = tk.Button(frame,text="Open Image",padx=20,pady=10,bg="#263D42",fg="red",command=open_btn_clicked)
open_btn.place(relx=0.05,rely=0.05)

blur_btn = tk.Button(frame,text="Blur Image",padx=20,pady=10,bg="#263D42",fg="red",command=blur_btn_clicked)
blur_btn.place(relx=0.4,rely=0.05)

show_btn = tk.Button(frame,text="Show Original Image",padx=10,pady=10,bg="#263D42",fg="red",command=show_btn_clicked)
show_btn.place(relx=0.35,rely=0.8)

ocr_btn = tk.Button(frame,text="OCR",padx=20,pady=10,bg="#263D42",fg="red",command=ocr_btn_clicked)
ocr_btn.place(relx=0.42,rely=0.3)

mcrop_btn = tk.Button(frame,text="Manual Crop",padx=20,pady=10,bg="#263D42",fg="red",command=mcrop_btn_clicked)
mcrop_btn.place(relx=0.7,rely=0.05)
# Text
# r_text = tk.Text(frame, height=2, width=30)
# r_text.place(relx=0.1,rely=0.2)
# r_text.insert(tk.END, "Just a text Widget\nin two lines\n")

root.mainloop()


