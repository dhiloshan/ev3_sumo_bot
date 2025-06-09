#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

"""
has all the functions for EV3 projects
other files will contain a subset of these functions, as not all of them are needed
"""

ev3 = EV3Brick()
leftFrontM = Motor(Port.D, Direction.COUNTERCLOCKWISE)
leftBackM = Motor(Port.C, Direction.CLOCKWISE)
rightFrontM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightBackM = Motor(Port.A, Direction.CLOCKWISE)
frontUS = UltrasonicSensor(Port.S1)
frontCS = ColorSensor(Port.S2)
backCS = ColorSensor(Port.S3)
backGS = GyroSensor(Port.S4)

def drive_time(speed: int, time: int, reverse: bool) -> None:
    if reverse == True:
        speed *= -1

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.run(speed)
    wait(time)

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def drive(speed: int, reverse: bool) -> None:
    if reverse == True:
        speed *= -1

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.run(speed)

def stopMotors() -> None:
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def turn(speed: int, time: int, turnLeft: bool) -> None:
    # turnLeft = True -> left turn
    # turnLeft = False -> right turn
    if turnLeft == False:
        speed *= -1

    for leftMotor in [leftFrontM, leftBackM]:
        leftMotor.run(speed)
    for rightMotor in [rightFrontM, rightBackM]:
        rightMotor.run(-speed)

    wait(time)
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def gyroTurn(speed: int, angle: int, turnLeft: bool):
    # right turn is positive angle
    # left turn is negative angle
    sensor.reset_angle(0)
    
    if turnLeft == False:
        speed *= -1
    
    startAngle = abs(frontGS.angle())

    while abs(frontGS.angle()) - startAngle < angle:
        for leftMotor in [leftFrontM, leftBackM]:
            leftMotor.run(speed)

        for rightMotor in [rightFrontM, rightBackM]:
            rightMotor.run(-speed)

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def detectCollision() -> None: # uses the touch sensor to do something
    if backTS.pressed():
        pass

def stayInBound() -> None: # uses the colour sensor to make sure the robot is in bound
    

while True:

