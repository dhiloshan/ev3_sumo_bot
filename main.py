#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math, random

ev3 = EV3Brick()
leftFrontM = Motor(Port.D, Direction.COUNTERCLOCKWISE)
leftBackM = Motor(Port.C, Direction.CLOCKWISE)
rightFrontM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightBackM = Motor(Port.A, Direction.CLOCKWISE)
frontUS = UltrasonicSensor(Port.S1)
frontCS = ColorSensor(Port.S2)
backCS = ColorSensor(Port.S3)
backTS = TouchSensor(Port.S4)

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

def turnTime(speed: int, time: int, turnLeft: bool) -> None:
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

def turn(speed: int, turnLeft: bool) -> None:
    # turnLeft = True -> left turn
    # turnLeft = False -> right turn
    if turnLeft == False:
        speed *= -1

    for leftMotor in [leftFrontM, leftBackM]:
        leftMotor.run(speed)
    for rightMotor in [rightFrontM, rightBackM]:
        rightMotor.run(-speed)

def stopMotors() -> None:
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

while True:
    # drive(1050, False)   
    turn(1050, False)

    curDist = frontUS.distance()
    if 0 < curDist < 350:
        stopMotors()

        while frontCS.color() == Color.BLACK and backCS.color() == Color.BLACK:
            drive(1050, False)
            wait(50)
        
        stopMotors()  
        drive_time(1050, 3200, True)
        turnTime(1050, random.randint(2800, 3800), True)

    if frontCS.color() != Color.BLACK:
        stopMotors()
        drive_time(1050, 4500, True)
        turnTime(1050, random.randrange(1400, 2800), True)
    
    if backCS.color() != Color.BLACK:
        stopMotors()
        drive_time(1050, 4500, False)
        turnTime(1050, random.randrange(1400, 2800), False)

    if backTS.pressed(): # there is a robot behind our robot
        stopMotors()
        
        while frontCS.color() == Color.BLACK and backCS.color() == Color.BLACK:
            drive(1050, True)
            wait(50)
        
        stopMotors()  
        drive_time(1050, 3200, False)
        turnTime(1050, random.randint(2800, 3800), True)