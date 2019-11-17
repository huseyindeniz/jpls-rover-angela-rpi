#!/usr/bin/env python3

from adafruit_servokit import ServoKit
import roslibpy
from time import sleep

FRONT_LEFT = 5
FRONT_RIGHT = 9
BACK_LEFT = 7
BACK_RIGHT = 11

FRONT_LEFT_REF = 150
FRONT_RIGHT_REF = 155
BACK_LEFT_REF = 45
BACK_RIGHT_REF = 125

class SteeringMotors(object):
    def __init__(self):
        self._rosClient = roslibpy.Ros(host='localhost', port=9090)
        self._rosClient.run()
        print('Is ROS connected?', self._rosClient.is_connected)
        self._listener = roslibpy.Topic(self._rosClient, '/angela/steering', 'std_msgs/Int32')
        self._listener.subscribe(lambda message: self._commandReceived(message))

        self._servoKit = ServoKit(channels=16)
        self.go_to_default_positions()

    def _commandReceived(self, message):
        angle = message['data']
        if angle <= 25 and angle >= -25:
            self.turn(angle)
        else:
            print("angle should be between -25 and 25")

    def go_to_default_positions(self):
        self._servoKit.servo[FRONT_LEFT].angle = FRONT_LEFT_REF
        self._servoKit.servo[FRONT_RIGHT].angle = FRONT_RIGHT_REF
        self._servoKit.servo[BACK_LEFT].angle = BACK_LEFT_REF
        self._servoKit.servo[BACK_RIGHT].angle = BACK_RIGHT_REF

    def turn(self, angle):
        self._servoKit.servo[FRONT_LEFT].angle = FRONT_LEFT_REF + angle
        self._servoKit.servo[FRONT_RIGHT].angle = FRONT_RIGHT_REF + angle
        self._servoKit.servo[BACK_LEFT].angle = BACK_LEFT_REF - angle
        self._servoKit.servo[BACK_RIGHT].angle = BACK_RIGHT_REF - angle       

if __name__ == '__main__':
    steeringMotors = SteeringMotors()
    while True:
        pass