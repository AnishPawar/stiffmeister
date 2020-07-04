#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist

def talker():
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', String, queue_size=10)
    rospy.init_node('speed', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 2.0
        twist.angular.z = 1.8
        


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
