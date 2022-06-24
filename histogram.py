
# Histograms allow you to visualise the distribution of pixel intensity in an image

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread('data/images/klaus.jpg')
img = cv.resize(img1, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Person', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)


# Gray scale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
#
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixes')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixes')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)
plt.show()

cv.waitKey(0)