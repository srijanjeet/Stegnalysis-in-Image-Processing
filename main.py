import cv2 as cv 
import numpy as np
import random
import math
import os




img = cv.imread('./test data for different steganography methods/de/Lena_de_Stego.tif')


img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img)

canny = cv.Canny(img, 125,175) #grabbing the edges of the image using canny edge detector
canny //= 255 #converting the grammer in [0,1] format


sobelx = cv.Sobel(img, -1,1,0)
sobely = cv.Sobel(img, -1,0,1)
sobelxy = cv.addWeighted(sobelx, 0.5 , sobely, 0.5, 0)

laplacian = cv.Laplacian(img, -1)


ret, sobelxy_bw= cv.threshold(sobelxy, 127, 255, cv.THRESH_BINARY)
ret, laplacian_bw = cv.threshold(laplacian, 127, 255, cv.THRESH_BINARY)
  
# converting to its binary form
bw = cv.threshold(sobelxy, 127, 255, cv.THRESH_BINARY)
sobelxy_bw //= 255
bw = cv.threshold(laplacian, 127, 255, cv.THRESH_BINARY)
laplacian_bw //=255

unique, counts = np.unique(sobelxy, return_counts=True)



image_2 =  cv.bitwise_or(canny, sobelxy_bw)
masked_mtrix = cv.bitwise_or(image_2, laplacian_bw )

# print(masked_mtrix)


len_mmtrix = len(masked_mtrix);

s  =  round(random.uniform(0.95, 0.98), 3)
z = random.randint(1, 4)


for i in range (0, len_mmtrix):
    
    for j in range(0, len(masked_mtrix[i])):
        if(masked_mtrix[i][j]==1 ):
            x  = img[i][j] * s
            math.ceil(x)
            if (x>255):
                j = j -1
            else:
                img[i][j]= x
                
        else:
            t = img[i][j] + z
            math.ceil(t)
            if (t>255):
                img [i][j] =img[i][j] -t                
                    
            else:
                img[i][j]= t
                
                
print(img)
            
cv.imshow("newImg",img)

# path = './result data/uniward'
# cv.imwrite(os. path. join(path , 'Peppers_uniward_new.tif'), img)


cv.waitKey(0)



