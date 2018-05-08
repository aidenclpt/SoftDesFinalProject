# Creates SatMap, GeoPoint, GeoLine, and GeoSegments bojects for the measurement
# of real distances from satellite photos and metadata files
import cv2
import numpy as np
import utm
import os
from shapely.geometry import Polygon


class SatMap:
    """Object containing image of a map containing the UTM and Lat-Lon
    coordinates of each pixel"""

    def parse_wld(self,wld_location):
        """Reads a .wld file in and esxtracts the information needed to describe
        the an images's location in the world using UTM"""

        wld = open(wld_location)
        x_width = wld.readline()
        D = wld.readline()
        B = wld.readline()
        y_width = wld.readline()
        easting = wld.readline()
        northing = wld.readline()

        return float(x_width), float(y_width), float(easting), float(northing)

    def parse_xml(self,xml_location):
        """Reads the .xml metadata file to find the UTM zone number and letter
        of the image"""

        xml = open(xml_location)
        xml.readline()
        words = str(xml.readline()).split(' ')
        for i in range(len(words)):
            if words[i] == 'zone':
                zone = words[i+1]
        zone_letter = zone[2]
        zone_number = int(zone[0] + zone[1])


        return int(zone_number), zone_letter

    def load_image(self, brightness = 0):
        """Takes in a file path and returns a numpy array containing a list of pixel values
        for each band in the list"""
        file_path = self.image_location
        print(file_path)
        im = cv2.imread(file_path)

        self.image = im
        self.height = im.shape[0]
        self.width = im.shape[1]
        self.num_channels = im.shape[2]

    def __init__(self,directory):
        """Creates a SatMap object based on a directory containing an image file,
        .wld file, and .xml file (a "GIS Ready Bundle" as downlaoded from the USGS)"""


        self.directory = directory
        self.files = os.listdir(directory)

        for file_name in self.files:
            if '.wld' in str(file_name):
                self.wld_location = directory + str(file_name)
            if '.jpg' in str(file_name) and not '.xml' in file_name:
                self.image_location = directory + str(file_name)
            if '.xml' in str(file_name):
                self.xml_location = directory + str(file_name)
        self.load_image()


        self.zone_number, self.zone_letter = self.parse_xml(self.xml_location)
        self.x_width, self.y_width, self.easting, self.northing = self.parse_wld(self.wld_location)
        self.scale = self.height/1080

    def get_utm(self,x,y):
        """Returns the UTM coordinates for given pixel locations x and y in the
        image"""

        utm_easting = self.easting + x*self.x_width*self.scale
        utm_northing = self.northing + y*self.y_width*self.scale

        return utm_easting, utm_northing

    def get_lat_lon(self,x,y):
        """Returns lattitude and longitude coordinations for given pixel locations
        x and y in the image"""


        utm_easting, utm_northing = self.get_utm(x,y)
        lat_lon = utm.to_latlon(utm_easting, utm_northing, self.zone_number, self.zone_letter)

        return lat_lon

class GeoPoint:
    """A point representing a physical location in a satellite image, located
    with pixel location, UTM coordinates, and lat-lon coordinates"""

    def __init__(self, map, x, y, size = 10, scale = 1):
        """makes a GoePoint object at """
        self.x = x
        self.y = y
        self.size = size
        self.map = map
        self.utm = map.get_utm(x,y)
        self.lat_lon = map.get_lat_lon(x,y)

class GeoLine:
    """A line connecting two GeoPoints with length in both pixel units and meters"""

    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2
        self.x1 = self.start.x
        self.y1 = self.start.y
        self.x2 = self.end.x
        self.y2 = self.end.y

        self.pixel_length = ((self.start.x-self.end.x)**2 + (self.start.y-self.end.y)**2)**0.5
        self.real_length = ((self.start.utm[0]-self.end.utm[0])**2 + (self.start.utm[1]-self.end.utm[1])**2)**0.5

class GeoPoly:
    """A polygon made up of GeoPoints used to find the length of complex paths and
    the area of complex shapes"""

    def __init__(self, point_list):
        self.kinter_coords = []
        self.shapely_coords = []
        self.point_list = point_list

        for point in point_list:
            self.kinter_coords.append(point.x)
            self.kinter_coords.append(point.y)
            self.shapely_coords.append(point.utm)

        if len(self.point_list) >=3:
            self.shapely_coords = tuple(self.shapely_coords)
            self.poly = Polygon(self.shapely_coords)
            self.area = self.poly.area


    def get_area(self):
        self.area = 0
        self.shapely_coords = []
        self.kinter_coords = []

        for point in self.point_list:
            self.kinter_coords.append(point.x)
            self.kinter_coords.append(point.y)
            self.shapely_coords.append(point.utm)

        if len(self.point_list) >=3:
            self.shapely_coords = tuple(self.shapely_coords)
            self.poly = Polygon(self.shapely_coords)
            self.area = self.poly.area
        return self.area


class GeoSegments:
    """A series of segments meant to approximate a non-linear path drawn by the
    user, primarily in order to find it's length"""

    def __init__(self, point_list):
        self.kinter_coords = []
        self.lines = []
        self.length = 0
        self.point_list = point_list

        if len(self.point_list) >= 2:
            for i in range(len(self.point_list)-1):
                line = GeoLine(self.point_list[i], self.point_list[i+1])
                self.lines.append(line)
                self.length += line.real_length

    def get_length(self):
        self.length = 0
        self.lines = []
        self.kinter_coords = []
        
        if len(self.point_list) >= 2:
            for i in range(len(self.point_list)-1):
                line = GeoLine(self.point_list[i], self.point_list[i+1])
                self.lines.append(line)
                self.length += line.real_length

        for point in self.point_list:
            self.kinter_coords.append(point.x)
            self.kinter_coords.append(point.y)

        return self.length



if __name__ == "__main__":
    directory = '/home/aiden/Final_Project_Image_Repo/images_with_metadata/Vasquez/'

    test = SatMap(directory)
    p1 = GeoPoint(test, 0, 0)
    p2 = GeoPoint(test, 0, 1)
    p3 = GeoPoint(test, 1, 1)
    p4 = GeoPoint(test, 1, 0)

    line = GeoLine(p1, p2)
    poly = GeoPoly([p1,p2,p3,p4])

    segments = GeoSegments([p1,p2,p3,p4])
    print(segments.length)
