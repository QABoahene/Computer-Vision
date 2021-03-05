#Importing OpenCV model
import cv2 as cv

'''The function 'imread()' takes in a path to an image 
and retuns that image as a matrix or pixels'''
sample_sneaker_img = cv.imread('sneaker_dataset/images/train/Jordan 1 Retro High Off-White White/5.jpg')

#show image
cv.imshow('Air Jordan 1 High', sample_sneaker_img)

cv.waitKey(0)