
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
Label(f1, text = 'Enter Image Path ➡').pack(side = LEFT)
e1 = Entry(f1, textvariable = e1_value, font = '10')
e1.pack()
f1.pack(side = TOP, pady = 30)

gui.mainloop()