import cv2 as cv
import numpy as np

img = cv.imread('data/images/animal1.jpeg')
cv.imshow('Animal', img)

# 1. Translation
def translate(img, x, y):
    transMatrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

translated = translate(img, 100, 100) # 100px right and 100px down (attaching negatives change the respective directions)
cv.imshow('Translated', translated)

# 2. Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated, 30)
# cv.imshow('Rotated_Rotated', rotated_rotated)

# 3. Resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# 4. Flipping an Image
flip = cv.flip(img, 0) # Flipping Vertically 180 degrees clockwise
cv.imshow('Flipped Vertically', flip)

flip = cv.flip(img, -1) # Flipping Vertically 180 degrees anticlockwise
cv.imshow('Flipped Vertically & Horizontally', flip)

flip = cv.flip(img, 1) # Flipping Horizontally 180 degrees
cv.imshow('Flipped Horizontally', flip)



cv.waitKey(0)
