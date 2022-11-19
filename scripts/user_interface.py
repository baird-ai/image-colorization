from tkinter import *
from tkinter import filedialog
from tkinter .colorchooser import askcolor
from tkinter import ttk
from tkinter.messagebox import showinfo
import cv2 as cv
import os
import time
import matplotlib.pyplot as plt


from PIL import Image, ImageTk
import PIL 
from main import run_model


# Creating the use interface, giving it dimensions, and and icon 
root = Tk()
root.geometry("800x500")
root.configure(bg="#f2f3f5")
root.title("bAIrd image colorization")
root.iconbitmap('GUI/images.ico')
root.resizable(False,False)
# Adding a text label at the top  of the

title = Label(text="تخيل أن الكون لا طعم له أو لون",justify=RIGHT,font=("Courier", 20))
title.grid(row=1,column=1,pady=20)


def UploadFile():
    ''' 
    A function that uploads a grey image that the user chooses from their storage and saves it in the
    grey images folder(directory) as greyimg.jpg
    '''
    curr_directory = os.getcwd()
    file_path = filedialog.askopenfilename(initialdir=curr_directory, title="Select Image", filetypes=[('JPG Files', '*.jpg'),('jpg Files', '*.jpg')])
    img = Image.open(file_path) 
    save_path = "greyimgs/"
    file_name = "greyimg.jpg"
    complete_name = os.path.join(save_path, file_name)
    img.save(complete_name)
    path_text = Label(root,text=file_path)
    path_text.grid(row=2,column=1, padx=10,pady=10,columnspan=4,sticky=W)


    
    if file_path is not None:
        pass
    root.update()

    
my_img2 =Image.open("GUI/Logo.png")
# Giving a default size to the image on the GUI
resized_img = my_img2.resize((401,189),Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(resized_img)
my_l2 = Label(image=my_img3)
my_l2.grid(row=0,column=1,padx=40,columnspan=4)

# color_button = Button(root,text= ("Color it!"), command= run_model)
# color_button.grid(row=1, column=2, columnspan=4)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=400

)
pb.grid(column=1, row=3, columnspan=2, padx=10, pady=20,sticky=W)


# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"

# value_label = ttk.Label(root, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)


def progress():
    
    while pb['value'] < 100:
        pb['value'] += 1
        time.sleep(0.00625)
        # value_label['text'] = update_progress_label()
        root.update()
   
    showinfo(message='Your image is ready!')
    run_model()
    pb['value'] = 0

start_button = ttk.Button(
    root,
    text='Color it',
    command=progress
)
start_button.grid(column=0, row=3, padx=25, pady=10, sticky=W)
root.update()

# Adding the upload button 
upload_button = ttk.Button(root, text=("Upload File"),command=UploadFile)
upload_button.grid(row=2, column=0, padx=25, pady=10,sticky=W)
root.update()

# Giving the upload button the path to save the uploaded photo to 




def savefile():
    root.update()
    my_img = cv.imread('coloredimgs/coloredimg.jpg')

    edge = Image.fromarray(my_img)

    tk_edge = ImageTk.PhotoImage(edge)
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    print (filename)
    if not filename:
        return
    edge.save(filename)

def makeitgrey():
    
    while pb2['value'] < 100:
        pb2['value'] += 1
        time.sleep(0.00625)
        # value_label['text'] = update_progress_label()
        root.update()
   
    showinfo(message='Your image is ready!')
    my_image =cv.imread('coloredimgs/coloredimg.jpg',0)
    final_img = cv.imwrite('coloredimgs/coloredimg.jpg',my_image)
    my_greyimg = cv.imread("coloredimgs/coloredimg.jpg")
    plt.imshow(my_greyimg)
    plt.axis('off')
    plt.show()

    pb2['value'] = 0

pb2 = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=400

)
pb2.grid(column=1, row=4, columnspan=2, padx=10, pady=20,sticky=W)


ttk.Button(root,text="Download image",command=savefile).grid(row=5, column=0, padx=25, pady=10,sticky=W)
# filedialog.SaveAs()
ttk.Button(root,text="Make it grey",command=makeitgrey).grid(row=4,column=0, padx=25, pady=10,sticky=W)

root.mainloop()