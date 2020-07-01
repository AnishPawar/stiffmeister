from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text

from Backend_v2 import mouse,warp_function,Get_Image,blur_function,ocr_function,save_img,auto_crop

import cv2
import numpy as np

# Global Variables
og_img = np.zeros((), np.uint8)

text = ''

# GUI Main loop
root = tk.Tk()

canvas = tk.Canvas(root,height=700,width = 700,bg="#6BF2BF")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.6,relheight=0.9,relx=0.2,rely=0.05)

text_box = tk.Frame(frame,bg="#FDFFD6")
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

# Button Click Definitions
def open_btn_clicked():
    filename= filedialog.askopenfilename(initialdir="/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning",title = "Select Image",filetypes=(("images","*.jpg"),("all files","*.*")))
    print(filename)
    
    global og_img
    og_img = cv2.imread(filename)

    cv2.imshow('image',og_img)
    Get_Image(og_img)
    
def blur_btn_clicked():
    blur_function()

def show_btn_clicked():
    cv2.imshow('image',og_img)
    
def ocr_btn_clicked():
    global text
    text = ocr_function()
    print("Working \n")
    print(text)

def mcrop_btn_clicked():
    mcrop = og_img
    Get_Image(mcrop)
    cv2.imshow('image',mcrop)
    cv2.setMouseCallback('image',mouse)

def destroy_btn_clicked():
    cv2.destroyAllWindows()

def show_txt_btn_clicked():
    
    scrollbar = Scrollbar(text_box)
    scrollbar.pack(side=RIGHT, fill=Y)
    ocr = Text(text_box, wrap=WORD, yscrollcommand=scrollbar.set,bg = '#FDFFD6')
    ocr.insert('1.0',text)

    ocr.place(relx=0,rely=0,relheight = 1,relwidth =1)

    scrollbar.config(command=ocr.yview)

def save_img_btn_clicked():
    save_img()

def auto_crop_btn_clicked():
    Get_Image(og_img)
    auto_crop(og_img)

#Labels

label = tk.Label(frame,text='Detected Text',fg= 'blue',bg='white',font =('Arial',22)) 
label.place(relx=0.3,rely=0.1)

# Buttons
open_btn = tk.Button(canvas,text="Open Image",padx=10,pady=10,fg="black",command=open_btn_clicked)
open_btn.place(relx=0.025,rely=0.05)

blur_btn = tk.Button(canvas,text="Blur Image",padx=14,pady=10,fg="black",command=blur_btn_clicked)
blur_btn.place(relx=0.025,rely=0.2)

Dummy_btn = tk.Button(canvas,text="Auto Crop",padx=14,pady=10,fg="black",command = auto_crop_btn_clicked)
Dummy_btn.place(relx=0.025,rely=0.375)

mcrop_btn = tk.Button(canvas,text="Manual Crop",padx=10,pady=10,bg="#263D42",fg="black",command=mcrop_btn_clicked)
mcrop_btn.place(relx=0.025,rely=0.5)

ocr_btn = tk.Button(canvas,text="OCR",padx=20,pady=10,bg="#263D42",fg="black",command=ocr_btn_clicked)
ocr_btn.place(relx=0.85,rely=0.05)

show_txt_btn = tk.Button(canvas,text="Show Text",padx=3,pady=10,bg="#263D42",fg="black",command=show_txt_btn_clicked)
show_txt_btn.place(relx=0.85,rely=0.2)

save_img_btn = tk.Button(canvas,text="Save Image",padx=3,pady=10,bg="#263D42",fg="green",command=save_img_btn_clicked)
save_img_btn.place(relx=0.85,rely=0.375)

show_btn = tk.Button(canvas,text="Show Original",padx=10,pady=10,bg="#263D42",fg="red",command=show_btn_clicked)
show_btn.place(relx=0.025,rely=0.895)

destroy_btn = tk.Button(canvas,text="Close \n Windows",padx=5,pady=10,bg="#263D42",fg="red",command=destroy_btn_clicked)
destroy_btn.place(relx=0.85,rely=0.87)

root.mainloop()