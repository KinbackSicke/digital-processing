import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
首先我们看看如何使用 Numpy 进行傅里叶变换。Numpy 中的 FFT 包可以帮助我们实现快速傅里叶变换。
函数 np.fft.fft2()可以对信号进行频率转换，输出结果是一个复数数组。
本函数的第一个参数是输入图像，要求是灰度格式。第二个参数是可选的, 决定输出数组的大小。
如果输出结果比输入图像大，输入图像就需要在进行 FFT 前补0。
如果输出结果比输入图像小的话，输入图像就会被切割。
现在我们得到了结果，频率为 0 的部分（直流分量）在输出图像的左上角。
如果想让它（直流分量）在输出图像的中心，我们还需要将结果沿两个方向平移N/2。
函数 np.fft.ifftshift() 可以帮助我们实现这一步。进行完频率变换之后，就可以构建振幅谱了。
'''

img = cv2.imread('test2.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#构建振幅
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude spectrum'), plt.xticks([]), plt.yticks([])
plt.show()