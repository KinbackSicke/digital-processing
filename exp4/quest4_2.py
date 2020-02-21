import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Fig5.jpg')
#拆分通道
(b, g, r) = cv2.split(img)
#对每个通道做均衡化
b1 = cv2.equalizeHist(b)
g1 = cv2.equalizeHist(g)
r1 = cv2.equalizeHist(r)
#通道合成
result = cv2.merge((b1, g1, r1),)
res = np.hstack((img, result))
cv2.imshow('dst', res)
cv2.waitKey(0)
