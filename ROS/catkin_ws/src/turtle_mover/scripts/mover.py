# #!/usr/bin/env python

# import rospy
# from geometry_msgs.msg import Twist
# from std_msgs.msg import String

# def talker():
#     # speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
#     # rospy.init_node('speed', anonymous=True)

#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz

#     counter = 0 

#     while not rospy.is_shutdown():
#         # twist = Twist()
#         # vector1 = [twist.linear.x = 2.0,twist.linear.y = 0.0,twist.linear.z = 0.0]
#         # vector2 =  [twist.angular.x = 0.0,twist.angular.y = 0.0,twist.angular.z = 1.8]
#         # twist.linear.x = 2.0
#         # twist.linear.y = 0.0
#         # twist.linear.z = 0.0
#         # twist.angular.x = 0.0
#         # twist.angular.y = 0.0
#         # twist.angular.z = 1.8
        
#         hello_str = "hello world %s" % counter

#         # rospy.loginfo(twist)
#         # speed_pub.publish(twist)

#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)

#         rate.sleep()
#         counter +=1
#         # rospy.spin()
        

# if __name__ == '__main)__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    counter = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % counter
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        counter += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
