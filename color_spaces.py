import cv2 as cv # reads in BGR format
import matplotlib.pyplot as plt

from rescale import rescaleFrame


# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
# cv.imshow('Original_Image', img)


# BGR to Grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV (hue, saturation, value (brightness))
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*a*b color space 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('L*a*b',lab)

# BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB',rgb)

# Matplotlib reads img in RGB format
# plt.imshow(rgb)
# plt.show()

# cannot directly convert grayscale to hsv. 
# steps are grayscale --> BGR --> HSV

# HSV to BGR 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# similarly L*a*b to BGR

cv.waitKey(0)