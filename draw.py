import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# 1. Paint the image a certain color

img = cv.imread('data/images/house.jpeg')

blank[:] = 255,255,255   # Painting entire image with white
cv.imshow('White', blank)

blank[200:300, 300:400] = 0,0,255   # Painting a portion of image red
cv.imshow('Red', blank)

# cv.imshow('House', img)

# 2. Draw Rectangle
# cv.rectangle(blank, (100,100), (250,400), (0,0,255), thickness=5)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=10)  # Dynamic Sizing
# cv.rectangle(blank, (100,100), (250,400), (0,0,255), thickness=cv.FILLED) # Fill rectangle
# cv.rectangle(blank, (100,100), (250,400), (0,0,255), thickness=-1) # Fill rectangle
cv.imshow('Rectangle', blank)

# 3. Draw Circle
# cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (0,255,0), thickness=3) # Green Circle at the centre of the image with radius 3
# cv.imshow('Circle', img)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3) # Green Circle at the centre of the image with radius 3
cv.imshow('Circle', blank)

# 4. Draw Line
cv.line(blank, (0,0), (blank.shape[1]//1, blank.shape[0]//1), (0,0,0), thickness=3)
cv.imshow('Line', blank)

# Write Text on Image
cv.putText(img, 'Klaus', (200, 47), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0), 1)
cv.imshow('Text', img)

cv.waitKey(0)
