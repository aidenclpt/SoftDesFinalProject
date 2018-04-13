import numpy as np
import cv2

"""
example that finds shapes and distinguishes between squares,
rectangles, and triangles, and colors them in different colors
approxpolydp gets an approximation of the shape which is what
allows us to color it in
"""

img = cv2.imread('try1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,1)
_,contours,h = cv2.findContours(thresh,1,2)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==5:
        print ("pentagon")
        cv2.drawContours(img,[cnt],0,(0,255,0),3)
    elif len(approx)==3:
        print ("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),3)
    elif len(approx)==4:
        print ("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
