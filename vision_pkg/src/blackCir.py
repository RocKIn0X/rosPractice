import cv2
import numpy as np
# import cv2.cv as cv

lower_black = np.array([0,0,0])
upper_black = np.array([255,150,60])
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    black = cv2.inRange(hsv, lower_black, upper_black)
    # cv2.imshow('img_show', black)
    # gray = cv2.cvtColor(black, cv2.COLOR_HSV2GRAY)

    circles = cv2.HoughCircles(black,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=50)
    # circles = np.unint(np.around(circles))
    if not(circles == None):
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('img_show', frame)
    # cv2.imshow('img_show', black)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindow()