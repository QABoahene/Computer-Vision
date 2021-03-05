import cv2 as cv

sample_sneaker_img = cv.imread('sneaker_dataset/images/train/Jordan 1 Retro High Rookie of the Year/5.jpg')
cv.imshow('Air Jordan 1 High', sample_sneaker_img)

''' A function to take the frame to be resized by a 
scale value. Works for images, videos and live videos!'''
def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)



resized_sneaker_img = rescale_frame(sample_sneaker_img)
cv.imshow('Image', resized_sneaker_img)

cv.waitKey(0)