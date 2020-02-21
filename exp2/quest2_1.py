import cv2
import numpy as np
import random

bg = cv2.VideoCapture(r'..\resources\20191014\vtest.avi')
#bg = cv2.VideoCapture('board.flv')
#img = cv2.imread('myphoto.jpg')
#img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
front = cv2.VideoCapture('front.flv')
fps = 1
subs = ['opencv', 'dsafs', 'fdsaf', 'fsdfsd']
text = subs[0]

def create_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 设定绿色的阈值
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #开操作消除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # Define the codec and create VideoWriter object
    mask_inv = cv2.bitwise_not(mask)
    return mask, mask_inv

fourcc = cv2.VideoWriter_fourcc(*'MJPG')#  注意编码器
width = int(bg.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(bg.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))
'''
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
while (bg.isOpened() & front.isOpened()):
    ret, frame = bg.read()
    ret2, front_img = front.read()
    if ret:
        fps = fps + 1
        front_img = cv2.resize(front_img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
        rows, cols, channels = front_img.shape
        rows1, cols1, channels1 = frame.shape
        roi = frame[rows1 - rows:rows1, 0:cols]
        mask, mask_inv = create_mask(front_img)
        frame_bg = cv2.bitwise_and(roi, roi, mask=mask)
        frame_fg = cv2.bitwise_and(front_img, front_img, mask=mask_inv)
        dst = cv2.add(frame_bg, frame_fg)
        frame[rows1 - rows:rows1, 0:cols] = dst
        cv2.putText(frame, text, (300, 550), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
        if fps % 24 == 0:
            text = random.choice(subs)
            fps = 1
        out.write(frame)
        cv2.imshow('video', frame)
        k = cv2.waitKey(20)
        if k == 27:
            break

bg.release()
front.release()
out.release()
cv2.destroyAllWindows()