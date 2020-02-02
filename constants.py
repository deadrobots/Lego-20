#!/usr/bin/python
# non-changing values

from wallaby import *

# time
START_TIME = 0

# start light
START_LIGHT_THRESHOLD = 50  # this is halfway between light on and light off

# gyro
TURN_CONVERSION = 5400  # subject to change following calibration

# motor ports
RIGHT_MOTOR = 0
LEFT_MOTOR = 3

# servo ports
LEFT_ARM = 0   # placeholder

# analog ports
RIGHT_TOPHAT = 0
LEFT_TOPHAT = 1
START_LIGHT = 5     # placeholder

# digital ports
CLONE_SWITCH = 1    # placeholder
RIGHT_BUTTON = 13
LEFT_BUTTON = 14
ARM_SWITCH = 0

# prime/clone
IS_CLONE = digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE

# sensor values
ON_BLACK = 2000

# servo arm values
LA_BACK = 1900
LA_FRONT = 0
LA_SIDE = 1300