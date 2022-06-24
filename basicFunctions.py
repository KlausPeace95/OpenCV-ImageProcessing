import cv2 as cv

img = cv.imread('data/images/face2.jpeg')
cv.imshow('Person', img)

img1 = cv.imread('data/images/house2.jpeg')
cv.imshow('House', img1)

# 1. Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred Face', blur)

blur = cv.GaussianBlur(img1, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred House', blur)

# 3. Create an Edge Cascade
canny = cv.Canny(img1, 125, 175)
cv.imshow('Canny Edges', canny)

canny1 = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges for Blurred', canny1)

# 4. Dilating an image
dilated = cv.dilate(canny1, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Erode image (Try to bring back original image after dilation)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resize images
resized = cv.resize(img1, (800, 400), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized_UP', resized)

resized1 = cv.resize(img1, (200, 150), interpolation=cv.INTER_AREA)
cv.imshow('Resized_DOWN', resized)

# 7. Crop an Image (On the basis that images are arrays)
cropped = img1[100:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)