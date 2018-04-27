from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from lat_lon import SatMap
import tkinter.simpledialog
def paint(event, sat_map):
    FillColor = "#FF0000"
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    w.create_oval(x1, y1, x2, y2, fill=FillColor)
    x = event.x
    y = event.y
    coordlist = []
    coordlist.append(x)
    coordlist.append(y)
    utm = sat_map.get_utm(x,y)
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, list(utm))
    mainloop()

    return coordlist
#setting up window
root = Tk()
root.title("Draw Some Points!")


w = Canvas(root, width=1440, height=1080, cursor="target")
w.pack(expand=YES, fill=BOTH)

File = askopenfilename(parent=root, initialdir="./", title='Select an image')
original = Image.open(File)
#original = original.thumbnail((1440,1080), Image.ANTIALIAS)
wpercent = (1080/float(original.size[1]))
hsize = int((float(original.size[0])*float(wpercent)))
original = original.resize((hsize,1080), Image.ANTIALIAS)
#image.thumbnail(size, Image.ANTIALIAS)
img =ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")
#w.config(font=("Ariel", 18, 'bold'))
parentDir = str(File)
parentDir = parentDir.rsplit('/', 1)[0]
sat_image = SatMap(parentDir  +'/')

w.bind("<Button-1>", lambda event: paint(event, sat_image))

# find path and subtract image name to get parent direcrtory.  make variable name.
    # label1 = Label(w, text='x"\n"y', bd=1, relief="solid", font="Times 32", width=15, height=4, anchor=SW)


root.mainloop()
