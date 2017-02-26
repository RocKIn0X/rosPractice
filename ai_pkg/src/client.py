#!/usr/bin/env python

import rospy
from srv_msg_practice_pkg.srv import *
from srv_msg_practice_pkg.msg import *
from std_msgs.msg import String

x_min = 300
x_max = 350
y_min = 225
y_max = 275


def checkCenterX(x):
    return x >= x_min and x <= x_max

def checkCenterY(y):
    return y >= y_min and y <= y_max

def commandControl(x, y):
    global center
    dir = ""
    
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
    pub = rospy.Publisher('direction', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        while not center:
            rospy.wait_for_service('name_service')
            client = rospy.ServiceProxy('name_service', vision_service)
            #print center
            data = client(center)
            data = data.data
            commandControl(data.x, data.y)
            print ("x = %s , y = %s")%(data.x, data.y)
