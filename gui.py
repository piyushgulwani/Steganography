from tkinter import *
import tkinter.messagebox as msg
from tkinter import filedialog
from PIL import Image

gui = Tk()
gui.title('Image Steganography')
gui.geometry('530x360')
gui.configure(bg = 'black')

#! For Attraction 😉
label1 = Label(gui, text = '', bg = 'cyan')
label1.pack(fill = X, side = TOP)
label2 = Label(gui, text = '', bg = 'cyan')
label2.pack(fill = Y, side = LEFT)
label3 = Label(gui, text = '', bg = 'cyan')
label3.pack(fill = Y, side = RIGHT)
label4 = Label(gui, text = '', bg = 'cyan')
label4.pack(fill = X, side = BOTTOM)

#! Frame 1 Components

def openfile() : 
    gui.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg", "*png", '.ico'),("all files","*.*")))
    filechoosen = gui.filename
    e1_value.set(filechoosen)
    gui.update()

f1 = Frame(gui)
l1 = Label(f1,text = 'Enter Image Path >> ')
l1.grid(row = 0,column = 0,ipadx = 25)

e1_value = StringVar()
e1 = Entry(f1, textvariable = e1_value)
e1.grid(row = 0, column = 1, ipadx = 30, padx = 10)

b1 = Button(f1, text = '📁', command = openfile)
b1.grid(row = 0, column = 2, ipadx = 10)
f1.pack(side = TOP)

gui.mainloop()