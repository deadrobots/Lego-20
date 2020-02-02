#!/usr/bin/python
# start light and servo functions

from wallaby import *
import constants as c
import gyroDrive as g
import threading as t


def drive(left_speed, right_speed):
    motor(c.LEFT_MOTOR, left_speed)
    motor(c.RIGHT_MOTOR, right_speed)


def drive_timed(left_speed, right_speed, time):
    motor(c.LEFT_MOTOR, left_speed)
    motor(c.RIGHT_MOTOR, right_speed)
    msleep(time)
    ao()


def sleep(time):
    drive_timed(0, 0, time)


def wait_for_button():
    print("Press Right Button...")
    while not digital(c.RIGHT_BUTTON):
        pass
    msleep(1)
    print("Pressed")
    msleep(1000)


def DEBUG():
    freeze(c.LEFT_MOTOR)
    freeze(c.RIGHT_MOTOR)
    print('Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME)
    ao()
    exit(0)


def DEBUG_with_wait():
    freeze(c.LEFT_MOTOR)
    freeze(c.RIGHT_MOTOR)
    print ('Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME)
    ao()
    msleep(5000)


#######################################
# start light functions

def calibrate(port):
    print("Press LEFT button with light on")
    while not left_button():
        pass
    while left_button():
        pass
    light_on = analog(port)
    print("On value =", light_on)
    if light_on > 200:
        print("Bad calibration")
        return False
    msleep(1000)
    print("Press RIGHT button with light off")
    while not right_button():
        pass
    while right_button():
        pass
    light_off = analog(port)
    print("Off value =", light_off)
    if light_off < 3000:
        print("Bad calibration")
        return False

    if (light_off - light_on) < 2000:
        print("Bad calibration")
        return False
    c.startLightThresh = (light_off - light_on) / 2
    print("Good calibration! ", c.START_LIGHT_THRESHOLD)
    return True


def wait_4(port):
    print("waiting for light!! ")
    while analog(port) > c.START_LIGHT_THRESHOLD:
        pass


def wait_4_light(ignore=False):
    if ignore:
        wait_for_button()
        return
    while not calibrate(c.START_LIGHT):
        pass
    wait_4(c.START_LIGHT)


#######################################
# servo functions

def move_servo(servo, end_position, speed=10):
    now = get_servo_position(servo)
    if now > 2047:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > end_position:
        speed = -speed
    for i in range(now, end_position, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, end_position)
    msleep(10)


def motor_calibration():
    move_servo(c.SERVO_ARM, c.ARM_UP)
    msleep(1000)
    g.calibrate_gyro()
    print("Distance calibration:")
    print("Place the robot square against some wall or edge, then")
    wait_for_button()
    g.drive_distance(99, 30)
    g.drive_timed(0, 0)
    print("Measure distance traveled.")
    print("If greater than 30 inches, decrease inches-to-ticks value in gyroDrive")
    print("If less than 30 inches, increase inches-to-ticks value")
    print("---")
    wait_for_button()
    print("Turning calibration:")
    print("Orient the robot parallel to a tape line")
    wait_for_button()
    g.turn_with_gyro(60, -60, 180)
    g.drive_timed(0, 0)
    msleep(100)
    print("If robot overturns, decrease turn_conversion in constants.")
    print("If robot underturns, increase turn_conversion in constants.")
    DEBUG()


def thread_servo(servo, pos, speed):    # do we need this?
    x = lambda: move_servo(servo, pos, speed)
    t.Thread(name='daemon', target=x).start()


def thread_anything(funk, *args, **kwargs):     # do we need this?
    x = lambda: funk(*args, **kwargs)
    t.Thread(name='daemon', target=x).start()
