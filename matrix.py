import cv2 as cv 
import numpy as np

img = cv.imread('Lena_de_Stego.tif')

canny = cv.Canny(img, 125,175) #grabbing the edges of the image using canny edge detector
canny //= 255 #converting the grammer in [0,1] format

x = len(canny)
print(canny)
cv.imshow("canny",canny)

cv.waitKey(0)



