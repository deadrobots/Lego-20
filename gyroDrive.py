#!/usr/bin/python
# driving using gyro for increased accuracy

from wallaby import *
import math
import constants as c
import utils as u


bias = 0
addition_factor = 1.920137e-16
multiplication_factor = 0.000004470956


if c.IS_PRIME:
    INCHES_TO_TICKS = 200   # subject to change
else:
    INCHES_TO_TICKS = 217   # subject to change


def _clear_ticks():
    clear_motor_position_counter(c.RIGHT_MOTOR)
    clear_motor_position_counter(c.LEFT_MOTOR)


def _freeze_motors():
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)


def calibrate_gyro():
    i = 0
    avg = 0
    while i < 100:
        avg += gyro_z()
        msleep(1)
        i += 1
    global bias
    bias = avg/i
    msleep(60)


#######################################
# drive functions
# the drive functions use the change in gyro_z to adjust wheel speeds and drive straight

def _drive(speed):
    # calibrate_gyro()
    theta = 0
    while True:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
        else:
            motor(c.RIGHT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (gyro_z() - bias) * 10
    _freeze_motors()


def _drive_left_right(left_speed, right_speed, theta=0):
    # calibrate_gyro()
    if right_speed > 0:
        motor(c.RIGHT_MOTOR, int((right_speed - right_speed * (addition_factor + multiplication_factor*theta))))
        motor(c.LEFT_MOTOR, int((left_speed + left_speed * (addition_factor + multiplication_factor*theta))))
    else:
        motor(c.RIGHT_MOTOR, int((right_speed + right_speed * (addition_factor + multiplication_factor*theta))))
        motor(c.LEFT_MOTOR, int((left_speed - left_speed * (addition_factor + multiplication_factor*theta))))
    msleep(10)


def drive_timed(speed, time):
    # print("driving for time")
    # calibrate_gyro()
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time/1000.0:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
        else:
            motor(c.RIGHT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (gyro_z() - bias) * 10
    _freeze_motors()


def drive_timed_left_right(left_speed, right_speed, time):
    # calibrate_gyro()
    # print("driving for time")
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time/1000.0:
        if left_speed > 0:
            motor(c.RIGHT_MOTOR, int((right_speed - right_speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((left_speed + left_speed * (addition_factor + multiplication_factor*theta))))
        else:
            motor(c.RIGHT_MOTOR, int((right_speed + right_speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((left_speed - left_speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (gyro_z() - bias) * 10
    _freeze_motors()


def drive_distance(speed, distance):
    # calibrate_gyro()
    _clear_ticks()
    # print("driving for distance")
    theta = 0
    while abs((get_motor_position_counter(c.RIGHT_MOTOR) + get_motor_position_counter(c.LEFT_MOTOR))/2) < distance * INCHES_TO_TICKS:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
        else:
            motor(c.RIGHT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor*theta))))
            motor(c.LEFT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (gyro_z() - bias) * 10
    _freeze_motors()


def drive_condition(speed, test_function, state=True):  # needs some work
    # this function was written by Charlie, the 2019 season captain
    # calibrate_gyro()
    # print("Driving while condition is inputted state")
    theta = 0
    while test_function() is state:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor * theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor * theta))))
        else:
            motor(c.RIGHT_MOTOR, int((speed + speed * (addition_factor + multiplication_factor * theta))))
            motor(c.LEFT_MOTOR, int((speed - speed * (addition_factor + multiplication_factor * theta))))
        msleep(10)
        theta += (gyro_z() - bias) * 10
    _freeze_motors()


#######################################
# pivot functions
# all of these turn/pivots measure the change gyro_z to make the turn or pivot more excact

def turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("turning")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta += abs(gyro_z() - bias) * 10
    # print(theta)
    _freeze_motors()


def pivot_on_left_wheel(right_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("pivoting on left")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, 0)
        msleep(10)
        theta += abs(gyro_z() - bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)
    _freeze_motors()


def pivot_on_right_wheel(left_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("pivoting on right")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, 0)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta += abs(gyro_z() - bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)
    _freeze_motors()
