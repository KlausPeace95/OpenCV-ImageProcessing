import cv2 as cv

path = r'data/videos/numpy.mp4'
capture = cv.VideoCapture(path)

window_name = 'Python'


while True:
    isTrue, frame = capture.read()
    cv.imshow(window_name, frame)

    if cv.waitKey(20) & 0xFF==ord('d'):    # Stops the video if key 'd' is pressed
        break

capture.release()
cv.destroyAllWindows()