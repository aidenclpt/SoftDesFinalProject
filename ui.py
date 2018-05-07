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
        self.points = []
        self.lines = None
        self.ovals = []
        self.vertices = []
        self.T = Text(text_root, height=2, width=40)
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
        self.w.bind("<Button-2>", lambda event: self.reset(event))
        self.w.bind("<B1-Motion>", lambda event: self.draw_segments(event))
        self.w.bind("<Enter>",self.clear_points)


    def update_image(self):
        self.w.delete(self.tkimage)

        self.image = self.original.resize((int(self.hsize*self.scale),int(self.vsize*self.scale)), Image.ANTIALIAS)
        self.photoim = ImageTk.PhotoImage(self.image)
        self.tkimage = self.w.create_image(-self.x, -self.y, image=self.photoim, anchor=NW)

        self.update()

    def zoom(self, event, scale):

        self.corners[0] = (self.corners[0] - event.x)*scale + event.x
        self.corners[1] = (self.corners[1] - event.y)*scale + event.y
        self.x = -self.corners[0]
        self.y = -self.corners[1]
        self.scale = self.scale * scale
        self.sat_image.scale = self.sat_image.scale/scale


        for i in range(len(self.points)):

            self.points[i][0] = (self.points[i][0] - event.x)*scale + event.x
            self.points[i][1] = (self.points[i][1] - event.y)*scale + event.y



        for i in range(len(self.segments.kinter_coords)):
            if i%2 == 0:
                new_x = (self.segments.kinter_coords[i] - event.x)*scale + event.x
                self.segments.kinter_coords[i] = new_x

            else:
                new_y = (self.segments.kinter_coords[i] - event.y)*scale + event.y
                self.segments.kinter_coords[i] = new_y
                self.segments.point_list[int((i-1)/2)].x = new_x
                self.segments.point_list[int((i-1)/2)].y = new_y
        self.segments.get_length()

        for i in range(len(self.polygon.kinter_coords)):
            if i%2 == 0:
                new_x = (self.polygon.kinter_coords[i] - event.x)*scale + event.x
                self.polygon.kinter_coords[i] = new_x

            else:
                new_y = (self.polygon.kinter_coords[i] - event.y)*scale + event.y
                self.polygon.kinter_coords[i] = new_y
                self.polygon.point_list[int((i-1)/2)].x = new_x
                self.polygon.point_list[int((i-1)/2)].y = new_y

        for i in range(len(self.polygon.point_list)):
            utm = self.sat_image.get_utm(self.polygon.point_list[i].x,self.polygon.point_list[i].y)
            self.polygon.point_list[i].utm = utm

        self.polygon.get_area()
        self.update_image()

    def update(self):
        FillColor = "#FF0000"

        for vertex in self.vertices:
            self.w.delete(vertex)

        self.vertices = []

        for point in self.polygon.point_list:
            x1, y1 = (point.x - 2), (point.y - 2)
            x2, y2 = (point.x + 2), (point.y + 2)
            self.vertices.append(self.w.create_oval(x1, y1, x2, y2, fill=FillColor))

        for oval in self.ovals:
            self.w.delete(oval)

        for point in self.points:
            x1, y1 = (point[0] - 2), (point[1] - 2)
            x2, y2 = (point[0] + 2), (point[1] + 2)
            self.ovals.append(self.w.create_oval(x1, y1, x2, y2, fill=FillColor))

        self.w.delete(self.lines)
        if len(self.segments.point_list) >=2:
            self.lines = self.w.create_line(*self.segments.kinter_coords, fill = 'red', width = '5')

        self.w.delete(self.tkpoly)
        if len(self.polygon.point_list) >=3:
            self.tkpoly = self.w.create_polygon(self.polygon.kinter_coords, outline = 'red', fill = '', width = 2)


    def reset(self, event):
        for oval in self.ovals:
            self.w.delete(oval)
        self.ovals = []


        for vertex in self.vertices:
            self.w.delete(vertex)

        self.vertices = []

        self.w.delete(self.lines)
        self.lines = None

        self.w.delete(self.tkpoly)
        self.tkpoly = None

        self.segments = GeoSegments([])
        self.polygon = GeoPoly([])

        self.w.delete(self.tkimage)
        self.scale = 1
        # self.image = self.original
        # self.photoim = ImageTk.PhotoImage(self.image)
        # self.tkimage = self.w.create_image(0, 0, image=self.photoim, anchor=NW)
        self.x = 0
        self.y = 0

        self.corners = [0,0]
        self.update_image()



    def draw_point(self, event):

        FillColor = "#FF0000"
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.ovals.append(self.w.create_oval(x1, y1, x2, y2, fill=FillColor))
        x = event.x
        y = event.y
        coordlist = []
        coordlist.append(x)
        coordlist.append(y)
        self.points.append(coordlist)
        utm = self.sat_image.get_utm(x,y)
        self.T3.delete('1.0', END)

        self.T3.insert(END, str(utm))
        latlong = self.sat_image.get_lat_lon(x,y)
        geostring = str(latlong[0]) + ', ' + str(latlong[1])
        geo.attraction_info(geo.find_attraction(geostring))

    def clear_points(self, event):
        self.points = []
        for oval in self.ovals:
            self.w.delete(oval)

    def draw_segments(self, event):
        FillColor = "#FF0000"
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
        self.vertices.append(self.w.create_oval(x1, y1, x2, y2, fill=FillColor))

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



#setting up window
root = Tk()
text_root = Toplevel()

File = askopenfilename(parent=root, initialdir="../", title='Select an image')

text_root.title("Line Segment Length")


Viewer(root, text_root, File)

root.title("Draw Some Points!")
current_segments = GeoSegments([])
current_poly = GeoPoly([])
root.mainloop()
