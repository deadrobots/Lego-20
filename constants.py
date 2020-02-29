#!/usr/bin/python
# non-changing values

from wallaby import *
# digital ports
CLONE_SWITCH = 1    # placeholder
RIGHT_BUTTON = 13
LEFT_BUTTON = 14
ARM_SWITCH = 0

#motor speeds
WIGGLE_SPEED = 10

# prime/clone
IS_CLONE = digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE

# time
START_TIME = 0


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

    # servo values
    LA_BACK = 1750
    LA_FRONT = 0
    LA_SIDE = 1400
    LA_RAMP_SIDE = 1100

    FA_DOWN1 = 1300
    FA_DOWN2 = 1500
    FA_DOWN3 = 1900     # 1700
    FA_DROP = 950
    FA_MID = 400  # ground on flat surface
    FA_UP = 0
    FA_COUPLER_DOWN = 1000
    FA_SMOOSH_UP = 950
    FA_SMOOSH_DOWN = 1200
    FA_KNOCK = 820
    FA_UNDER_BRIDGE = 780

    FC_OPEN = 1350
    FC_CLOSED = 500
    FC_OPEN_BIN = 1020
    FC_CLOSED_BIN = 100 # 430
    FC_COUPLER_OPEN = 625  # 625

  #5400
else:  # IS_CLONE (Yellow Lego)
    # sensor values
    ON_BLACK = 2000

    # servo values
    LA_BACK = 1850
    LA_FRONT = 350
    LA_SIDE = 1550
    LA_RAMP_SIDE = 1250

    FA_DOWN1 = 1300
    FA_DOWN2 = 1500
    FA_DOWN3 = 1700
    FA_DROP = 950
    FA_MID = 600  # Ground on flat surface
    FA_UP = 200
    FA_COUPLER_DOWN = 850
    FA_SMOOSH_UP = 950
    FA_SMOOSH_DOWN = 1200
    FA_KNOCK = 820
    FA_UNDER_BRIDGE = 780


    FC_OPEN = 1850
    FC_CLOSED = 800
    FC_OPEN_BIN = 1050
    FC_CLOSED_BIN = 0
    FC_COUPLER_OPEN = 660



