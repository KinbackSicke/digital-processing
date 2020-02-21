import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(1):
    # 获取每一帧
    ret,frame = cap.read()
    #print(ret)
    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((50, 50), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #draw = cv2.drawContours(frame.copy(), contours, 0, (0, 0, 255), 3)

    # 做出矩形边界
    x, y, w, h = cv2.boundingRect(mask)
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break
# 关闭窗口
cv2.destroyAllWindows()


