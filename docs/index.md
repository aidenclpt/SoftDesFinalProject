# Homepage  
**Pages:** | [GIS](https://rickyroze.github.io/SoftDesFinalProject/GIS "GIS info page") | [Maps API Page](https://rickyroze.github.io/SoftDesFinalProject/MapPage "Google Maps API page") | [Technical Page](https://rickyroze.github.io/SoftDesFinalProject/TechnicalPage "Technical Page") | [Results Page](https://rickyroze.github.io/SoftDesFinalProject/ResultsPage "Results") | [Our Story](https://rickyroze.github.io/SoftDesFinalProject/OurStory "Our Story") |

## High level overview:

#### Parsing metadata from satellite images and providing relevant information based on user inputs.

## What does our project do?

Our project is a tool for taking in satellite images in a "GIS ready bundle"
(containing a .wld file and .xml file with image metadata, as would be
downloaded from a source of satellite images, such as the USGS) and translating
the size of features in the image to their size and location in the real world.
Points, lines, and contours can be drawn in by the user to measure position,
length, and area of features in the image. In addition, our code interfaces with
the Google Maps API to find nearby features to coordinates selected in the image.

## Why does our project matter?

This piece of software provides the user with a versatile platform to go
from readily available satellite images to sizes in the real world. Existing
services offer the ability to measure distance between points and along mapped
roads, however our software allows more versatility with the ability for the
user to draw in custom paths. This could be used to calculate the area of
geographic features, take rough measurements of buildings, or calculate the
distance of a hiking route. In addition, the modular design of the program means
that the modules can also be used individually for a file selection GUI, an
object oriented approach to managing GIS metadata, and an interface with the
Google Maps API.

