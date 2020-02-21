import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
现在我们可以进行频域变换了，我们就可以在频域对图像进行一些操作了，
例如高通滤波和重建图像（DFT 的逆变换）。
比如我们可以使用一个60x60 的矩形窗口对图像进行掩模操作从而去除低频分量。
然后再使用函数np.fft.ifftshift() 进行逆平移操作，所以现在直流分量又回到左上角了，
左后使用函数 np.ifft2() 进行 FFT 逆变换。
'''

img = cv2.imread('test2.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
fshift[crow - 30: crow + 30, ccol - 30: ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Input After HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Image In JET'), plt.xticks([]), plt.yticks([])
plt.show()