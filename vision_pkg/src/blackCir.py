#!/usr/bin/env python

import cv2
import numpy as np
import rospy
from srv_msg_practice_pkg.srv import vision_service
from srv_msg_practice_pkg.msg import vision_position
# import cv2.cv as cv

# flatten = lambda l: [item for sublist in l for item in sublist]
lower_red = np.array([0,100,150])
upper_red = np.array([15,255,255])
lower_red1 = np.array([165,100,150])
upper_red1 = np.array([180,255,255])
cap = cv2.VideoCapture(0)

def callback(req):
    res = vision_position()
    if not(req.isDetected):
        while(True):
            ret, frame = cap.read()

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            red = cv2.inRange(hsv, lower_red, upper_red)
            red1 = cv2.inRange(hsv, lower_red1, upper_red1)
            realRed = red1
            # cv2.imshow('img_show', black)
            # gray = cv2.cvtColor(black, cv2.COLOR_HSV2GRAY)
            
            rett, thresh = cv2.threshold(realRed, 127, 255, cv2.THRESH_BINARY)

            circles = cv2.HoughCircles(realRed,cv2.HOUGH_GRADIENT,4,60,
                                    param1=100,param2=150,minRadius=90,maxRadius=120)


            print(circles)
            # circles = np.unint(np.around(circles))
            if not(circles == None):
                print(type(circles))
                
                circleList = circles.tolist()[:2]
                print circleList
                res.x = circleList[0][0][0]
                res.y = circleList[0][0][1]
                print res.x
                print res.y
                cap.release()
                # cv2.destroyAllWindow()
                return res 
            
                # for i in circles[0,:]:
                #     # draw the outer circle
                #     cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                #     # draw the center of the circle
                #     cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

                
            # cv2.imshow('red_img', realRed)
            # cv2.imshow('img_show', frame)
            # cv2.imshow('tresh', thresh)
            # cv2.imshow('img_show', black)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindow()

if __name__ == '__main__':
    rospy.init_node('node_service', anonymous=True)
    try:
        service = rospy.Service('name_service', vision_service, callback)
        rospy.spin()
    except rospy.ServiceException, e:
        print "Service call failed: %s" %e