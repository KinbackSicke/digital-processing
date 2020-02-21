import cv2
import numpy as np
from matplotlib import pyplot as plt


def HPF_filter(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    fshift[crow - 30: crow + 30, ccol - 30: ccol + 30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def LPF_filter(img):
    # 理想低通滤波器
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    # 创建中间为1周围为0的掩膜
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - 30: crow + 30, ccol - 30: ccol + 30] = 1
    fshift = dft_shift * mask
    # 逆变换
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def DPF_filter(img):
    #带通滤波器
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    x, y = crow // 2, ccol // 2
    # 创建中间为1周围为0的掩膜
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - x:crow + x, ccol - y:ccol + y] = 1
    mask[crow - x + 30:crow + x + 30, ccol - y - 30:ccol + y + 30] = 0
    fshift = dft_shift * mask
    # 逆变换
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back


img = cv2.imread('child.jpg', 0)
print(img.shape[0], img.shape[1])
b = HPF_filter(img)
g = DPF_filter(img)
r = LPF_filter(img)
img_bgr = cv2.imread('child.jpg')
img_bgr[:, :, 0] = b
img_bgr[:, :, 1] = g
img_bgr[:, :, 2] = r
cv2.imshow('res', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
plt.subplot(131), plt.imshow(b, cmap='gray')
plt.title('Input After HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(g, cmap='gray')
plt.title('Input After DPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(r, cmap='gray')
plt.title('Input After LPF'), plt.xticks([]), plt.yticks([])
plt.show()
'''



