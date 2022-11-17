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
        # self.display.geometry('600x630')
        self.display.resizable(width=0, height=0)
        self.display.columnconfigure(4, minsize=30)
        self.display.configure(borderwidth=0)

        # buttons and more

        self.button_upload_photo = Button(self.display, text='Upload', command=self.open_file)
        self.button_upload_photo.grid(row=3, columnspan=4)
        
        self.button_rotate_left = Button(self.display, text='Rotate left', command=self.rotate_left)
        self.button_rotate_left.grid(row=1, column=2)

        self.button_rotate_right = Button(self.display, text='Rotate right', command=self.rotate_right)
        self.button_rotate_right.grid(row=1, column=3)
        
        self.text_bright = Label(self.display, text="Brightness:", font=("Arial 10 bold"))
        self.text_bright.grid(row=0, column=0)

        self.v2 = IntVar()
        self.v1 = IntVar()

        self.scale2 = ttk.Scale(self.display, from_=0, to=20, variable=self.v2,
                   orient=HORIZONTAL, command=self.brightness)
        
        self.scale_blur = ttk.Scale(self.display, from_=0, to=20, variable=self.v1, orient=HORIZONTAL, command=self.blur)
        self.text_blur = Label(self.display, text='Blur:', font=('Arial 10 bold'))
        self.text_blur.grid(row=0, column=2)
        
        self.scale_blur.grid(row=0, column=3)
        self.scale2.grid(row=0, column=1)

        self.canvas = Canvas(self.display, width=600, height=530, highlightthickness = 0)
        self.canvas.grid(row=2, columnspan=4)
        self.current_rotation = 0
        self.direction_rotation = None
        self.image = None
        self.img_path = None

        # permanent operation of the window

        self.display.mainloop()

# functions for buttons

    def open_file(self):

        self.img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        self.image = Image.open(self.img_path)
        self.image.thumbnail((600, 600))
        photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(300, 250, image=photo_image)
        self.canvas.image = photo_image

    def rotate_image(self):
        if not self.direction_rotation:
            return
        self.image.thumbnail((600, 600))
        if self.direction_rotation == 'Left':
            self.current_rotation += 10
            self.image = self.image.rotate(self.current_rotation)
        elif self.direction_rotation == 'Right':
            self.current_rotation -= 10
            self.image = self.image.rotate(self.current_rotation)
        photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(300, 210, image=photo_image)
        self.canvas.image = photo_image


    def rotate_left(self):
        self.direction_rotation = 'Left'
        self.rotate_image()

    def rotate_right(self):
        self.direction_rotation = 'Right'
        self.rotate_image()

    def brightness(self, event):
        for m in range(0, self.v2.get()+1):
            self.image.thumbnail((600, 600))
            imgg = ImageEnhance.Brightness(self.image)
            self.image = imgg.enhance(m)
            photo_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(300, 210, image=photo_image)
            self.canvas.image = photo_image
    
    def blur(self, event):
        for m in range(0, self.v1.get()+1):
            self.image.thumbnail((600, 600))
            imgg = self.image.filter(ImageFilter.BoxBlur(m))
            photo_image = ImageTk.PhotoImage(imgg)
            self.canvas.create_image(300, 210, image=photo_image)
            self.canvas.image = photo_image


    

    # functions

window = Window()