#!/usr/bin/env python

import rospy
from srv_msg_pkg.srv import *
from srv_msg_pkg.msg import *
from std_msgs.msg import String

float x_min = 50
float x_max = 75
float y_min = 50
float y_max = 75

bool center = False

def checkCenterX(x):
    return x >= x_min and x <= x_max

def checkCenterY(y):
    return y >= y_min and y <= y_max

def commandControl(x, y):
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
    rospy.init_node('node_client', anonymous=True)
    rospy.wait_for_service('vision_srv')
    client = rospy.ServiceProxy('vision_srv', vision)
    print center
    data = client(center)
    data = data.data
    commandControl(data.x, data.y)
