#!/usr/bin/env python3

import rospy
#from std_msgs.msg import String
from Lab_2.msg import Num
def talker():
	pub = rospy.Publisher('chatter', Num, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10 hz
	while not rospy.is_shutdown():
		#hello_str = "hello world"
		msg = Num()
		msg.num= 1
		pub.publish(msg)
		rate.sleep()
		
		
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
