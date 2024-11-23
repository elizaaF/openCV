import cv2 as cv
import numpy as np

img = cv.imread('photos/boston.jpg')
cv.imshow('Boston', img)

# Translation
def translate(img, x, y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimension = (img.shape[1], img.shape[0]) # this means img-1 is width and img-2 is height
  return cv.warpAffine(img, transMat, dimension)

# -x --> Left
# -y --> Up
# x --> Right
# y --> down

tranlated = translate(img, -100, 100)
cv.imshow('translated', tranlated)

# Rotation 

def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    rotPoint =(width//2, height//2)

  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimension = (width, height)

  return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, -45)
cv.imshow('rotated', rotated)

# Resizing 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flipping 
flip = cv.flip(img,0) # if 0 is gonna be applied vertically and 1 is gonna be applied horizonatally 
cv.imshow('Flip', flip)

# cropping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)