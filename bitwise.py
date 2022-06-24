# Bitwise Operators operate in a binary fashion ("1" for "ON" and "0" for "OFF")

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)  # Returns the intersecting region of the two images

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)  # Returns the intersecting and non-intersecting regions of the two images

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)  # Returns the non-intersecting region of the two images

# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Rectangle NOT', bitwise_not)  # Returns nothing (inverts the bit)
bitwise_not1 = cv.bitwise_not(circle)
cv.imshow('Bitwise Circle NOT', bitwise_not1)  # Returns nothing (inverts the bit)
bitwise_xor_not = cv.bitwise_not(bitwise_xor)
cv.imshow('Bitwise XOR NOT', bitwise_xor_not)  # Inverts the non-intersecting region

cv.waitKey(0)