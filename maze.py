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

def drive(speed: int, reverse: bool, time: int) -> None:
    if(reverse == true):
        speed *= -1
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.run(speed)
    wait(time)
    for motor in [leftFrontM, leftBackM, rightFrontM, rightBackM]:
        motor.stop()

drive(1500, true, 3000)