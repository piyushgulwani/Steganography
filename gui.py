from tkinter import *
import tkinter.messagebox as msg
from tkinter import filedialog
from PIL import Image

#! Base Code
def genData(data):
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        pix = [value for value in imdata.__next__()[:3] +
            imdata.__next__()[:3] +   imdata.__next__()[:3]]

        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


def encode():
    if e1_value.get() == None or e1_value.get() == '' : 
        msg.showerror('Error', 'Image File Not Provided ')

    elif e2_value.get() == None or e2_value.get() == '' : 
        msg.showerror('Error', 'Encoding Message Not Provided')

    elif e3_value.get() == None or e3_value.get() == '' : 
        msg.showerror('Error ', 'New Image Not Provided')

    else : 

        img = e1_value.get()
        image = Image.open(img, 'r')

        data = e2_value.get()

        newimg = image.copy()
        encode_enc(newimg, data)

        new_img_name = e3_value.get()
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
        msg.showinfo('Success', 'Message Encoded')


def decode():

    if e1_value.get() == None or e1_value.get() == '' : 
        msg.showerror('Error', 'Image Not Provided !!')

    else :
        img = e1_value.get()
        image = Image.open(img, 'r')

        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
            imgdata.__next__()[:3] + imgdata.__next__()[:3]]

            binstr = ''

            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                # return data
                e4_value.set(data)
                gui.update()
                msg.showinfo('Success', 'Message Decoded ')
                break


#! Gui
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
    gui.filename =  filedialog.askopenfilename(initialdir = "/",
title = "Select file",filetypes = (("jpeg files", "*.jpg"), ("png files", "*.png ")))
    filechoosen = gui.filename
    e1_value.set(filechoosen)
    gui.update()

f1 = Frame(gui)
l1 = Label(f1,text = 'Enter Image Path >> ')
l1.grid(row = 0,column = 0,ipadx = 25)

e1_value = StringVar()
e1 = Entry(f1, textvariable = e1_value)
e1.grid(row = 0, column = 1, ipadx = 30, padx = 10)

b1 = Button(f1, text = '📁', command = openfile, activebackground = 'cyan')
b1.grid(row = 0, column = 2, ipadx = 10)
f1.pack(side = TOP)

#! Frame 3 Components 
f3 = Frame(gui)

l2 = Label(f3, text = 'Enter Message To be Encoded >>')
l2.pack(side = LEFT, ipadx = 20)

e2_value = StringVar()
e2 = Entry(f3, textvariable = e2_value)
e2.pack(ipadx = 35)

f3.pack(pady = 20)

#! Frame 4 Components 
f4 = Frame(gui)

l3 = Label(f4, text = 'Enter new image name  >>')
l3.pack(ipadx = 35, side = LEFT)

e3_value = StringVar()
e3 = Entry(f4, textvariable = e3_value)
e3.pack(ipadx = 35)

f4.pack()

#! Frame 5 Components 
f5 = Frame(gui)

l4 = Label(f5, text = 'Decoded Message  >>')
l4.pack(ipadx = 35, side = LEFT)

e4_value = StringVar()
e4 = Entry(f5, textvariable = e4_value)
e4.pack(ipadx = 40)

f5.pack(pady = 20)

#! Frame 2 Components 
f2 = Frame(gui)
b2 = Button(f2, text = 'Encode', command = encode)
b2.pack(ipadx = 30, side = LEFT)

b3 = Button(f2, text = 'Decode', command = decode)
b3.pack(ipadx = 30, side = RIGHT)

f2.pack(pady = 30)

gui.mainloop()