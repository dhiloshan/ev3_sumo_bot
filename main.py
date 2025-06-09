#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
sensor = GyroSensor(Port.S4)

while True:
    ev3.screen.clear()
    curAngle = sensor.angle()      # returns an int
    ev3.screen.draw_text(0, 50, curAngle)
    ev3.speaker.beep()
    wait(500)