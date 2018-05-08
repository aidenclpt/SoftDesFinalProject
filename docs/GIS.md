**Pages:** | [***Home***](https://rickyroze.github.io/SoftDesFinalProject/) | [Google Maps](https://rickyroze.github.io/SoftDesFinalProject/MapPage "Google Maps API page") | [Process and Implementation](https://rickyroze.github.io/SoftDesFinalProject/TechnicalPage "Technical Page") | [Outcomes and Application](https://rickyroze.github.io/SoftDesFinalProject/ResultsPage "Results") | [Our Story](https://rickyroze.github.io/SoftDesFinalProject/OurStory "Our Story") |
### Geographic and Satellite Information


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

        utm_easting = self.easting + x*self.x_width*self.scale
        utm_northing = self.northing + y*self.y_width*self.scale

        return utm_easting, utm_northing
     
  
  The user is also able to zoom in and out. In the user interface, this effect is acheived by scaling up the image by a set 
  scale factor each time the program reads in a scroll wheel input and then moving the top left corner such that the center of
  the zoom is the location of the cursor. The scale factor of the model is also changed such that the function above will still 
  return accurate coordinates allowing the length and area finding capabilities to function on zoomed images.

[***Home***](https://rickyroze.github.io/SoftDesFinalProject/)
