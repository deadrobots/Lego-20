#!/usr/bin/python

import os, sys
from wallaby import *
import actions as a
import gyroDrive as g
import drive as d
import utils as u
import constants as c


def main():
    a.init()
    c.START_TIME = seconds()
    a.lower_ramp()
    a. move_coupler_to_blocks()
    a.back_to_up_ramp_position()
    set_servo_position(c.LEFT_ARM, c.LA_SIDE)  # fold in left arm
    a.go_up_ramp()
    u.DEBUG()
    d.line_follow_until_switch()
    # u.move_servo(c.RIGHT_ARM, c.RA_DOWN) #lower long arm into pit
    u.wait_for_button()
    a.reverse_and_turn()
    u.DEBUG()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();