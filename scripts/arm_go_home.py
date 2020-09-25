# Always use the "Locobot-Lite" configuration
import sys

import numpy as np
from pyrobot import Robot

def arm_go_home(input_args):

    robot = Robot('locobot_lite')
    success = robot.arm.go_home()
    return success

if __name__ == '__main__':
    arm_go_home(sys.argv[1:])
