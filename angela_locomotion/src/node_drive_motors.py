#!/usr/bin/env python
from driver_roboclaw import Roboclaw
from std_msgs.msg import Int32
import rospy

BACK_ADDRESS = 0x80
MIDDLE_ADDRESS = 0x81
FRONT_ADDRESS = 0x82

ACCELERATION = 1000

class DriveMotors(object):

    def __init__(self):
        rospy.init_node('node_drive_motors')
        rospy.loginfo('node_drive_motors started')
        self._init_roboclaw()
        self._init_drive_motors_subscriber()

    def _init_roboclaw(self):
        self._roboclaw = Roboclaw("/dev/ttyS0", 38400)
        self._roboclaw.Open()

    def _init_drive_motors_subscriber(self):
        self._drive_motors_sub = rospy.Subscriber("/angela/drive_motors", Int32, self._command_received)

    def _command_received(self, message):
        speed = message.data
        self._roboclaw.SpeedAccelM1(FRONT_ADDRESS, ACCELERATION, -speed)
        self._roboclaw.SpeedAccelM2(FRONT_ADDRESS, ACCELERATION, speed)
        self._roboclaw.SpeedAccelM1(MIDDLE_ADDRESS, ACCELERATION, -speed)
        self._roboclaw.SpeedAccelM2(MIDDLE_ADDRESS, ACCELERATION, speed)
        self._roboclaw.SpeedAccelM1(BACK_ADDRESS, ACCELERATION, -speed)
        self._roboclaw.SpeedAccelM2(BACK_ADDRESS, ACCELERATION, speed)

if __name__ == '__main__':
    driveMotorsObj = DriveMotors()
    rate = rospy.Rate(10)
    rate.sleep()
    rospy.spin()