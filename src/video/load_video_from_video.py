import cv2
import os
import numpy as np

CWD = os.getcwd()

cap = cv2.VideoCapture('../../asserts/videos/MVI_1058.avi')

while cap.isOpened():
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
