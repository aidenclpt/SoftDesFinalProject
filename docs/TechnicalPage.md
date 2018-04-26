### Technical Page
  Implementation:
+ We will have a flow chart separated into three main blocks- image processing, google maps API, GUI
+ We will then treat each module as its own heading and within them explain their flow process
+ Generally the process is Parse GIS -> maps API -> GUI
+ Maps API-> takes a given latitude and longitude -> gives latitude and longitude to google places then returns location details and address -> can now return name of neighborhood, rating of the area, etc. ->searches address within given radius for restaurants nearby -> searches google images by restaurant name and returns images
+ Implementation: To run this program you will need to install numpy, googleplace, PIL, geopy.geocoders, io, and Tkinter. After this clone the repositoy (https://github.com/rickyroze/SoftDesFinalProject.git) and run Final.py. You will be asked to select an image to run the program with, you can either use an image we have provided from USGS (also in this repository:https://github.com/aidenclpt/Final_Project_Image_Repo) or import your own satellite images. After this run the program and the GUI will pop up allowing you full access to the program! 
+Attributions: United States Geological Survey (USGS), Google Places API Documentation
[***Home***](https://rickyroze.github.io/SoftDesFinalProject/)
![alt text](SoftDesFinalProject/docs/flowchart.png "Flowchart1")

