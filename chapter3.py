# Croping and Resizing Images
import cv2
import numpy as np

img = cv2.imread('resources/lambo.png')
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
imgResize2 = cv2.resize(img, (1000, 500))

imgCropped = img[0:400, 100:200]

cv2.imshow("Image", img)
# cv2.imshow("Image Resized", imgResize)
# cv2.imshow("Image Resized Bigger", imgResize2)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)