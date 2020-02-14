#!/usr/bin/python
# non-changing values

from wallaby import *
# digital ports
CLONE_SWITCH = 1    # placeholder
RIGHT_BUTTON = 13
LEFT_BUTTON = 14
ARM_SWITCH = 0

# prime/clone
IS_CLONE = digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE

# time
START_TIME = 0

# gyro
TURN_CONVERSION = 5400  # subject to change following calibration

# motor ports
RIGHT_MOTOR = 0
LEFT_MOTOR = 3

# servo ports
LEFT_ARM = 0
FRONT_ARM = 1
FRONT_CLAW = 2

# analog ports
RIGHT_TOPHAT = 0
LEFT_TOPHAT = 1
START_LIGHT = 5     # placeholder

if IS_PRIME:  # Red Lego
    # sensor values
    ON_BLACK = 2000

    # servo arm values
    LA_BACK = 1750
    LA_FRONT = 0
    LA_SIDE = 1400

    FA_DOWN = 1600 # to edit
    FA_MID = 600  # Ground on flat surface to edit
    FA_UP = 0

    FC_OPEN = 1400
    FC_CLOSED = 800
else:  # IS_CLONE (Yellow Lego)
    # sensor values
    ON_BLACK = 2000

    # servo arm values
    LA_BACK = 1850
    LA_FRONT = 100
    LA_SIDE = 1550

    FA_DOWN = 1600
    FA_MID = 600  # Ground on flat surface
    FA_UP = 0

    FC_OPEN = 1400
    FC_CLOSED = 800

