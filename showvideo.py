import cv2

#cap = cv2.VideoCapture(r'.\resources\20191014\vtest.avi')
cap = cv2.VideoCapture(r'.\exp2\board.flv')

def click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        cv2.imshow('frame', gray)
        cv2.setMouseCallback('frame', click)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()