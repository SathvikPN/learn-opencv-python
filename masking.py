import cv2 as cv
import numpy as np

from rescale import rescaleFrame
# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
cv.imshow('Original_Image', img)

# size of masking image must be same as that of image 
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2 - 90, img.shape[0]//2 - 40), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)