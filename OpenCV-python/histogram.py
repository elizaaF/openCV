import cv2 as cv 
import numpy as np 

# import matplotlib.pyplot as plt

img = cv.imread('photos/cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

grey = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.imshow('Gray', grey)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

# Grayscale Histogram 
gray_hist = cv.calcHist([grey], [0], None, [256], [0,256])

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('bin')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0, 256])
#plt.show()

# Colour Histogram 

#plt.figure()
#plt.title('Color Histogram')
#plt.xlabel('bins')
#plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
  hist = cv.calcHist([img], [i], mask, [256], [0,256])
  #plt.plot(hist, color=col)
  #plt.xlim([0, 256])

#plt.show()

cv.waitKey(0)