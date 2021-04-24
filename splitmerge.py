import cv2 as cv # reads in BGR format
import numpy as np

from rescale import rescaleFrame


# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
# cv.imshow('Original_Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)



cv.waitKey(0) 