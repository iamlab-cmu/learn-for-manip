# Always use the "Locobot-Lite" configuration
import time
import numpy as np
from pyrobot import Robot

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

displacement_zneg = np.array([0, 0, -0.15])
print('Moving arm +z.')
robot.arm.move_ee_xyz(displacement_zneg, plan=False)
time.sleep(1)

displacement_zpos = np.array([0, 0, 0.15])
print('Moving arm -z.')
robot.arm.move_ee_xyz(displacement_zpos, plan=False)
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
