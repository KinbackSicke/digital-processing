import cv2
import numpy as np

pts1 = np.zeros((4, 2), np.float32)
#pts2 = np.zeros((4, 2), np.float32)
pts2 = np.float32([[0, 0], [0, 800], [500, 800], [500, 0]])
clickTime = 0


def torectangle(event, x, y, flags, param):
    global clickTime, pts1, pts2
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x, y)
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('image', img)
        pts1[clickTime] = [x, y]
        clickTime += 1
        if clickTime == 4:
            clickTime = 0
            M = cv2.getPerspectiveTransform(pts1, pts2)
            dst = cv2.warpPerspective(img, M, (400, 600))
            cv2.imshow('perspective', dst)

cv2.namedWindow('image')
img = cv2.imread('news.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
#img = np.zeros((500, 500, 3), np.float32)
cv2.imshow('image', img)
cv2.setMouseCallback('image', torectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
