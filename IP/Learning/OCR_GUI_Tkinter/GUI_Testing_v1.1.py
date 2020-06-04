from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text

from Backend_v1 import mouse,warp_function,Get_Image,blur_function,ocr_function,save_img

import cv2
import numpy as np

# Global Variables
og_img = np.zeros((), np.uint8)

text = ''

# GUI Main loop
root = tk.Tk()

canvas = tk.Canvas(root,height=700,width = 700,bg="grey")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.6,relheight=0.9,relx=0.2,rely=0.05)

# Button Click Definitions
def open_btn_clicked():
    filename= filedialog.askopenfilename(initialdir="/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning",title = "Select Image",filetypes=(("images","*.jpg"),("all files","*.*")))
    print(filename)
    filename = filename.strip("/Users/anishpawar/Robocon/Robocon_Anish/Matlab_IP/IP/Learning/")
    filename = filename + "pg"
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
    label = tk.Label(frame,text=text,bg='gray')
    label.place(relwidth=0.8,relheight=0.3,relx=0.1,rely=0.1)

def save_img_btn_clicked():
    save_img()


# Buttons
open_btn = tk.Button(canvas,text="Open Image",padx=10,pady=10,fg="black",command=open_btn_clicked)
open_btn.place(relx=0.025,rely=0.05)


blur_btn = tk.Button(canvas,text="Blur Image",padx=14,pady=10,fg="red",command=blur_btn_clicked)
blur_btn.place(relx=0.025,rely=0.2)

Dummy_btn = tk.Button(canvas,text="Dummy",padx=14,pady=10,fg="red")
Dummy_btn.place(relx=0.025,rely=0.375)

mcrop_btn = tk.Button(canvas,text="Manual Crop",padx=10,pady=10,bg="#263D42",fg="red",command=mcrop_btn_clicked)
mcrop_btn.place(relx=0.025,rely=0.5)

ocr_btn = tk.Button(canvas,text="OCR",padx=20,pady=10,bg="#263D42",fg="red",command=ocr_btn_clicked)
ocr_btn.place(relx=0.85,rely=0.05)

show_txt_btn = tk.Button(canvas,text="Show Text",padx=3,pady=10,bg="#263D42",fg="red",command=show_txt_btn_clicked)
show_txt_btn.place(relx=0.85,rely=0.2)

save_img_btn = tk.Button(canvas,text="Save Image",padx=3,pady=10,bg="#263D42",fg="green",command=save_img_btn_clicked)
save_img_btn.place(relx=0.85,rely=0.375)

show_btn = tk.Button(canvas,text="Show Original",padx=10,pady=10,bg="#263D42",fg="red",command=show_btn_clicked)
show_btn.place(relx=0.025,rely=0.895)


destroy_btn = tk.Button(canvas,text="Close \n Windows",padx=5,pady=10,bg="#263D42",fg="red",command=destroy_btn_clicked)
destroy_btn.place(relx=0.85,rely=0.87)


root.mainloop()



