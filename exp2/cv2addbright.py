import numpy as np
import cv2

img = cv2.imread(r'..\resources\20191014\woman.tif', 0)
#加亮度
img1 = cv2.add(img, 80)
#减亮度
img2 = cv2.subtract(img, 80)
cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
