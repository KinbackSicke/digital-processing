import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.bmp')
'''
前面的滤波器都是用计算得到的一个平均值来取代中心像素的值，而中值滤波一种统计滤波器，采用中位数来取代模板中原点对应位置的值。
'''

blur3 = cv2.medianBlur(img, 3)
blur5 = cv2.medianBlur(img, 5)
blur7 = cv2.medianBlur(img, 7)
blur7 = cv2.Sobel(blur7, -1, 1, 1, ksize=5)
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur3), plt.title('blurred 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur5), plt.title('blurred 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur7), plt.title('blurred 7*7')
plt.xticks([]), plt.yticks([])
plt.show()