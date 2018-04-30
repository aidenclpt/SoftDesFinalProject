from tkinter import *
import time
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from lat_lon import SatMap, GeoSegments, GeoPoint, GeoPoly
import tkinter.simpledialog
import geo

Image.MAX_IMAGE_PIXELS = 250000000

class Viewer:
    def __init__(self, text_root):
        self.points = None
        self.lines = None
        self.polygon = None
        self.T = Text(text_root, height=2, width=30)
        self.T.pack(side = RIGHT)


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
    latlong = sat_map.get_lat_lon(x,y)
    geostring = str(latlong[0]) + ', ' + str(latlong[1])
    geo.attraction_info(geo.find_attraction(geostring))

    root = Tk()
    T = Text(root, height=2, width=40)
    T.pack()
    #T.pack(side)
    T.insert(END, list(utm))
    mainloop()
    return coordlist

def draw_segments(event, sat_map, segments, view):
    FillColor = "#FF0000"
    text_root.quit()
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
    view.T.delete('1.0', END)

    view.T.insert(END, segments.length)
    time.sleep(0.1)
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
    view.T = Text(root, height=2, width=40)
    view.T.pack()
    view.T.insert(END, area)
    mainloop()


#setting up window
root = Tk()
#text_root = Tk()





File = askopenfilename(parent=root, initialdir="./", title='Select an image')
original = Image.open(File)
#original = original.thumbnail((1440,1080), Image.ANTIALIAS)
wpercent = (1080/float(original.size[1]))
hsize = int((float(original.size[0])*float(wpercent)))
original = original.resize((hsize,1080), Image.ANTIALIAS)

parentDir = str(File)
parentDir = parentDir.rsplit('/', 1)[0]
sat_image = SatMap(parentDir  +'/')

w = Canvas(root, width = 1080/sat_image.height * sat_image.width, height=1080, cursor="target")
text_root = Tk()
text_root.title("Line Segment Length")
current_view = Viewer(text_root)
w.pack(expand=YES, fill=BOTH)

root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])

#image.thumbnail(size, Image.ANTIALIAS)
img =ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")

#w.config(font=("Ariel", 18, 'bold'))



w.bind("<Button-3>", lambda event: draw_point(event, sat_image, current_view))
w.bind("<B1-Motion>", lambda event: draw_segments(event, sat_image, current_segments, current_view))

# w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_poly))

# find path and subtract image name to get parent direcrtory.  make variable name.
    # label1 = Label(w, text='x"\n"y', bd=1, relief="solid", font="Times 32", width=15, height=4, anchor=SW)
root.mainloop()
