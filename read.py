import cv2 as cv

#opening images 

# img = cv.imread('photo.png')
# cv.imshow('Photo', img)
# cv.waitKey(0)

#opening videos presaved

# capture = cv.VideoCapture("video.mp4")
# while True:
#     isTrue , frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyWindow()

# opening the live webcam

# capture = cv.VideoCapture(0)
# while True:
#     isTrue , frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyWindow()

# resizing the image and videos

# def rescaleFrame(frame,scale = 0.7):

#     width = int(frame.shape[1] * scale)
#     heigth = int(frame.shape[0] * scale)

#     dimensions = (width,heigth)

#     return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

# #Reading the video
# capture = cv.VideoCapture("video.mp4")

# while True:
#     isTrue , frame = capture.read()
#     frame_resized = rescaleFrame(frame)

#     # cv.imshow('Video', frame)
#     cv.imshow('Video Rezied', frame_resized)
    


#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyWindow()

# resizing the live videos 
# this doesnt work on the existing vidoes and images 

# def changeres(width,height):

#     capture.set(3,width)
#     capture.set(4,height)



