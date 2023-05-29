import cv2 as cv

#opening images 

img = cv.imread('photo.png')
cv.imshow('Photo', img)

# converting to a gray image

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Photo', gray)

# bBlur image 

# blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
# cv.imshow('Photo', blur)

# Edge Cascade -- displays the edges

# canny = cv.Canny(img, 125,175)
# cv.imshow('Photo', canny)

# dilate the image

# dilate = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Photos', dilate)

# Eroding

# eroded  = cv.erode(dilate, (3,3),iterations=1)
# cv.imshow('Photos', eroded)

# resize

# resize = cv.resize(img, (500,500), interpolation= cv.INTER_LINEAR)
# cv.imshow('Photo', resize)

# cropping 

# cropped = img[50:200 , 200:400]
# cv.imshow('Photo', cropped)



cv.waitKey(0)