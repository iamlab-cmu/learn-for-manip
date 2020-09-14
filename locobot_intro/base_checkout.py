# Always use the "Locobot-Lite" configuration
import time
import numpy as np
from pyrobot import Robot

base_config_dict={'base_controller': 'movebase'}
robot = Robot('locobot_lite', base_config=base_config_dict)

# Reset
robot.arm.go_home()

# Turn in place
target_position = [0.0, 0.0, 1.5707] # rotate on-spot by 90 degrees
robot.base.go_to_relative(target_position, smooth=False, close_loop=True)
time.sleep(1)

# Move a bit
target_position = [1.0, 1.0, 0.0] 
robot.base.go_to_relative(target_position, smooth=False, close_loop=True)
time.sleep(1)
