import cv2
import numpy as np
import utm
import os


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

    def load_image(self, brightness = 20):
        """Takes in a file path and returns a numpy array containing a list of pixel values
        for each band in the list"""
        file_path = self.image_location

        im = cv2.imread(file_path)
        self.image = im
        self.height = im.shape[0]
        self.width = im.shape[1]
        self.num_channels = im.shape[2]
        self.utm_map = np.zeros((self.height,self.width,2))
        self.lat_lon_map = np.zeros((self.height,self.width,2))

        channels = cv2.split(im)
        res = []

        for channel in channels:
            if sum(channel)[0] > 0:
                res.append(cv2.equalizeHist(channel))

        equalized = np.zeros((im.shape[0], im.shape[1], len(res)))

        for i in range(equalized.shape[2]):
            equalized[:,:,i] = res[i] + brightness

        cv2.imwrite(self.directory + '/results/test.jpg',im)

    def __init__(self,directory):
        """Creates a SatMap object based on a directory containing an image file,
        .wld file, ad .xml file (a "GIS Ready Bundle" as downlaoded from the USGS)"""

        self.directory = directory
        self.files = os.listdir(directory)
        if not os.path.exists(directory):
            os.makedirs(directory + '/results')

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


    def get_utm(self,x,y):
        """Returns the UTM coordinates for given pixel locations x and y in the
        image"""

        utm_easting = self.easting + x*self.x_width
        utm_northing = self.northing + y*self.y_width

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

    def __init__(self, map, x, y, size = 10):
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

        self.pixel_length = ((start.x-end.x)**2 + (start.y-end.y)**2)**0.5
        self.real_length = ((start.utm[0]-end.utm[0])**2 + (start.utm[1]-end.utm[1])**2)**0.5





directory = '/home/aiden/Final_Project_Image_Repo/images_with_metadata/'

test = SatMap(directory)
p1 = GeoPoint()
