import cv2
import numpy as np

cap = cv2.VideoCapture(r'.\resources\20191014\vtest.avi')
font = cv2.FONT_HERSHEY_SIMPLEX
show = True

def show_subs(event, x, y, flags, param):
    global show
    if event == cv2.EVENT_LBUTTONDOWN:
        show = not show

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.resize(gray, (960, 640))
        if show == True:
            cv2.putText(gray, "HELLO OPENCV", (250, 500), font, 1.0, (0, 255, 255), 2)
        cv2.setMouseCallback('frame', show_subs)
        cv2.imshow('frame', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()