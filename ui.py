from tkinter import *
import time
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from lat_lon import SatMap, GeoSegments, GeoPoint, GeoPoly
import tkinter.simpledialog
import geo

Image.MAX_IMAGE_PIXELS = 250000000

class Viewer():
    def __init__(self, main_root, text_root, image_file):

        original = Image.open(image_file)
        wpercent = (1080/float(original.size[1]))
        self.hsize = int((float(original.size[0])*float(wpercent)))
        self.vsize = 1080
        self.original = original.resize((self.hsize,self.vsize), Image.ANTIALIAS)

        parentDir = str(image_file)
        self.parentDir = parentDir.rsplit('/', 1)[0]
        self.sat_image = SatMap(self.parentDir  +'/')
        self.segments = GeoSegments([])
        self.polygon = GeoPoly([])
        self.tkpoly = None

        self.w = Canvas(main_root, width = self.hsize, height=self.vsize, cursor="target")
        self.w.pack(expand=YES, fill=BOTH)
        self.w.grid(row = 0, column = 0)
        self.points = None
        self.lines = None
        self.T = Text(text_root, height=2, width=30)
        self.T.pack(side = RIGHT)

        text_root_2 = Toplevel()
        text_root_2.title("Polygon Area")
        self.T2 = Text(text_root_2, height=2, width=40)
        self.T2.pack()

        text_root_3 = Toplevel()
        text_root_3.title("Point Coordinates")
        self.T3 = Text(text_root_3, height=2, width=40)
        self.T3.pack()

        self.x = 0
        self.y = 0
        self.scale = 1
        self.place_img = None
        self.image = self.original
        self.photoim = ImageTk.PhotoImage(self.image)
        self.tkimage = self.w.create_image(0, 0, image=self.photoim, anchor=NW)


        self.corners = [0,0]
        self.w.bind("<Button-4>", lambda event: self.zoom(event, 0.95))
        self.w.bind("<Button-5>", lambda event: self.zoom(event, 1.05))
        self.w.bind("<Button-3>", lambda event: self.draw_point(event))
        self.w.bind("<Button-1>", lambda event: self.draw_poly(event))
        self.w.bind("<B1-Motion>", lambda event: self.draw_segments(event))


    def update_image(self):
        self.w.delete(self.tkimage)

        self.image = self.original.resize((int(self.hsize*self.scale),int(self.vsize*self.scale)), Image.ANTIALIAS)
        self.photoim = ImageTk.PhotoImage(self.image)
        self.tkimage = self.w.create_image(-self.x, -self.y, image=self.photoim, anchor=NW)

    def zoom(self, event, scale):

        self.corners[0] = (self.corners[0] - event.x)*scale + event.x
        self.corners[1] = (self.corners[1] - event.y)*scale + event.y
        self.x = -self.corners[0]
        self.y = -self.corners[1]
        self.scale = self.scale * scale
        self.sat_image.scale = self.sat_image.scale/scale
        self.update_image()

    def draw_point(self, event):
        FillColor = "#FF0000"
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.w.create_oval(x1, y1, x2, y2, fill=FillColor)
        x = event.x
        y = event.y
        coordlist = []
        coordlist.append(x)
        coordlist.append(y)
        utm = self.sat_image.get_utm(x,y)
        self.T3.delete('1.0', END)

        self.T3.insert(END, str(utm))
        print(str(utm))
        latlong = self.sat_image.get_lat_lon(x,y)
        geostring = str(latlong[0]) + ', ' + str(latlong[1])
        geo.attraction_info(geo.find_attraction(geostring))


    def draw_segments(self, event):
        FillColor = "#FF0000"
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        # self.w.create_oval(x1, y1, x2, y2, fill=FillColor)
        self.w.delete(self.lines)
        x = event.x
        y = event.y

        point = GeoPoint(self.sat_image, x, y)
        self.segments.point_list.append(point)

        self.segments.get_length()
        if len(self.segments.point_list) >=2:
            self.lines = self.w.create_line(*self.segments.kinter_coords, fill = 'red', width = '5')

        self.T.delete('1.0', END)

        self.T.insert(END, self.segments.length)





    def draw_poly(self, event):
        FillColor = "#FF0000"
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        # self.w.create_oval(x1, y1, x2, y2, fill=FillColor)

        self.w.delete(self.tkpoly)
        x = event.x
        y = event.y

        point = GeoPoint(self.sat_image, x, y)
        self.polygon.point_list.append(point)
        area = self.polygon.get_area()
        if len(self.polygon.point_list) >=3:
            self.tkpoly = self.w.create_polygon(self.polygon.kinter_coords, outline = 'red', fill = '', width = 2)


        self.T2.delete('1.0', END)

        self.T2.insert(END, area)
    #mainloop()


#setting up window
root = Tk()
text_root = Toplevel()

File = askopenfilename(parent=root, initialdir="../", title='Select an image')

text_root.title("Line Segment Length")

#w.bind("<ButtonPress-1>", lambda event: draw_poly(event, sat_image, current_view, current_poly))


Viewer(root, text_root, File)
#w.create_image(current_view.x, current_view.y, image=img, anchor="nw")

root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])
root.mainloop()
