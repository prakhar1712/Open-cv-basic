import cv2 as cv
import numpy as np

#opening images 

img = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', img)

img[200:400] = 0,255,0
cv.imshow('Green', img)

# Translation 

# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions  = (img.shape[1],img.shape[0])

#     return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y -->up
# x -->right
# y -->down

# translated = translate(img,100,100)
# cv.imshow('Photo',translated)

# rotation 

# def rotate(img, angle, rotPoint = None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotaMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions = (width,height)

#     return cv.warpAffine(img,rotaMat,dimensions)

# rotated = rotate(img,45)
# cv.imshow('Roatated', rotated)

# 45 is rotated clockwise
# -45 is rotated anticlockwise

# flipping the image

flip = cv.flip(img,0)
cv.imshow('Flip', flip)

 # 0  -- flipped horizontally
 # -1 -- flipped vertically
  
cv.waitKey(0)