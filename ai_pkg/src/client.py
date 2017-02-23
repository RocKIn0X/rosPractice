#!/usr/bin/env python

import rospy
from srv_msg_practice_pkg.srv import *
from srv_msg_practice_pkg.msg import *

x_min = 50
x_max = 75
y_min = 50
y_max = 75


def checkCenterX(x):
    return x >= x_min and x <= x_max

def checkCenterY(y):
    return y >= y_min and y <= y_max

def commandControl(x, y):
    global center
    pub = rospy.Publisher('direction', string, queue_size=10)
    rospy.init_node('client', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if (x <= x_min and y <= y_min):
            dir = "R U"
        elif (x <= x_min and y >= y_max):
            dir = "R D"
        elif (x >= x_max and y <= y_min):
            dir = "L U"
        elif (x >= x_max and y >= y_max):
            dir = "L D"
        elif (checkCenterX(x) and checkCenterY(y)):
            dir = "center"
            center = True
        
        rospy.loginfo(dir)
        pub.publish(dir)
        rate.sleep()

if __name__ == '__main__':
    global center 
    center = False
    rospy.init_node('node_client', anonymous=True)
    rospy.wait_for_service('name_service')
    client = rospy.ServiceProxy('name_service', vision_service)
    #print center
    data = client(center)
    data = data.data
    #commandControl(data.x, data.y)
    print "x = " + data.x
    print "y = " + data.y
