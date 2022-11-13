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

        # buttons and more

        self.button_upload_photo = Button(self.display, text='Upload', command=self.open_file)
        self.button_upload_photo.grid(row=2, columnspan=4)
        
        self.button_rotate_left = Button(self.display, text='Rotate left', command=self.rotate_left)
        self.button_rotate_left.grid(row=0, column=2)

        self.button_rotate_right = Button(self.display, text='Rotate right', command=self.rotate_right)
        self.button_rotate_right.grid(row=0, column=3)
        
        self.text_bright = Label(self.display, text="Brightness:", font=("ariel 10 bold"))
        self.text_bright.grid(row=0, column=0)

        self.v2 = IntVar()

        self.scale2 = ttk.Scale(self.display, from_=0, to=20, variable=self.v2,
                   orient=HORIZONTAL, command=self.brightness)
        
        self.scale2.grid(row=0, column=1)

        self.canvas = Canvas(self.display, width=600, height=530, highlightthickness = 0)
        self.canvas.grid(row=1, columnspan=4)

        # permanent operation of the window

        self.display.mainloop()

# functions for buttons

    def open_file(self):
        global img_path, img
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((600, 600))
        img1 = ImageTk.PhotoImage(img)
        self.canvas.create_image(300, 250, image=img1)
        self.canvas.image = img1

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def brightness(self):
        global img_path, img2, img3
        for m in range(0, self.v2.get()+1):
            img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        self.canvas.create_image(300, 210, image=img3)
        self.canvas.image = img3


    

    # functions

window = Window()