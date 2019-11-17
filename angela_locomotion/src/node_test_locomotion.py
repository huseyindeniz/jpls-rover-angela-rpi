#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32, Float64
# joystick'e subscribe ol
# steering ve drive'a publish et

class TestLocomotion(object):

    def __init__(self):
        rospy.init_node('node_test_locomotion')
        rospy.loginfo('node_test_locomotion started')
        self._init_drive_motors_publisher()
        self._init_steering_publisher()
        self._init_joystick_subscriber()

    def _init_joystick_subscriber(self):
        self._joystick_sub = rospy.Subscriber("/angela/joy", Joy, self._joystick_message_received)

    def _init_drive_motors_publisher(self):
        self._drive_motors_pub = rospy.Publisher('/angela/drive_motors', Int32, queue_size=1)

    def _init_steering_publisher(self):
        self._steering_pub = rospy.Publisher('/angela/steering', Int32, queue_size=1)

    def _joystick_message_received(self, data):
        steering_angle = - round(data.axes[0] * 25)
        self._steering_pub.publish(steering_angle)
        drive_speed = round(data.axes[1] * 3000)
        self._drive_motors_pub.publish(drive_speed)

if __name__ == '__main__':
    testLocomotionObj = TestLocomotion()
    rate = rospy.Rate(10)
    rate.sleep()
    rospy.spin()
