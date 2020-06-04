from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text

import pytesseract
from pytesseract import Output

import cv2
import numpy as np

og_img = np.zeros((), np.uint8,)

window = Tk()

window.title("Document Scanner")

window.geometry('400x400')


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
    blur = cv2.GaussianBlur(blur_base,(11,11),0)
    cv2.imshow('image',blur)

def show_btn_clicked():
    cv2.imshow('image',og_img)


open_btn = Button(window, text="Open Image",bg="blue",fg="red", command=open_btn_clicked)

open_btn.grid(column=1, row=0)

blur_btn = Button(window, text = "Blur", command= blur_btn_clicked)
blur_btn.grid(column=20, row=0)

show_btn = Button(window, text = "Show Original Image", command= show_btn_clicked)
show_btn.grid(column=10, row=0)


window.mainloop()