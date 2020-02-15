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
    # a.lower_ramp()
    # a. move_coupler_to_blocks()
    # a.back_to_up_ramp_position()
    # a.go_up_ramp()
    a.go_to_center()
    u.wait_for_button()
    a.reverse_and_turn()
    u.DEBUG()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();