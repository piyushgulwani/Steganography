
#! Importing Modules
from tkinter import *
import tkinter.messagebox as tsmg
from PIL import Image 


#! Generating Data for Encoding/ Decoding
def generate_data(data):
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))

    return newd

#! Modifying Pixel to Encode or Decode Message
def modify_pixel(pix, data):
    datalist = generate_data(data)
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

    for pixel in modify_pixel(newimg.getdata(), data):

        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


def encode():

    try :
        img = e1_value.get()
        image = Image.open(img, 'r')

        data = e2_value.get()
        if (len(data) == 0):
            raise ValueError('Data is empty')

        newimg = image.copy()
        encode_enc(newimg, data)

        new_img_name = input("Enter the name of new image :\t ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

        tsmg.showinfo('Done', message= 'Data Encrypted')

    except Exception as e : 
        tsmg.showerror('Error', message='Encryption Failed')


def decode():
    try :
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
                return data

    except Exception as e: 
        tsmg.showerror('Error', message='Decryption Error')

#! Basic Configurations
gui = Tk()
gui.title('Image Steganography')
gui.geometry('500x300')
gui.configure(bg = 'black')

#! Taking Image 
f1 = Frame(gui)
e1_value = StringVar()
Label(f1, text = 'Enter Image Path ').pack(side = LEFT, padx = 40)
e1 = Entry(f1, textvariable = e1_value, font = '10')
e1.pack(side = BOTTOM)
f1.pack(side = TOP, pady = 10)

#! Taking Data to be encoded 
f2 = Frame(gui)
Label(f2, text = 'Enter Message to be encoded ').pack(side = LEFT)
e2_value = StringVar()
e2 = Entry(f2, textvariable = e2_value).pack(ipadx = 40)
f2.pack(pady = 20)

#! Encoding Image
f3 = Frame(gui)
b1 = Button(f3, text = 'Encode', command = encode).pack(side = LEFT, ipadx = 30)
b2 = Button(f3, text = 'Decode', command = decode).pack(side = RIGHT,ipadx = 30)
f3.pack(padx = 40)

def history() : 
    pass

gui.mainloop()