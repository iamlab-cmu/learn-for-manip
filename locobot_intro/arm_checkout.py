# Use this command to launch the control script:
# roslaunch locobot_control main.launch use_arm:=true

# Always use the "Locobot-Lite" configuration
import sys
import time

import numpy as np

from pyrobot import Robot

def arm_checkout(input_args):

    # Warn the user
    user_response = raw_input("The robot arm is about to move. Is the area clear? (Y/n): ")
    if user_response and user_response.lower() != 'y':
        print("Invalid response. Exiting.")
        return False

    robot = Robot('locobot_lite')

    # Reset
    print('Setting arm to home.')
    robot.arm.go_home()

    # Go to joins
    target_joints = [
            [0.408, 0.721, -0.471, -1.4, 0.920],
            [-0.675, 0, 0.23, 1, -0.70]
        ]

    for joint in target_joints:
        print('Going to joint config: {}'.format(joint))
        robot.arm.set_joint_positions(joint, plan=False)
        time.sleep(1)
        joint_sense = robot.arm.get_joint_angles()
        print('Current joint config: {}'.format(joint_sense))
        time.sleep(1)

    # EE control
    print('Setting arm to home.')
    robot.arm.go_home()
    time.sleep(1)

    current_ee_pose = robot.arm.pose_ee
    current_ee_pos = current_ee_pose[0]
    current_ee_rot = current_ee_pose[1]
    print('Current ee (end-effector) position: {}'.format(current_ee_pos.T))
    print('Current ee (end-effector) orientation: \n{}'.format(current_ee_rot))

    use_planner = False

    displacement_zneg = np.array([0, 0, -0.1])
    print('Moving arm -z.')
    robot.arm.move_ee_xyz(displacement_zneg, plan=use_planner)
    time.sleep(1)

    displacement_zpos = np.array([0, 0, 0.1])
    print('Moving arm +z.')
    robot.arm.move_ee_xyz(displacement_zpos, plan=use_planner)
    time.sleep(1)

    print('Setting arm to home.')
    robot.arm.go_home()
    time.sleep(1)

    # Gripper control
    print('Opening gripper.')
    robot.gripper.open()
    time.sleep(1)

    print('Closing gripper.')
    robot.gripper.close()
    time.sleep(1)

    print('Opening gripper.')
    robot.gripper.open()
    time.sleep(1)

if __name__ == '__main__':
    arm_checkout(sys.argv[1:])
