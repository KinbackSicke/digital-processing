import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.bmp')
'''
高斯模式本质上是一种算术均值滤波，模板中的系数是对某个高斯函数离散化的结果。在OpenCV中可以用 cv2.GaussianBlur()实现。
指定高斯核的宽和高（必须是奇数）。以及高斯函数沿 X，Y 方向的标准差。
如果只指定了 X 方向的标准差，Y 方向也会取相同值。如果两个标准差都是 0，那么函数会根据核函数的大小自己计算。
高斯滤波可以有效的从图像中去除高斯噪声。
'''

Gaussianblur = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(Gaussianblur), plt.title('Gaussian blurred')
plt.xticks([]), plt.yticks([])
plt.show()