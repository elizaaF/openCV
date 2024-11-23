import cv2 as cv 

img = cv.imread('photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimenstion = (width, height)

  return cv.resize(frame, dimenstion, interpolation=cv.INTER_AREA)

image_resized = rescaleFrame(img)
cv.imshow('cat', image_resized)

# Reading videos

def changeRes(width, height):
  capture.set(3, width)
  capture.set(4, height)

capture = cv.VideoCapture('dog.mp4')

while True:
  isTrue, frame = capture.read()
  
  frame_resized = rescaleFrame(frame, scale=.2)

  cv.imshow('video', frame)
  cv.imshow('video', frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

  capture.release()
  cv.destroyAllWindows()

cv.waitKey(0)

cv.waitKey(0)