# blank.shape[1] --> Width
# blank.shape[0] --> Height
#  (0,0) ------ x
#     |
#     |
#     |
#     y

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # 3 --> number of color channels
# cv.imshow('blank', blank)

# # 1. Paint image a certain color
# blank[:] = 0,255,0
# # blank[200:300, 300:450] = 0,255,0 # BGR
# cv.imshow('green', blank)


# 2. Draw Rectangle
cv.rectangle(blank, (0,0),(blank.shape[1]//4, blank.shape[0]), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 3. Draw Circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('circle', blank)

# 4. Draw Line
cv.line(blank, (250,250),(blank.shape[1]//4,0), (255,255,255), thickness=2)
# cv.imshow('line', blank)


# 5. Write Text on Images
cv.putText(blank, "Hello, I'm Sathvik", (150,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)


cv.waitKey(0)
