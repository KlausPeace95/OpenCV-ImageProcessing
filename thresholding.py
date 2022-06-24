import cv2 as cv

img1 = cv.imread('data/images/klaus.jpg')
img = cv.resize(img1, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding (Manually Specify the thresholding values)
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)
threshold, thresh_inverse = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Threshold', thresh_inverse)

# Adaptive Thresholding (Computer finds the threshold value)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
# adaptive_thresh_inverse = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 9)
# cv.imshow('Adaptive Inverse Thresholding', adaptive_thresh_inverse)
adaptive_thresh_g = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Gaussian Thresholding', adaptive_thresh_g)

cv.waitKey(0)