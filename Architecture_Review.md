# Architectural Review Preparation and Framing
Ricky Rose, Aiden Carley-Clopton, Grace Montagnino

## Background and context
Ultimately, our goal is to look at multi-channel (visible/non-visible light) satellite images and be able to locate man made artifacts (such as archaeological sites), and other significant features within them. An alternate approach would be to use Lidar point cloud data, dependent on our ability to find that data and process it. Our system would take satellite imagery, and break it up into channels. It would then use various feature detection techniques such as Canny Edge Detection to find features such as straight lines and rectangles which indicate human made products. Lidar would add a third dimension which would allow for topological features such as large flat areas to be examined as well. We would like to use this information to display locations of significant features and eventually have a user interface built for our system.

## Key questions
From this review we would like some input as to which features of images (other than edges, maybe involving a Fast Fourier Transform) we should focus in on, and what kind of preprocessing (such as vectorizing) would be necessary for those images. Currently, our team is contemplating and struggling with data sources. We are trying to balance availability of data with what operations and computations we are able to perform with it. We would like to draw in outsider perspectives mostly on what types of features in images and things in the world we should aim to find. There are a lot of different things we could focus on detecting (buildings, topography, etc.) It would be great to hear what other people think would be most interesting and correctly scoped for us in this project.

## Agenda for technical review session 
We plan to start our architectural review by explaining the premise of our project. We will explain our goals as well as our stretch goals. Following this, we will ask specific guiding questions (What features should we focus on finding? What sort of preprocessing do we need to do? Any ideas about data sources?) We will then ask follow-up questions based on the answers provided by our peers, as well as respond to any questions/concerns from our feedback group.
Feedback form link: https://goo.gl/forms/BZ8KakvNGLx1X72y2
