from wallaby import *
import gyroDrive as g
import drive as d
import utils as u
import constants as c


def init():
    print("running init")
    enable_servos()
    print("don't touch me, i'm calibrating!!")
    g.calibrate_gyro()
    # testing motors
    g.drive_timed(30, 1000)
    # pivoting left and right
    g.pivot_on_left_wheel(30, 15)
    g.pivot_on_left_wheel(-30, 15)
    g.pivot_on_right_wheel(30, 15)
    g.pivot_on_right_wheel(-30, 15)
    g.drive_timed(-30, 1000)
    # testing servos
    set_servo_position(c.LEFT_ARM, c.LA_FRONT)
    if c.IS_PRIME:
        print("i am prime")
    else:
        print("i am clone")
    u.wait_for_button()
    g.calibrate_gyro()


def lower_ramp():
    g.drive_distance(60, 18)
    msleep(100)
    set_servo_position(c.LEFT_ARM, c.LA_SIDE)
    msleep(250)
    g.drive_distance(-60, 9)
    msleep(100)


def move_coupler_to_blocks():
    print "move coupler"
    g.pivot_on_left_wheel(50, 100)
    d.line_follow_right(1500)
    msleep(100)
    d.cross_line()
    msleep(50)
    d.line_follow_right_left(4500)
    msleep(100)
    d.set_servo_position(c.LEFT_ARM, c.LA_FRONT)


def back_to_up_ramp_position():
    g.drive_timed(-50, 8500)
    msleep(1000)
    g.pivot_on_right_wheel(50, 90)
    d.drive_timed(50, 50, 2000)
    g.pivot_on_left_wheel(50, 90)


def go_up_ramp():
    d.timed_line_follow_right_smooth(7300)
    msleep(100)
    # at the top of the ramp
    g.drive_distance(-30, 2)
    msleep(100)
    g.turn_with_gyro(0, 50, 90)
    msleep(100)


def reverse_and_turn():
    g.drive_distance(-50, 18)
    g.pivot_on_right_wheel(-30,45)
