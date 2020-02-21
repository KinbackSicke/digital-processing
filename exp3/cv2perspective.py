import cv2
import numpy as np

'''
对于视角变换，需要一个3x3 变换矩阵。
在变换前后直线还是直线。要构建这个变换矩阵，需要在输入图像上找4 个点，以及他们在输出图像上对应的位置。
这四个点中的任意三个都不能共线。
这个变换矩阵可以由函数cv2.getPerspectiveTransform() 构建。
然后把这个矩阵传给函数cv2.warpPerspective。
'''

img = cv2.imread('news.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (600, 800))
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.imwrite('getPerspectiveTransformImg.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
