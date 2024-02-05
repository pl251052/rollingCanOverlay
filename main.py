#import cv2 and numpy to read and process image
import cv2 as cv
import numpy as np
#import overlay code
from overlay_code import *



if __name__ == "__main__":
    capture = cv.VideoCapture("IMG_2799.mov") #Gets and saves video
    while True:
        # Runs trough the video, frame by frame
        there, img = capture.read()
        if there: # Prevents errors by making sure the frame is there
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Converts each frame to grayscale
            gray = cv.blur(gray, (1, 1))
            gray = cv.medianBlur(gray, 1) #Blur image using average pixel, this is to remove noise and make the outer ring of the can pop out
            img = overlay(gray,img)
            cv.imshow("Detected", img) #Shows image with overlay
            cv.waitKey(1)
        else:
            break
          
    capture.release()
    cv.destroyAllWindows() #Releases the video and closes all open windows.