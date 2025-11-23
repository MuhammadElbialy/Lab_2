#!/usr/bin/env python3

import rospy
#from std_msgs.msg import String
from Lab_2.msg import Num

def callback(data):
	print ("I heard " + str(data.num))
	
	
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", Num, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	
if __name__ == '__main__':
 	listener()
