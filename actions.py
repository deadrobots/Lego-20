from wallaby import *
import gyroDrive as g
import drive as d
import utils as u
import constants as c


def init():
    if c.IS_PRIME:
        print("I am lego prime")
    else:
        print("I am lego clone")
    print("running init")
    enable_servos()
    print("don't touch me, i'm calibrating!!")
    g.calibrate_gyro()

    #power_on_test()

    u.move_servo(c.LEFT_ARM, c.LA_FRONT)
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)

    # for start at top of ramp
    # u.move_servo(c.LEFT_ARM, c.LA_SIDE)
    # u.move_servo(c.FRONT_ARM, c.FA_UP)
    # u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)

    u.wait_for_button()
    c.START_TIME = seconds()


def power_on_test():
    # testing servos
    print("testing front arm")
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    u.move_servo(c.FRONT_ARM, c.FA_MID)
    u.move_servo(c.FRONT_ARM, c.FA_UP)
    print("testing claw")
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)
    u.move_servo(c.FRONT_CLAW, c.FC_OPEN)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)
    print("testing left arm")
    u.move_servo(c.LEFT_ARM, c.LA_FRONT)
    u.move_servo(c.LEFT_ARM, c.LA_BACK)
    u.move_servo(c.LEFT_ARM, c.LA_FRONT)
    #testing switch
    u.wait_for_switch(c.ARM_SWITCH)
    # testing motors
    print("testing motors")
    g.drive_timed(30, 1000)
    # pivoting left and right
    g.pivot_on_left_wheel(30, 15)
    g.pivot_on_left_wheel(-30, 15)
    g.drive_timed(-30, 1000)
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


def lower_ramp():
    g.drive_distance(60, 23)
    msleep(100)
    set_servo_position(c.LEFT_ARM, c.LA_SIDE)  #grab coupler
    msleep(250)
    g.drive_condition(-60, d.on_white_left)
    msleep(100)
    d.square_up_black(-50, -50)
    msleep(100)


def move_coupler_to_blocks():
    print "move coupler"
    g.turn_with_gyro(-60, 60, 90)
    msleep(100)
    g.drive_distance(-50, 6)
    g.drive_condition(60, d.on_white_left)
    u.move_servo(c.FRONT_CLAW, c.FC_OPEN, 100)
    u.move_servo(c.FRONT_ARM, c.FA_COUPLER_DOWN, 100)
    g.drive_distance(60, 21)
    msleep(50)
    d.set_servo_position(c.LEFT_ARM, c.LA_FRONT)


def back_to_up_ramp_position():
    g.drive_timed(-90, 5200)  # square up
    msleep(100)
    u.move_servo(c.LEFT_ARM, c.LA_BACK, 100)
    u.move_servo(c.FRONT_ARM, c.FA_UP, 100)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED, 100)
    if c.IS_PRIME:
        msleep(50)
        g.pivot_on_right_wheel(70, 95)  # 90
    else:
        # g.drive_distance(70, 0.5)
        msleep(50)
        g.pivot_on_right_wheel(70, 92)
    g.drive_distance(70, 17)
    g.drive_distance(-70, 4)
    g.pivot_on_left_wheel(50, 95)  # 90
    g.drive_distance(70, 2)
    set_servo_position(c.LEFT_ARM, c.LA_RAMP_SIDE)  # fold in left arm


def go_up_ramp():
    d.timed_line_follow_right_smooth(7500)
    # at the top of the ramp
    g.drive_distance(-90, 2)
    g.turn_with_gyro(0, 75, 82)
    u.move_servo(c.FRONT_ARM, c.FA_MID)


def grab_poms():
    #g.drive_distance(100, 2)
    d.line_follow_until_switch()
    g.drive_distance(-65, 3) #4
    u.move_servo(c.FRONT_ARM, c.FA_DOWN1)
    u.move_servo(c.FRONT_CLAW, c.FC_OPEN_BIN, 5)
    g.drive_distance(50, .6)
    u.move_servo(c.FRONT_ARM, c.FA_DOWN2, 5)
    g.drive_distance(50, 1)
    u.move_servo(c.FRONT_ARM, c.FA_DOWN3, 5)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED_BIN, 5)
    u.move_servo(c.FRONT_ARM, c.FA_DOWN2, 3)
    g.drive_distance(-50, .9)
    u.move_servo(c.FRONT_ARM, c.FA_DOWN1, 3)
    g.drive_distance(-50, .6)
    u.move_servo(c.FRONT_ARM, c.FA_MID, 3)


def deliver_poms():
    g.drive_distance(-65, 7)
    g.turn_with_gyro(-70, 50, 76)
    g.drive_distance(-30, 0.5)  # 2
    u.move_servo(c.FRONT_ARM, c.FA_SMOOSH_DOWN, 5)
    u.move_servo(c.FRONT_CLAW, c.FC_COUPLER_OPEN + 60, 20)
    d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 175)
    d.drive_timed(c.WIGGLE_SPEED, -c.WIGGLE_SPEED, 350)
    d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 350)
    d.drive_timed(c.WIGGLE_SPEED, -c.WIGGLE_SPEED, 350)
    d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 175)
    u.move_servo(c.FRONT_CLAW, c.FC_OPEN, 20)
    u.move_servo(c.FRONT_ARM, c.FA_SMOOSH_UP)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED_BIN)
    u.move_servo(c.FRONT_ARM, c.FA_SMOOSH_DOWN)
    #u.move_servo(c.FRONT_CLAW, c.FC_COUPLER_OPEN + 60, 20)
    # d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 175)
    # d.drive_timed(c.WIGGLE_SPEED, -c.WIGGLE_SPEED, 350)
    # d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 350)
    # d.drive_timed(c.WIGGLE_SPEED, -c.WIGGLE_SPEED, 350)
    # d.drive_timed(-c.WIGGLE_SPEED, c.WIGGLE_SPEED, 175)
    #u.move_servo(c. FRONT_CLAW, c.FC_OPEN )



def smoosh_poms():
    u.move_servo(c.FRONT_ARM, c.FA_SMOOSH_UP)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED_BIN + 85, 5)
    u.move_servo(c.FRONT_ARM, c.FA_SMOOSH_DOWN, 6)


def return_to_poms():
    u.move_servo(c.FRONT_ARM, c.FA_MID)
    u.move_servo(c.FRONT_CLAW, c.FC_CLOSED)
    g.turn_with_gyro(70, -50, 88)    # 90
    g.drive_distance(-50, 4)
    msleep(100)







