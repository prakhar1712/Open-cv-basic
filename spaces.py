import cv2 as cv
import numpy as np

# open cv uses BGR format of images but matplotlib and others uses RGB as default way

#opening images 

img = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', img)

img[200:400] = 0,255,0
cv.imshow('Green', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# BGR to GRAY

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to l*a*b

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)