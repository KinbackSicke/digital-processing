import cv2
import numpy as np
'''
在仿射变换中，图中所有的平行线在结果图像中同样平行。
为了创建这个矩阵，需要从原图像中找到三个点以及它们在输出图像中的位置。
然后    cv2.getAffineTransform 会创建一个2x3 的矩阵，
最后这个矩阵会被传给函数cv2.warpAffine。
'''
img = cv2.imread('drawing.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50, 50], [200, 50],[50, 200]])
pts2 = np.float32([[10, 100], [200, 50],[100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.imwrite('getAffineTransformImg.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
