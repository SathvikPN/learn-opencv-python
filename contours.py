import cv2 as cv
from rescale import rescaleFrame
import numpy as np

original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
# cv.imshow('Original_Image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY',gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)