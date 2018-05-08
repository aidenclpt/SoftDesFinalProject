# Satelite Image Processing
By Aiden Carley-Clopton, Grace Montagnino, and Richard Rose

# Relevant Files
Please note that because this was a long term project, there have been several iterations and versions of this code. With this in mind, the only files relevant to the final product are: Fianl.py, geo.py, ui.py, latlong.py.

Video Link:
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)


Poster Link:

# The Program
Our project is a tool for taking in satellite images in a “GIS ready bundle” (containing a .wld file and .xml file with image metadata, as would be downloaded from a source of satellite images, such as the USGS) and translating the size of features in the image to their size and location in the real world. Points, lines, and contours can be drawn in by the user to measure position, length, and area of features in the image. In addition, our code interfaces with the Google Maps API to find nearby features to coordinates selected in the image.

# Dependencies
To run this program you will need to install numpy,googleplace,PIL,geopy.geocoders,cv2,utm,shapely. You can use the following commands to do so.

    pip install numpy
    pip install python-google-places
    pip install Pillow
    pip install geopy
    pip install opencv-python
    pip install utm
    pip install shapely

After installing all necessary software clone the repositoy (https://github.com/rickyroze/SoftDesFinalProject.git) and run Final.py.

    git clone https://github.com/rickyroze/SoftDesFinalProject.git
    python3 Final.py

A file selector will pop up and you will be asked to select an image to run the program with, you can either use an image we have provided from USGS (also in this repository:https://github.com/aidenclpt/Final_Project_Image_Repo) or import your own satellite images. If you choose to use an image from us, you will want to run the line of code below in your terminal window.

    git clone https://github.com/aidenclpt/Final_Project_Image_Repo.git

After the GUI will pop up allowing you full access to the program!

# Image Repo
The small to medium sized images in this project are stored in a second github
repo. You can clone it here: https://github.com/aidenclpt/Final_Project_Image_Repo
The file path in which you locate it doesn't matter, except for a line in
image_load.py which references the landsat bands stored within it.

# image_load.py

This file contains the functions used to make color images out of multiple
channels obtained from satellite imagery. It balances the levels to account for
the fact that raw sensor data provides very dim images. It creates a directory
called "results" which will be ignored when committing to GitHub as to not clutter
the repo with generated images.

# Lisence
MIT License
Copyright (c) 2018 Richard Rose, Aiden Carley-Clopton, Grace Montagnino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Attributions:
United States Geological Survey (USGS), Google Places API Documentation, Orbview3
