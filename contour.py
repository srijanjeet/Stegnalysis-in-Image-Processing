import cv2 as cv 
import numpy as np

img = cv.imread('cats.jpg')

cv.imshow('Cats', img)
# print(img)

#creating a blank image
blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Converting it into gray scale image
# print (gray)
# cv.imshow('Gray', gray)

# writing a blur function it will reduce the contours by a significant ammount
blur = cv.GaussianBlur(gray , (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(gray, 125,175) #grabbing the edges of the image using canny edge detector
print(canny)
cv.imshow('Canny images', canny)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #it will return 2 values cv.RETR_list return all contours, 
print(f'contours found {len(contours)}')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
# cv.imshow("blank ", blank)

cv.waitKey(0)






