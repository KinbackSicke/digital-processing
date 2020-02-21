import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
使用OpenCV 统计直方图函数cv2.calcHist统计一幅图像的直方图。该函数和它的参数如下：
cv2:calcHist(images; channels; mask; histSize; ranges[; hist[; accumulate]])
images: 原图像（图像格式为uint8 或float32）。当传入函数时应该用中括号[] 括起来，例如：[img]。
channels: 同样需要用中括号括起来，它会告诉函数我们要统计那幅图像的直方图。
        如果输入图像是灰度图，它的值就是[0]；如果是彩色图像的话，传入的参数可以是[0]，[1]，[2]，分别对应着通道B，G，R。
mask: 掩模图像。要统计整幅图像的直方图就把它设为None。但是如果只需统计图像某一部分的直方图，就需要制作一个掩模图像。
histSize:BIN 的数目。也应该用中括号括起来，例如：[32], [128], [256]。
ranges: 像素值范围，通常为[0，256]
'''
'''
img = cv2.imread('flower.jpg', 0)
#hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#使用Numpy 统计直方图Numpy 中的函数np.histogram() 也可以帮我们统计直方图。可以尝试如下代码：
#hist, bins = np.histogram(img.ravel(), 256, [0, 256])

cv2.imshow('img', img)
#img.ravel() 将图像转成一维数组，这里没有中括号。
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

from matplotlib import pyplot as plt
img = cv2.imread('flower.jpg')
color = ('b','g','r')
# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置enumerrate 函数会有更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
