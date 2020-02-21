import cv2
import numpy as np
from matplotlib import pyplot as plt

#理想低通滤波器
img = cv2.imread('test2.jpg', 0)
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
#创建中间为1周围为0的掩膜
mask = np.zeros((rows, cols), np.uint8)
mask[crow - 30: crow + 30, ccol - 30: ccol + 30] = 1
fshift = dft_shift * mask
#逆变换
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Img After LPF'), plt.xticks([]), plt.yticks([])
plt.show()
