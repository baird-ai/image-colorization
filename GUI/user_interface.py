from tkinter import *
from tkinter import filedialog
from tkinter .colorchooser import askcolor
import cv2 as cv
import os

from PIL import Image, ImageTk, ImageGrab
import PIL 

root = Tk()
root.geometry("660x500")
root.configure(bg="#f2f3f5")
root.title("colorize your image")
root.iconbitmap('3162558.ico')
root.resizable(False,False)

title = Label(text="تخيل ان الكون لا طعم له او لون",font=("Courier", 27))
title.grid(row=0,column=2,pady=20)

def UploadFile():
   curr_directory = os.getcwd()
   file_path = filedialog.askopenfilename(initialdir=curr_directory, title="Select Image", filetypes=[('JPG Files', '*.jpg'),('jpg Files', '*.jpg')])
   img = Image.open(file_path) 
   save_path = "greyimgs/"
   file_name = "greyimg.jpg"
   complete_name = os.path.join(save_path, file_name)
   img.save(complete_name)
   path_text = Label(root,text=file_path,bg="#B2B2B2")
   path_text.grid(row=2,column=1,pady=10,columnspan=4)
   
   if file_path is not None:
        pass

upload_button = Button(root, text=("Upload File"),command=UploadFile)
upload_button.grid(row=1, column=1,columnspan=4)


my_img2 =Image.open("coloredimgs/coloredimg.jpg")

resized_img = my_img2.resize((350,200),Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(resized_img)
my_l2 = Label(image=my_img3)
my_l2.grid(row=3,padx=20,pady=20,columnspan=4)


my_img = cv.imread('coloredimgs/coloredimg.jpg')

edge = Image.fromarray(my_img)

tk_edge = ImageTk.PhotoImage(edge)
def savefile():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    print (filename)
    if not filename:
        return
    edge.save(filename)

Button(root,text="Download image",command=savefile).grid(row=4, column=1,columnspan=4)
filedialog.SaveAs()


root.mainloop()