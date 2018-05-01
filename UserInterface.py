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
        self.image = None
        self.x = 0
        self.y = 0
        self.scale = 1
        self.vsize = 1080
        self.hsize = None
        self.tkimage = None

def generate_image(view):

    w.delete(view.tkimage)
    wpercent = (1080/float(view.image.size[1]))
    hsize = int((float(view.image.size[0])*float(wpercent)))

    view.image = view.original.resize((int(view.hsize*view.scale),int(view.vsize*view.scale)), Image.ANTIALIAS)

    img =ImageTk.PhotoImage(view.image)
    print('hi')
    view.tkimage = w.create_image(int(view.x), int(view.y), image=img, anchor="nw")

    
    mainloop()

def zoom(event, sat_map, view, scale):

    view.scale = view.scale * scale
    sat_map.scale = sat_map.scale/scale
    dx = (event.x - view.hsize/2)*(scale-1)
    dy = (event.y - view.vsize/2)*(scale-1)
    view.x = view.x - dx
    view.y = view.y - dy
    print(view.scale)

    generate_image(view)



def zoom_in(event, sat_map, view):
    factor = 1.01

    x = event.x
    y = event.y

    time.sleep(0.1)


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

def draw_poly(event, sat_map, view, polygon):
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
text_root = Tk()

File = askopenfilename(parent=root, initialdir="./", title='Select an image')
original = Image.open(File)
wpercent = (1080/float(original.size[1]))
hsize = int((float(original.size[0])*float(wpercent)))
original = original.resize((hsize,1080), Image.ANTIALIAS)

try:
    current_view.x
except:
    current_view = Viewer(text_root)
    current_view.hsize = hsize

if current_view.image == None:
    current_view.image = original
    current_view.original = original


parentDir = str(File)
parentDir = parentDir.rsplit('/', 1)[0]
sat_image = SatMap(parentDir  +'/')

w = Canvas(root, width = 1080/sat_image.height * sat_image.width, height=1080, cursor="target")

text_root.title("Line Segment Length")


w.bind("<Button-4>", lambda event: zoom(event, sat_image, current_view, 0.95))
w.bind("<Button-5>", lambda event: zoom(event, sat_image, current_view, 1.05))
w.bind("<Button-3>", lambda event: draw_point(event, sat_image, current_view))
w.bind("<B1-Motion>", lambda event: draw_segments(event, sat_image, current_segments, current_view))
w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_view, current_poly))

w.pack(expand=YES, fill=BOTH)


print('hi')


#w.create_image(current_view.x, current_view.y, image=img, anchor="nw")

root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])

#image.thumbnail(size, Image.ANTIALIAS)


#w.config(font=("Ariel", 18, 'bold'))



# w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_poly))

# find path and subtract image name to get parent direcrtory.  make variable name.
    # label1 = Label(w, text='x"\n"y', bd=1, relief="solid", font="Times 32", width=15, height=4, anchor=SW)
generate_image(current_view)
root.mainloop()
