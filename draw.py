import numpy as np 
import cv2 as cv

#Creating a dummy/blank image to work with alternatively
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank Image', blank)

# Paint the image in a certain colour
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

sneaker_sample_img = cv.imread('sneaker_dataset/images/train/Jordan 1 Retro High Rookie of the Year/5.jpg')
cv.imshow('Air Jordan 1 High', sneaker_sample_img)

#Paint the sneaker image
sneaker_sample_img[100:700, 300:400] = 0, 0, 255
cv.imshow('Red Rectangle', sneaker_sample_img)

cv.waitKey(0)