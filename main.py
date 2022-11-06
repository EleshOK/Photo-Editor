# imports

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# window

class Window():
    def __init__(self):
        display = Tk()
        display.title('Photo editor')
        display.geometry('600x600')
        display.resizable(0, 0)

        # buttons

        button_upload_photo = Button(display, text='Upload')
        button_upload_photo.place(x=250, y=550)
        
        button_rotate_left = Button(display, text='Rotate left', command=rotate_left)
        button_rotate_left.place(x=550, y=20)

        button_rotate_right = Button(display, text='Rotate right', command=rotate_right)
        button_rotate_right.place(x=500, y=20)
        
        button_brightness = Button(display, text='Brightness', command=brightness)
        button_brightness.place(x=20, y=20)
        self.canvas = Canvas(display, canvas)
    
        # permanent operation of the window

        display.mainloop()

    # functions

    def open_file(self):
        global img_path, img
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img1 = ImageTk.PhotoImage(img)
        Window.self.canvas.create_image(300, 210, image=img1)
        Window.self.canvas.image = img1

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def brightness(self):
        pass
