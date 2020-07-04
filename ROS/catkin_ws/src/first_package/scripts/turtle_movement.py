#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def mover():
    pub = rospy.Publisher('/turtle1/cmd_vel',Float64MultiArray,queue_size= 10)
    rospy.init_node('mover',anonymous= True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        vel = [2.0, 0.0, 0.0] [0.0, 0.0, 1.8]
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:    
        mover()
    except rospy.ROSInterruptException:
        pass