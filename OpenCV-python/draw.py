import cv2 as cv 
import numpy as np

blank = np.zeros((500, 500,3), dtype='uint8')

cv.imshow('blank', blank)

#img = cv.imread('photos/cat.jpg')
#cv.imshow('Cat', img)

# pait the image in the certain colors 

#blank[200:300, 300:400] = 0,225,0
#cv.imshow('blank', blank)

# draw a rectangle
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=-1)
#cv.imshow('rectangle', blank)

# draw a circle
#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,225), thickness=-1) # -1 means the circled is filled.
#cv.imshow('circle', blank)

# draw the line
#cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)
#cv.imshow('line', blank)

# Write text
cv.putText(blank, 'hello, my name is elizaa!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow('text', blank)
cv.waitKey(0)