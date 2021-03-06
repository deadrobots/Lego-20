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
    a.lower_ramp()
    a.move_coupler_to_blocks()
    a.back_up_around_blocks()
    a.back_to_up_ramp_position()
    a.go_up_ramp()
    a.grab_poms()
    a.deliver_poms()
    a.smoosh_poms()
    a.return_to_poms()
    a.second_grab_poms()
    a.deliver_poms()
    a.smoosh_poms()
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    a.get_back_down_from_ramp()
    a.get_back_to_coupler()
    a.return_to_start()
    u.DEBUG()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();