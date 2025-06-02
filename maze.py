#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
leftFrontM = Motor(Port.A, Direction.CLOCKWISE)
leftBackM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightFrontM = Motor(Port.C, Direction.CLOCKWISE)
rightBackM = Motor(Port.D, Direction.COUNTERCLOCKWISE)

def drive(speed: int, time: int, reverse: bool) -> None:
    if(reverse == True):
        speed *= -1

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.run(speed)
    wait(time)

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def turn(speed: int, tim`e: int, turnLeft: bool) -> None:
    # turnLeft = True -> left turn
    # turnLeft = False -> right turn
    if(turnLeft == False):
        speed *= -1

    for leftMotor in [leftFrontM, leftBackM]:
        leftMotor.run(speed)
    for rightMotor in [rightFrontM, rightBackM]:
        rightMotor.run(-speed)

    wait(time)
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

# 1050 is the max speed
turn(1050, 4000, True) # perfect 90 degree turn