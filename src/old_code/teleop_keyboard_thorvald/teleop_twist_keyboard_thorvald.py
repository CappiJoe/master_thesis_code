#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class redirect_twist():
    def __init__(self):
        self.twist_pub = rospy.Publisher('twist_mux/cmd_vel', Twist, queue_size=1) #self.twist_pub if used outside init, queue size = 1 for newest pub.
        rospy.Subscriber("cmd_vel", Twist, self.update_twist) #..Subscriber(Topic, msg_type, callback_funct

    def update_twist(self,twist_sub):
        rospy.loginfo(twist_sub)
        self.twist_pub.publish(twist_sub)
        rospy.loginfo("I can TALK")




    # def send_message(self):
    #     r = rospy.Rate(10)
    #     while not rospy.is_shutdown():
    #         self.twist_pub.publish(self.twist_msg)
    #         rospy.loginfo("I can TALK")
    #         r.sleep() # command that ensures sleep if there is more time in rate after executing code.

if __name__ == '__main__':
    rospy.init_node("redirect", anonymous=True)
    redirect_twist()
    rospy.spin() #Sorger for at noden star og lytter, evt spinonce.
