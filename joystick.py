#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16

def callback(msg):
    if msg.axes[1]==1:   #forward
        ct=1
    elif msg.axes[0]==-1:  #right
        ct=2
    elif msg.axes[0]==1:   #left
        ct=3
    elif msg.axes[1]==-1:   #backward
        ct=4
    else:                    #stop
        ct=0

    pub1.publish(ct)



if __name__ == '__main__':
    try:
        global pub
        rospy.init_node('joyROS', anonymous=True)
        pub1 = rospy.Publisher("motion" , Int16 , queue_size=10)
        rospy.Subscriber("joy",Joy, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass