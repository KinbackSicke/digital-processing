import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
#腐蚀与膨胀
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(erosion, cmap='gray')
plt.title('erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dilation, cmap='gray')
plt.title('dilation'), plt.xticks([]), plt.yticks([])
plt.show()