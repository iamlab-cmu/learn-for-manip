# Use this command to launch the control script:
# roslaunch locobot_control main.launch use_camera:=true

# Always use the "Locobot-Lite" configuration
import sys
import time

import numpy as np

from pyrobot import Robot
from pyrobot.utils.util import try_cv2_import
cv2 = try_cv2_import()

def show_camera_output(robot):
    rgb, depth = robot.camera.get_rgb_depth()
    cv2.imshow('Color', rgb[:, :, ::-1])
    cv2.imshow('Depth', depth*10)
    cv2.waitKey(-1)

def camera_checkout(input_args):

    robot = Robot('locobot_lite')

    # Should be center and horizontal
    robot.camera.reset()
    print('Camera state [pan, tilt]: {}'.format(robot.camera.state))
    show_camera_output(robot)

    # Should be poinnted to the left and down
    robot.camera.set_pan_tilt(1., 0.3)
    print('Camera state [pan, tilt]: {}'.format(robot.camera.state))
    show_camera_output(robot)

    # Should be pointed to the right and up
    robot.camera.set_pan_tilt(-1., -0.3)
    print('Camera state [pan, tilt]: {}'.format(robot.camera.state))
    show_camera_output(robot)

    robot.camera.reset()


if __name__ == '__main__':
    camera_checkout(sys.argv[1:])
