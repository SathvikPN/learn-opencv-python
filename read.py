import cv2 as cv
# Read Images
img = cv.imread('Photos/Saath.jpg')
cv.imshow('window_name', img)
cv.waitKey(0)

# Read Videos
capture = cv.VideoCapture('Videos/hurray.mp4')
while True:
    isTrue, frame = capture.read() # frame by frame
    cv.imshow('MyVideo', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
