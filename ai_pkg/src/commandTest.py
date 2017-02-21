#!/usr/bin/env python

import rospy

from std_msgs.msg import String

if __name__ == '__main__':
    n = 0
    pub = rospy.Publisher('dir', String, queue_size=10)
    rospy.init_node('clientTest', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        if (n % 4 == 0):
            dir = "R U"
        elif (n % 4 == 1):
            dir = "R D"
        elif (n % 4 == 2):
            dir = "L U"
        elif (n % 4 == 3):
            dir = "L D"

        n += 1

        rospy.loginfo(dir)
        pub.publish(dir)
        rate.sleep()
