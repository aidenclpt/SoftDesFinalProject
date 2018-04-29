from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from lat_lon import SatMap, GeoSegments, GeoPoint, GeoPoly
import tkinter.simpledialog

class Viewer:
    def __init__(self):
        self.points = None
        self.lines = None
        self.polygon = None

def draw_point(event, sat_map, view):
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

def draw_segments(event, sat_map, segments, view):
    FillColor = "#FF0000"
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    w.create_oval(x1, y1, x2, y2, fill=FillColor)

    x = event.x
    y = event.y

    point = GeoPoint(sat_map, x, y)
    segments.point_list.append(point)
    segments.get_length()
    if len(segments.point_list) >=2:
        view.lines = w.create_line(*segments.kinter_coords, fill = 'red', width = '5')
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, segments.length)
    mainloop()

def draw_poly(event, sat_map, polygon):
    FillColor = "#FF0000"
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    w.create_oval(x1, y1, x2, y2, fill=FillColor)

    x = event.x
    y = event.y

    point = GeoPoint(sat_map, x, y)
    polygon.point_list.append(point)
    area = polygon.get_area()
    if len(polygon.point_list) >=3:
        view.polygon = w.create_polygon(polygon.kinter_coords, outline = 'red', fill = 'red', width = 2)
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, area)
    mainloop()


#setting up window
root = Tk()
root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])


w = Canvas(root, width=1440, height=1080, cursor="target")
current_view = Viewer()
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


w.bind("<Button-2>", lambda event: draw_point(event, sat_image))
w.bind("<B1-Motion>", lambda event: draw_segments(event, sat_image, current_segments, current_view))

# w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_poly))

# find path and subtract image name to get parent direcrtory.  make variable name.
    # label1 = Label(w, text='x"\n"y', bd=1, relief="solid", font="Times 32", width=15, height=4, anchor=SW)


root.mainloop()
