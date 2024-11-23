import cv2 as cv 

# Reading images 
# img = cv.imread('photos/group 1.jpg')

# cv.imshow('Group', img)

import cv2 as cv 

# Reading images 
# img = cv.imread('photos/group 1.jpg')

# cv.imshow('Group', img)

# Reading videos

capture = cv.VideoCapture('dog.mp4')

while True:
  isTrue, frame = capture.read()

  cv.imshow('video', frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

  capture.release()
  cv.destroyAllWindows()

cv.waitKey(0)
