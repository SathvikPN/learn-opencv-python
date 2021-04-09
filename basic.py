""" Basic Functions in OpenCV """

import cv2 as cv
from rescale import rescaleFrame

# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
cv.imshow('Original_Image', img)


# 1.Convert to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# 2.Blur Image 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) # ksize must be +ve and odd
# cv.imshow('Blur', blur)


# 3.Edge Cascade 
canny = cv.Canny(img,125,175)
# cany = cv.Canny(blur,125,175) # pass blur image to reduce edges
# cv.imshow('Canny Edges', canny)


# 4.Dilating the Image 
dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)

# 5.Eroding --> nearly reverses dilation
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded',eroded)


# 6. Resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # Ignores aspect ratio
# cv.imshow('Resized', resized)

# 7.Cropping 
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)









