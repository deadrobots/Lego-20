#!/usr/bin/python
# motor tick driving

from wallaby import *
import utils as u
import constants as c
import gyroDrive as g


def drive(left_speed, right_speed):
    motor(c.LEFT_MOTOR, left_speed)
    motor(c.RIGHT_MOTOR, right_speed)


def drive_timed(left_speed, right_speed, time):
    motor(c.LEFT_MOTOR, left_speed)
    motor(c.RIGHT_MOTOR, right_speed)
    msleep(time)
    ao()


def tick_drive(left_speed, right_speed, time):
    if left_speed > 1400:
        print("speed too fast. please pick a number under 1401.")
        left_speed = 1400
    if right_speed > 1400:
        print("speed too fast. please pick a number under 1401.")
        right_speed = 1400
    mav(c.LEFT_MOTOR, left_speed)
    mav(c.RIGHT_MOTOR, right_speed)
    msleep(time)


def sleep(time):
    drive_timed(0, 0, time)


#######################################
# line follow functions

def on_black_left():
    return analog(c.LEFT_TOPHAT) > c.ON_BLACK


def on_black_right():
    return analog(c.RIGHT_TOPHAT) > c.ON_BLACK


def on_white_left():
    return analog(c.LEFT_TOPHAT) < c.ON_BLACK


def on_white_right():
    return analog(c.RIGHT_TOPHAT) < c.ON_BLACK

def cross_line():
    drive(0, 40)
    while on_white_right():
        pass
    msleep(20)
    while on_black_right():
        pass
    drive(0, 0)


def line_follow_until_switch():
    while digital(c.ARM_SWITCH) == 0:
        if on_black_right():
            drive_timed(90, 70, 20)
        else:
            drive_timed(70, 90, 20)
    freeze(c.LEFT_MOTOR)
    freeze(c.RIGHT_MOTOR)


def line_follow_left(time):
    sec = seconds()
    while seconds() - sec < time/1000.0:
        if on_black_left():
            drive(40, 70)    # drive values may need to be changed
        else:
            drive(70, 40)    # drive values may need to be changed
    drive(0, 0)


def line_follow_right(time):
    sec = seconds()
    while seconds() - sec < time/1000.0:
        if on_black_right():
            drive(70, 40)    # drive values may need to be changed
        else:
            drive(40, 70)    # drive values may need to be changed
    drive(0, 0)


def line_follow_right_left(time):
    sec = seconds()
    while seconds() - sec < time/1000.0:
        if on_black_right():
            drive(40, 70)    # drive values may need to be changed
        else:
            drive(70, 40)    # drive values may need to be changed
    drive(0, 0)


def timed_line_follow_left(time):
    sec = seconds() + time/1000.0
    while seconds() < sec:
        if on_black_left():
            drive_timed(20, 90, 20)
        else:
            drive_timed(90, 20, 20)
        msleep(10)


def timed_line_follow_left_smooth(time):
    sec = seconds() + time/1000.0
    while seconds() < sec:
        if on_black_left():
            drive_timed(20, 40, 20)
        else:
            drive_timed(40, 20, 20)
        msleep(10)


def timed_line_follow_right(time):
    sec = seconds() + time/1000.0
    while seconds() < sec:
        if on_black_right():
            drive_timed(90, 20, 20)
        else:
            drive_timed(20, 90, 20)
        msleep(10)


def timed_line_follow_right_smooth(time):
    sec = seconds() + time/1000.0
    while seconds() < sec:
        if on_black_right():
            drive_timed(80, 60, 20)
        else:
            drive_timed(60, 80, 20)
        msleep(10)


def timed_proportional_line_follow_right(time):
    sec = seconds() + time/1000.0
    while seconds() < sec:
        if analog(c.RIGHT_TOPHAT) < 200:
            motor(c.LEFT_MOTOR, 30)
            motor(c.RIGHT_MOTOR, 100)
        elif analog(c.RIGHT_TOPHAT) < 800:
            motor(c.LEFT_MOTOR, 60)
            motor(c.RIGHT_MOTOR, 80)
        elif analog(c.RIGHT_TOPHAT) < 1400:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 80)
        elif analog(c.RIGHT_TOPHAT) < 2000:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 60)
        else:
            motor(c.LEFT_MOTOR, 100)
            motor(c.RIGHT_MOTOR, 30)
    ao()


#######################################
# square up functions

def drive_till_black(tophat, speed):
    while analog(tophat) < c.ON_BLACK:
        drive(speed, speed)


def square_up_black(left_speed, right_speed):   # drives till black then squares up
    while left_speed != 0 or right_speed != 0:
        if on_black_left():
            left_speed = 0
        if on_black_right():
            right_speed = 0
        drive(left_speed, right_speed)


def square_up_white(left_speed, right_speed):   # drives till black then squares up
    while left_speed != 0 or right_speed != 0:
        if on_white_left():
            left_speed = 0
        if on_white_right():
            right_speed = 0
        drive(left_speed, right_speed)


#######################################
# loop break timers


TIME = 0  # this represents how long to wait before breaking a loop.


def set_wait(delay):  # sets wait time in seconds before breaking a loop.
    global TIME
    TIME = seconds() + delay


def get_wait():  # used to break a loop after using "setWait"
    return seconds() < TIME
