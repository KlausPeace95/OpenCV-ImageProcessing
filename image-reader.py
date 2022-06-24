import cv2 as cv

path = r'data/images/flower1.jpeg'
img = cv.imread(path)

window_name = 'Face'

cv.imshow(window_name, img)
cv.waitKey(0)

cv.destroyAllWindows()

