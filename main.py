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
    a.go_up_ramp()
    set_servo_position(c.LEFT_ARM, c.LA_SIDE)
    d.line_follow_until_switch()
    u.DEBUG()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();