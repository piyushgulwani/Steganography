from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image

gui = Tk()
gui.title('Image Steganography')
gui.geometry('530x360')
gui.configure(bg = 'black')

label1 = Label(gui, text = '', bg = 'cyan')
label1.pack(fill = X, side = TOP)
label2 = Label(gui, text = '', bg = 'cyan')
label2.pack(fill = Y, side = LEFT)
label3 = Label(gui, text = '', bg = 'cyan')
label3.pack(fill = Y, side = RIGHT)
label4 = Label(gui, text = '', bg = 'cyan')
label4.pack(fill = X, side = BOTTOM)

gui.mainloop()