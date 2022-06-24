import cv2 as cv
import numpy as np

img = cv.imread('data/images/klaus.jpg')
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Person', resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(resized, resized, mask=mask)
cv.imshow('Masked Image', masked)

masked1 = cv.bitwise_or(resized, resized, mask=mask)
cv.imshow('Masked Image 1', masked1)

cv.waitKey(0)