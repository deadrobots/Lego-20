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
    print("testing motors")
    g.drive_timed(30, 1000)
    # pivoting left and right
    g.pivot_on_left_wheel(30, 15)
    g.pivot_on_left_wheel(-30, 15)
    g.drive_timed(-30, 1000)
    if c.IS_PRIME:
        print("i am lego prime")
    else:
        print("i am lego clone")
    # testing servos
    print("testing left arm")
    u.move_servo(c.LEFT_ARM, c.LA_FRONT)
    u.move_servo(c.LEFT_ARM, c.LA_BACK)
    u.move_servo(c.LEFT_ARM, c.LA_FRONT)
    print("testing front arm")
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    u.move_servo(c.FRONT_ARM, c.FA_MID)
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    print("testing left arm")
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)
    u.move_servo(c.FRONT_CLAW, c.FC_OPEN)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)
    # testing tophat
    print("testing right tophat")
    g.drive_condition(50, d.on_white_right)
    msleep(500)
    print("see black")
    g.drive_condition(50, d.on_black_right)
    msleep(500)
    print("see white")
    g.drive_timed(50, 500)
    print("testing left tophat")
    g.drive_condition(-50, d.on_white_left)
    msleep(500)
    print("see black")
    g.drive_condition(-50, d.on_black_left)
    msleep(500)
    print("see white")
    g.drive_timed(-50, 500)
    u.wait_for_button()
    # g.calibrate_gyro()


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
