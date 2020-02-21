import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.bmp')
'''
可以使用函数 cv2.blur() 和 cv2.boxFilter() 来完均值滤波任务。
与filter2D不同的是，我们需要设定卷积窗口的尺寸（宽和高），即可进行卷积处理。
'''

blur3 = cv2.blur(img, (3, 3))
blur5 = cv2.blur(img, (5, 5))
blur7 = cv2.blur(img, (7, 7))
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur3), plt.title('blurred 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur5), plt.title('blurred 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur7), plt.title('blurred 7*7')
plt.xticks([]), plt.yticks([])
plt.show()