import cv2 as cv

img = cv.imread('data/images/animal3.jpeg')
cv.imshow('Animal', img)

# Averaging (Average Blur). Draws a kernel with pixels and computes the average of the surrounding pixels and assign value to the centre one
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur (Gets less blurring than Averaging but more natural than averaging)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (Similar to averaging but finds the median instead of the average of surrounding pixels). More effective in removing noise than the above
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (Used in more CV projects: It checks whether the blurring is reducing the edges or not)
bilateral = cv.bilateralFilter(img, 20, 75, 50)  # Kind of a painting version of the original image
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)