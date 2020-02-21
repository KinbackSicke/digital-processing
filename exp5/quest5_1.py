import cv2
import numpy as np


#实现卷积
def convolve(img, kernel):
    height = kernel.shape[0]
    width = kernel.shape[1]
    conv_height = img.shape[0] - kernel.shape[0] + 1
    conv_width = img.shape[1] - kernel.shape[1] + 1

    conv = np.zeros((conv_height, conv_width), np.uint8)
    for i in range(conv_height):
        for j in range(conv_width):
            res = (img[i:i + height, j:j + width] * kernel).sum()
            if res < 0:
                res = 0
            elif res > 255:
                res = 255
            conv[i][j] = res
    return conv


img  = cv2.imread('lena.bmp', 0)
kernel = np.ones((5, 5), np.float32) / 25
conv = convolve(img, kernel)
cv2.imshow('img', img)
cv2.imshow('conv', conv)
cv2.waitKey(0)
cv2.destroyAllWindows()