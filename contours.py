import cv2 as cv
import numpy as np

img = cv.imread('data/images/flower3.jpeg')
cv.imshow('Flower', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Contours are the lines or curves that join the continuous
# points along the boundary of an
# NB: CONTOURS ARE NOT EDGES

# Gray the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayed', gray)

# Blur the image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Display Edges
canny =cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Finding contours using threshold value
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# Display Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')
print(f'{len(canny)} edge(s) found')

# Draw contours on blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours_Drawn', blank)

cv.waitKey(0)