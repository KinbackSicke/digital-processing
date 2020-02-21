import cv2
import numpy as np

#OpenCV 中的直方图均衡化函数为cv2.equalizeHist()。这个函数的输入图片仅仅是一副灰度图像，输出结果是直方图均衡化之后的图像。
img = cv2.imread('Fig5.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imwrite('hist.jpg', res)
cv2.waitKey(0)
cv2.destroyAllWindows()