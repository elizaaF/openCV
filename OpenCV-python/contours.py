import cv2 as cv 
import numpy as np

img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur) # so when we applied blur into that image it will reduce the contours.

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

res, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Countours drawn', blank)
cv.waitKey(0)