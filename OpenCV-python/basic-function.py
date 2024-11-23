import cv2 as cv 

img = cv.imread('photos/boston.jpg')
cv.imshow('boston', img)

# converting to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

# blur 

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Dilating the images
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation= cv.INTER_AREA)
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)