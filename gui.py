
#! Importing Modules
from tkinter import *
import tkinter as tk
from PIL import Image 

#! Basic Configurations
gui = Tk()
gui.title('Image Steganography')
gui.geometry('500x700')
gui.configure(bg = 'black')

#! Taking Image 
f1 = Frame(gui)
e1_value = StringVar()
Label(f1, text = 'Enter Image Path ').pack(side = LEFT, padx = 40)
e1 = Entry(f1, textvariable = e1_value, font = '10')
e1.pack(side = BOTTOM)
f1.pack(side = TOP, pady = 10)

#! Encoding Image
f2 = Frame(gui)
b1 = Button(f2, text = 'Encode', command = '').pack(side = LEFT, ipadx = 30)
b2 = Button(f2, text = 'Decode', command = '').pack(side = RIGHT,ipadx = 30)
f2.pack(padx = 40)

gui.mainloop()