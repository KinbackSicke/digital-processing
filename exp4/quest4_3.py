import cv2
import numpy as np


def histRegular(img_source, img_result):
    img_reg = img_source.copy()
    rows, cols, channels = img_source.shape
    for i in range(channels):
        hist1, bins = np.histogram(img_reg[:, :, i].ravel(), 256, [0, 256])
        hist2, bins = np.histogram(img_result[:, :, i].ravel(), 256, [0, 256])
        #计算累积分布
        cdf1 = hist1.cumsum()
        cdf2 = hist2.cumsum()
        cdf1_hist = hist1.cumsum() / cdf1.max()  # 灰度值的累计值的比率
        cdf2_hist = hist2.cumsum() / cdf2.max()
        #累积分布的差值
        diff_cdf = [[0 for j in range(256)] for k in range(256)]
        for j in range(256):
            for k in range(256):
                diff_cdf[j][k] = abs(cdf1_hist[j] - cdf2_hist[k])
        #构建灰度级映射表
        lut = [0 for j in range(256)]
        for j in range(256):
            min = diff_cdf[j][0]
            index = 0
            #查找源灰度级为j的映射灰度
            #和j的累积概率差值最小的规定化灰度index
            for k in range(256):
                if min > diff_cdf[j][k]:
                    min = diff_cdf[j][k]
                    index = k
            lut[j] = ([j, index])

        for j in range(rows):
            for k in range(cols):
                img_reg[j, k, i] = lut[img_reg[j, k, i]][1]
    return img_reg

img_src = cv2.imread('Fig7A.jpg')
img_res = cv2.imread('Fig7B.jpg')
img_histr = histRegular(img_src, img_res)

cv2.imshow('src', img_src)
cv2.imshow('img_res', img_res)
cv2.imshow('img_histr', img_histr)
cv2.waitKey(0)
cv2.destroyAllWindows()