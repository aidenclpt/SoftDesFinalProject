### Homepage  
**Pages:** | [GIS](https://rickyroze.github.io/SoftDesFinalProject/GIS "GIS info page") | [Map Page](https://rickyroze.github.io/SoftDesFinalProject/MapPage) | [Technical Page](https://rickyroze.github.io/SoftDesFinalProject/TechnicalPage) | [Results Page](https://rickyroze.github.io/SoftDesFinalProject/ResultsPage) |

## What does Out Project Do?

Our project is a tool for taking in satellite images in a "GIS ready bundle"
(containing a .wld file and .xml file with image metadata, as would be
downloaded from a source of satellite images, such as the USGS) and translating
the size of features in the image to their size and location in the real world.
Points, lines, and contours can be drawn in by the user to measure position,
length, and area of features in the image. In addition, our code interfaces with
the Google Maps API to find nearby features to coordinates selected in the image.

## Why does Our Project Matter?

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

## Our Story
Origionally, our goal was to create maps from satellite images by detecting streets and roads. We started with pattern detection done by the computer. As we got further into line and feature detection, we realized that our accuracy levels were too low for what we wanted to accomplish. We soon leanred that people are much better at recognizing patterns than computers, but computers can give statistics that people cannot. We decided to pivot with this notion in mind. Our program now allows users to write in their patterns, and have the computer return the statistics. For example, someone going on a roadtrip could draw in their path of travel and get estimations of distance traveled, nearby restaurants, etc. This approach to mapping allows the users to focus on the pattern and the computer to focus on the statistics. Now, after processing the satellite images into usable pictures, we use the Google Places API to gather information about each latitude and longitude.

