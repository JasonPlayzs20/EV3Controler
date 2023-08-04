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

gg = ["black","talbe", "red", "white", "green"]
gh = []
SonicSens = UltrasonicSensor(Port.S1)
# GyroSens = GyroSensor(Port.S2)
ColourSens2 = ColorSensor(Port.S2)
ColourSens1 = ColorSensor(Port.S3)

for i in gg:
    gh=[]
    ev3.speaker.say("starting"+ i)
    for g in range(100):
        x = ColourSens1.reflection()
        print(i, x)
        print(ColourSens1.color())
        gh.append(x)
    gh.sort()
    print(gh[0], "....", str(gh[len(gh)-1]))
    ev3.speaker.say("3")
    time.sleep(1)
    ev3.speaker.say("2")
    time.sleep(1)
    ev3.speaker.say("1")
    time.sleep(1)