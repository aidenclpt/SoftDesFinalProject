**AR 2 Reflection

*Feedback and decisions

General feedback about the project was that people felt a lot better about the scope and focus of our project than they did at our last architectural review. However, they were still confused about why our project was interesting, and why someone would want it. In the future, we are going to work closely with the UI specifically to make this user experience more intentional and clear. We were given the feedback that the GUI would be done most efficiently in Tkinter; however, that will have a “90s Windows” look. An alternative for that is pyQT, but it is a bit less fleshed out so it may be more difficult to use. We took this into account and decided to start with Tkinter and see where this gets us because it will allow us to do file browsing and not run the UI from the command line.

On more of a feature detection note, it was pointed out that curvy lines are something we need to be more focused on as roads are inconsistent, so we have started looking into using HoughLines to detect curves and not just straight lines. While we had already been using Houghlines, no curvy lines have been detected, so we need to look into that further. It was suggested that we average color of roads and weed out that to help us increase road detection accuracy. As far as image processing, the general consensus was that as long as the satellite image was easy to read, “true color” does not really matter. Beyond that, there was little feedback about other ways we should be processing images. We are working now on increasing contrast so that the satellite images are easier to read and process. New questions moving forward are: How will we detect curved lines? How will we make this a distinguishable project (there is some confusion about why we are doing this)? What can we add to make this useful to the user beyond extracting a digital map? Moving forward we are going to look into different statistics we can calculate as well to give with the newly generated map (ie. longest road, how square a city is, etc.).

*Review process reflection 

Considering only one of us was able to present, the review went pretty well. In the past, we have not made a presentation, and having one this time proved very valuable. That being said, while we got answers to some of our questions, but a lot of our questions were left unanswered. While we gave ample information about what our program does and what we want it to do, we did not explain how our programs work which made the technical conversations a bit harder. It was difficult to explain the parts of the project that those not present were more involved with, but we did our best. Because we made a powerpoint presentation, we stuck pretty directly to the plan. I think that giving more background on how our programs work, and not just what they do would be appreciated by the audience. If we were to do this over again, we would explain how our code works in much more depth, and not just what it does. Hopefully, this would allow our audience to better understand where we are and where we are trying to go.