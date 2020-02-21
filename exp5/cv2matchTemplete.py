import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
模板匹配是用来在一副大图中搜寻查找模版图像位置的方法。
OpenCV 为我们提供了函数：cv2.matchTemplate()。
和 2D 卷积一样，它也是用模板图像在输入图像（大图）上滑动，
并在每一个位置对模板图像和与其对应的输入图像的子区域进行比较。
OpenCV 提供了几种不同的比较方法（细节请看文档）。
返回的结果是一个灰度图像，每一个像素值表示了此区域与模板的匹配程度。
'''

img = cv2.imread('lena.bmp', 0)
img2 = img.copy()
templete = cv2.imread('eye.png', 0)
w, h = templete.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    # eval 语句用来计算存储在字符串中的有效 Python 表达式
    method = eval(meth)
res = cv2.matchTemplate(img, templete, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# 使用不同的比较方法，对结果的解释不同
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, 255, 2)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(meth)
plt.show()
