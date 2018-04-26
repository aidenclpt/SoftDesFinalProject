from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog

def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    x = event.x
    y = event.y
    coordlist = []
    coordlist.append(x)
    coordlist.append(y)
    return coordlist
root = Tk()
#setting up window
root.title("Draw Some Points!")
w = Canvas(root, width=1080, height=720, cursor="target")
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)
File = askopenfilename(parent=root, initialdir="./", title='Select an image')
original = Image.open(File)
original = original.resize((1080,720))
img =ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")
parentDir = str(File)
parentDir = parentDir.rsplit('/', 1)[0]
# find path and subtract image name to get parent direcrtory.  make variable name.

print(coordlist)


root.mainloop()
