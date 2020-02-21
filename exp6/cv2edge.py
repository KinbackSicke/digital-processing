import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('house.tif', 0)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

dilate = cv2.dilate(img, element)
erode = cv2.erode(img, element)

result = cv2.absdiff(dilate, erode)
#上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
#反色，即对二值图每个像素取反
result = cv2.bitwise_not(result)
#显示图像
cv2.imshow('result', result)
cv2.waitKey(0)