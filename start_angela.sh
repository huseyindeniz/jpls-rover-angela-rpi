#!/bin/bash

bash -c "chmod 777 /dev/ttyS0"
bash -c "ssh -R 6900:10.42.0.31:22 angela@192.168.1.37"
bash -i -c "python3 ~/catkin_ws/src/jpls-rover-angela-rpi/angela_locomotion/src/node_steering_motors.py"



