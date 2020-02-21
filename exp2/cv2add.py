import cv2
import numpy as np
'''
注意：OpenCV 中的加法与Numpy 的加法是有所不同的。OpenCV 的加法
是一种饱和操作，而Numpy 的加法是一种取模操作。

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x + y)
'''
'''
现在把两幅图混合在一起。第一幅图的权重是0.7，第二幅图的权重
是0.3。函数cv2.addWeighted() 可以按下面的公式对图片进行混合操作。
'''
img1 = cv2.imread(r'..\resources\20191014\diamond2.jpg')
img2 = cv2.imread(r'..\resources\20191014\flower2.jpg')
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


