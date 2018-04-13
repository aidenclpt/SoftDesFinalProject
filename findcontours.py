import numpy as np
import cv2
"""
simple example that
finds all the contours and draws green lines around them
"""
img = cv2.imread('try1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

_,contours,h = cv2.findContours(thresh,1,2)

cv2.drawContours(img, contours, -1, (0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
