#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# ports are reversed
ev3 = EV3Brick()
leftFrontM = Motor(Port.D, Direction.COUNTERCLOCKWISE)
leftBackM = Motor(Port.C, Direction.CLOCKWISE)
rightFrontM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightBackM = Motor(Port.A, Direction.CLOCKWISE)
frontUS = UltrasonicSensor(Port.S1)
frontCS = ColorSensor(Port.S2)
backCS = ColorSensor(Port.S3)

def drive(speed: int, reverse: bool) -> None:
    if(reverse == True):
        speed *= -1

    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.run(speed)

def stopMotors() -> None:
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

def turn(speed: int, time: int, turnLeft: bool) -> None:
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

while True:
    drive(1050, False)
    frontDist = frontUS.distance()
    if frontDist < 180:
        stopMotors()
        wait(300)
        turn(1050, 4000, True)
        leftDist = frontUS.distance()

        wait(300)
        turn(1050, 8000, False)
        rightDist = frontUS.distance()

        if leftDist > rightDist:
            turn(1050, 8000, True) # turn leftward since it is positioned rightward