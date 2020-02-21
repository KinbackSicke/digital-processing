import cv2
import numpy as np

img = cv2.imread('blue2.jpg')
#img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#转换到HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 设定蓝色的阈值
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#开操作消除噪声
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#draw = cv2.drawContours(img.copy(), contours, 0, (0, 0, 255), 3)
x, y, w, h = cv2.boundingRect(mask)
'''
参数：
img  是一个二值图
x，y 是矩阵左上点的坐标，
w，h 是矩阵的宽和高
'''
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#对原图像和掩模进行位运算
res = cv2.bitwise_and(img, img, mask=mask)
#cv2.imshow('hsv', hsv)
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
