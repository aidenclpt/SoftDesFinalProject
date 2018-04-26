    ### GIS
+ Shows before and after images of satellite image processed and not processed
+ Shows with color balance and without image
+ Snippets of code to show what is being done to image
+ Shows how each pixel is mapped to a latitude/longitude

The GIS portion of our code starts by parsing metadata. A world file (.wld) looks like this

    4.0200000000 
    0.0000000000 
    0.0000000000 
    -4.0200000000 
    496748.3682234660 
    4427796.8562399521
   
These values represent the x resulution, rotation, y resolution and UTM northing and easting of the top left corner. In this case, each pixel is 4.2m in the x and y direction. This can then be used to find the position of a given pixel in the real world in UTM coordinates. From this the python utm library allows us to translate those coordinates to GPS. The code snippet below shows how the data gathered from the world file is used to relate pixel coordinates to real-world position.

    def get_utm(self,x,y):
            """Returns the UTM coordinates for given pixel locations x and y in the
            image"""

            utm_easting = self.easting + x*self.x_width
            utm_northing = self.northing + y*self.y_width

            return utm_easting, utm_northing

[***Home***](https://rickyroze.github.io/SoftDesFinalProject/)
