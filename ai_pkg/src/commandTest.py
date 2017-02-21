#!/usr/bin/env python

import rospy

from std_msgs.msg import String

if __name__ == '__main__':
    pub = rospy.Publisher('direction', string, queue_size=10)
    rospy.init_node('client', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        int n = 0;

        if (n % 4 == 0):
            dir = "R U"
        elif (n % 4 == 1):
            dir = "R D"
        elif (n % 4 == 2):
            dir = "L U"
        elif (n % 4 == 3):
            dir = "L D"

        n++;

        rospy.loginfo(dir)
        pub.publish(dir)
        rate.sleep()
