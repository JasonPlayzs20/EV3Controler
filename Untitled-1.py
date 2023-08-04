#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
Motor_1 = Motor(Port.B)
Motor_2 = Motor(Port.C)

#arm motors
Motor_3 = Motor(Port.A)
Motor_4 = Motor(Port.D)

SonicSens = UltrasonicSensor(Port.S1)
# GyroSens = GyroSensor(Port.S2)
ColourSens1 = ColorSensor(Port.S3)
ColourSens2 = ColorSensor(Port.S2)

def LineFollowR(color):
    while True:
        if (ColourSens2.color() == Color.BLACK):
            Motor_1.run(270)
            Motor_2.run(300)
        elif (ColourSens2.reflection() > 50 and ColourSens2.reflection() < 65):
            Motor_1.run(300)
            Motor_2.run(270)
        if (ColourSens1.color() == color):
            Motor_1.run(0)
            Motor_2.run(0)
            break
        if ColourSens1.color() == Color.BLACK and ColourSens2.color() == Color.BLACK: 
            Motor_1.run(0)
            Motor_2.run(0)
            break

def LineFollowL(color):
    while True:
        if (ColourSens1.color() == Color.BLACK):
            Motor_1.run(300)
            Motor_2.run(270)
        elif (ColourSens1.reflection() > 50 and ColourSens1.reflection() < 65):
            Motor_1.run(270)
            Motor_2.run(300)
        if (ColourSens2.color() == color):
            Motor_1.run(0)
            Motor_2.run(0)
            break
        if ColourSens1.color() == Color.BLACK and ColourSens2.color() == Color.BLACK: 
            Motor_1.run(0)
            Motor_2.run(0)
            break

def turn(dir): 
    if dir == "right": 
        Motor_1.run(100)
        Motor_2.run(-100) 
    else: 
        Motor_1.run(-100)
        Motor_2.run(100)


LineFollowR(Color.RED)
turn("left")





