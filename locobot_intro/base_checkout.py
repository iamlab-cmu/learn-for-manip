# Use this command to launch the control script:
# roslaunch locobot_control main.launch use_base:=true base:=create

# Always use the "Locobot-Lite" configuration
import sys
import time

import numpy as np

from pyrobot import Robot

def base_checkout(input_args):

    # Warn the user
    user_response = raw_input("The robot base is about to move. Is the area clear? (Y/n): ")
    if user_response and user_response.lower() != 'y':
        print("Invalid response. Exiting.")
        return False

    # This controller may not be the best for all applications
    # Please revisit the choice of base controller for other applications
    base_config_dict={'base_controller': 'movebase'}
    robot = Robot('locobot_lite', base_config=base_config_dict)

    # Turn in place
    target_position = [0., 0., 1.5707] # rotate on-spot by 90 degrees
    print('Turning in place.')
    robot.base.go_to_relative(
        target_position, smooth=False, close_loop=True
    )
    time.sleep(1)

    odom_state = robot.base.get_state('odom')
    print('Current position from odometry [x/y/yaw]: {}'.format(odom_state))
    time.sleep(1)

    # Turn in place
    target_position = [0., 0., -1.5707] # rotate on-spot by 90 degrees
    print('Turning in place.')
    robot.base.go_to_relative(
        target_position, smooth=False, close_loop=True
    )
    time.sleep(1)

    odom_state = robot.base.get_state('odom')
    print('Current position from odometry [x/y/yaw]: {}'.format(odom_state))
    time.sleep(1)

    # Move a bit
    target_position = [0.25, 0., 0.]
    print('Moving base forward.')
    robot.base.go_to_relative(
        target_position, smooth=False, close_loop=True
    )
    time.sleep(1)

    odom_state = robot.base.get_state('odom')
    print('Current position from odometry [x/y/yaw]: {}'.format(odom_state))
    time.sleep(1)

if __name__ == '__main__':
    base_checkout(sys.argv[1:])
