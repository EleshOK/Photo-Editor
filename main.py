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
        self.display = Tk()
        self.display.title('Photo editor')
        self.display.geometry('600x600')
        self.display.resizable(width=0, height=0)
        self.display.columnconfigure(4, minsize=30)
        self.display.configure(borderwidth=0)

        # buttons

        self.button_upload_photo = Button(self.display, text='Upload')
        self.button_upload_photo.grid(row=2, columnspan=4)
        # self.button_upload_photo.place(x=265, y=550)
        
        self.button_rotate_left = Button(self.display, text='Rotate left', command=self.rotate_left)
        self.button_rotate_left.grid(row=0, column=2)
        # self.button_rotate_left.place(x=550, y=20)

        self.button_rotate_right = Button(self.display, text='Rotate right', command=self.rotate_right)
        self.button_rotate_right.grid(row=0, column=3)
        # self.button_rotate_right.place(x=500, y=20)
        
        self.button_brightness = Button(self.display, text='Brightness', command=self.brightness)
        self.button_brightness.grid(row=0, column=0)
        # self.button_brightness.place(x=20, y=20)
        self.canvas = Canvas(self.display, width=600, height=530, bg='red', highlightthickness = 0)
        self.canvas.grid(row=1, columnspan=4)
        # self.canvas.place(y=20, x=0)

        # permanent operation of the window

        self.display.mainloop()

# functions for buttons

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


    

    # functions

window = Window()