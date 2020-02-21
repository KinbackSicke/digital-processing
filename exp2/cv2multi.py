import numpy as np
import cv2
'''
两幅图像进行乘法运算可以实现掩模操作，即屏蔽掉图像的某些部分。
一幅图像乘以一个常数通常被称为缩放，这是一种常见的图像处理操作。
如果使用的缩放因子大于1，那么将增强图像的亮度，如果因子小于1则会使图像变暗。
缩放通常将产生比简单添加像素偏移量自然得多的明暗效果，
这是因为这种操作能够更好地维持图像的相关对比度。
两幅图像进行乘法运算可以实现掩模操作，即屏蔽掉图像的某些部分。
一幅图像乘以一个常数通常被称为缩放，这是一种常见的图像处理操作。
如果使用的缩放因子大于1，那么将增强图像的亮度，如果因子小于1则会使图像变暗。
缩放通常将产生比简单添加像素偏移量自然得多的明暗效果，这是因为这种操作能够更好地维持图像的相关对比度。
'''


img = cv2.imread(r'..\resources\20191014\woman.tif', 0)
rols, cols = img.shape
img1 = cv2.multiply(img, 2)
img3 = cv2.multiply(img, img)
cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()