import cv2 as cv
import numpy as np


def overlay(grayed, img):
    elements = grayed.shape[0] #Shows the number of elements in the numpy array
    circles = cv.HoughCircles(grayed, cv.HOUGH_GRADIENT, 1, elements / 8, param1=30, param2=55, minRadius=110, maxRadius=150)
    # Creates a circle around the outer ring of the can using a high param1 & param2 to indicate that a large difference in gradient is neccessary.
    # The minRadius and maxRadius are extra precautions against detecting circles that arent actually there.
    if circles is not None: #checks if circles are actually detected
        circles = np.uint16(np.around(circles)) #rounds the numbers so the next few steps work
        for circle in circles[0, :]:
            center = (circle[0], circle[1]) # finds the coordinate of the center of the circle
            cv.circle(img, center, 1, (0, 0, 255), 6) #draws a point by drawing a very thick circle with a small radius.
            radius = circle[2] #finds the radius of the circle
            cv.circle(img, center, radius, (0, 255, 0), 10) #overlays the circumfrence of the circle
        return img #returns image with overlay
    else:
        return img #returns image without overlay
        #Keeps the program from resulting in an error if there are no circles detected