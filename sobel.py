import cv2 as cv
import numpy as np

img = cv.imread('Lena_de_Stego.tif')
# img = cv.imread('dog.jpg')
img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow("img", img)

sobelx = cv.Sobel(img, -1,1,0)
sobely = cv.Sobel(img, -1,0,1)
sobelxy = cv.addWeighted(sobelx, 0.5 , sobely, 0.5, 0)

laplacian = cv.Laplacian(img, -1)


ret, bw_img = cv.threshold(sobelxy, 127, 255, cv.THRESH_BINARY)
  
# converting to its binary form
# bw = cv.threshold(sobelxy, 127, 255, cv.THRESH_BINARY)
bw_img //= 255

# print(np.unique(bw_img))
print(bw_img)
print(sobelxy)

unique, counts = np.unique(sobelxy, return_counts=True)
# print(np.asarray((unique, counts)).T)



# cv.imshow("Sobelx" ,sobelx)
# cv.imshow("Sobely" ,sobely)
# cv.imshow("Sobelx" ,sobelxy)
# cv.imshow("Laplacian" ,laplacian)

# print(sobelxy)
# print(laplacian)

# print(np.unique(laplacian))
cv.waitKey(0)


