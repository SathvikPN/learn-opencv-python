import cv2 as cv

from rescale import rescaleFrame
# Original BGR Image
original_img = cv.imread('Photos/cert.png')
img = rescaleFrame(original_img,0.4)
cv.imshow('Original_Image', img)


# pixels window -------------
# # #
# #C #
# # #


# Averaging of surrounding pixels' intensity for center pixel
average = cv.blur(img, (7,7)) # pixel window size 3X3 that slides in matrix fashion
cv.imshow('Average Blur',average)

# Gaussian Blur (more natural blur)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur (good for noise reduction)
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur',median)

# Bilateral (retains edges)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)