import cv2
import numpy as np
# import cv2.cv as cv

lower_black = np.array([0,0,0])
upper_black = np.array([255,100,60])
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    black = cv2.inRange(hsv, lower_black, upper_black)
    cv2.imshow('img_show', black)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindow()