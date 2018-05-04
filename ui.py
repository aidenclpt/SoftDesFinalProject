from tkinter import *
import time
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from lat_lon import SatMap, GeoSegments, GeoPoint, GeoPoly
import tkinter.simpledialog
import geo

Image.MAX_IMAGE_PIXELS = 250000000

class Viewer:
    def __init__(self, main_root, text_root, image_file):

        original = Image.open(image_file)
        wpercent = (1080/float(original.size[1]))
        self.hsize = int((float(original.size[0])*float(wpercent)))
        self.vsize = 1080
        self.original = original.resize((self.hsize,1080), Image.ANTIALIAS)

        parentDir = str(image_file)
        self.parentDir = parentDir.rsplit('/', 1)[0]
        self.sat_image = SatMap(self.parentDir  +'/')

        self.w = Canvas(main_root, width = 1080/self.sat_image.height * self.sat_image.width, height=1080, cursor="target")
        self.w.pack(expand=YES, fill=BOTH)
        self.points = None
        self.lines = None
        self.polygon = None
        self.T = Text(text_root, height=2, width=30)
        self.T.pack(side = RIGHT)

        self.x = 0
        self.y = 0
        self.scale = 1

        self.image = self.original
        self.tkimage = self.w.create_image(int(self.x), int(self.y), image=ImageTk.PhotoImage(self.image), anchor="nw")

        self.w.bind("<Button-4>", lambda event: self.update_image(event, 0.95))
        self.w.bind("<Button-5>", lambda event: self.update_image(event, 1.05))
        self.w.bind("<Button-3>", lambda event: self.raw_point(event))
        self.w.bind("<B1-Motion>", lambda event:self.draw_segments(event))

    def update_image(view, w):

        self.w.itemconfig(self.tkimage, image = ImageTk.PhotoImage(self.image))
        # w.delete(view.tkimage)


        # view.image = view.original.resize((int(view.hsize*view.scale),int(view.vsize*view.scale)), Image.ANTIALIAS)
        #
        #
        # # print(img)
        #
        #
        # if not view.started:
        #
        #     print(view.tkimage)
        #     view.started = True
        #     mainloop()
        # else:
        #     print(view.tkimage)
        #     w.itemconfig(view.tkimage, image = img)
        #
        #
        # #mainloop()


    def zoom(event, sat_map, view, w, scale):

        view.scale = view.scale * scale
        sat_map.scale = sat_map.scale/scale
        dx = (event.x - view.hsize/2)*(scale-1)
        dy = (event.y - view.vsize/2)*(scale-1)
        view.x = view.x - dx
        view.y = view.y - dy
        print(view.scale)

        self.update_image()



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

    #mainloop()

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
    #mainloop()


#setting up window
root = Tk()
text_root = Tk()

File = askopenfilename(parent=root, initialdir="../", title='Select an image')

text_root.title("Line Segment Length")

#w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_view, current_poly))


current_view = Viewer(root, text_root, File)
#w.create_image(current_view.x, current_view.y, image=img, anchor="nw")

root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])
root.mainloop()
