import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('jerode.png', 0)
img2 = cv2.imread('jdilate.png', 0)

kernel = np.ones((5, 5), np.uint8)
#开操作
open = cv2.morphologyEx(img1, cv2.MORPH_OPEN ,kernel)
#闭操作
close  = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

plt.subplot(221), plt.imshow(img1, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(open, cmap='gray')
plt.title('opening'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img2, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(close, cmap='gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])
plt.show()