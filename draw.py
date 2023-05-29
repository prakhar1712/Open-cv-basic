import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a ceratin color 

# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# we used the entire array inorder to color the entire image so we can choose to color a certain part of the image
# by slicing the array

# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# drawing  a rectangle using the rectangle property

# cv.rectangle(blank, (0,0) , (250,250),(0,255,0),thickness= 4)
# cv.imshow('Rectangle', blank)

# inorder to fill the color in the image we use 


# cv.rectangle(blank, (0,0) , (250,250),(0,255,0),thickness= cv.FILLED)
# cv.imshow('Rectangle', blank)

# inorder to draw circle

# cv.circle(blank, (250,250), radius=100, color=(0,255,0) , thickness=cv.FILLED)
# cv.imshow('Circle', blank)

# draw a line on a image

# cv.line(blank, (230,230) , (400,400) , color=(0,255,0), thickness=3)
# cv.imshow('Line', blank)

# write on the image

cv.putText(blank,'hello world', (240,203), cv.FONT_HERSHEY_TRIPLEX,1.0, color=(0,255,0),thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
