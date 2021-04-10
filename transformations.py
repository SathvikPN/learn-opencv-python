""" Basic Opencv Transformations """
import cv2 as cv
from rescale import rescaleFrame
import numpy as np


# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
cv.imshow('Original_Image', img)

# 1.Translation 
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # Width,Height
    return cv.warpAffine(img, transMat, dimensions)

    # y --> shift down    -y --> up
    # x --> shift right   -x --> left


translated = translate(img, -100,-100)
# cv.imshow('Translated', translated)



# 2.Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -45)
# cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated,-45)
# cv.imshow('Rotated_Rotated', rotated_rotated)


# 3.Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)


# 4.Flipping
flip = cv.flip(img,-1)
# cv.imshow('Flipped',flip) 
# 0 --> over x axis
# 1 --> y axis
# -1 --> both x and y


# 5.Cropping
cropped = img[200:300, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)