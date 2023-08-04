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
Motor_1 = Motor(Port.A)
Motor_2 = Motor(Port.C)



SonicSens = UltrasonicSensor(Port.S1)
# GyroSens = GyroSensor(Port.S2)
# ColourSens = ColorSensor(Port.S3)
TouchSens = TouchSensor(Port.S4)
TouchSens2 = TouchSensor(Port.S3)
def leftright():
    Motor_1.run(200)
    Motor_2.run(-200)
    time.sleep(1.1)
    Motor_1.stop()
    Motor_2.stop()
    if SonicSens.distance() > 100:
        return
    Motor_1.run(-200)
    Motor_2.run(200)
    time.sleep(2.2)
    Motor_1.stop()
    Motor_2.stop()
    if SonicSens.distance() > 100:
        return
Motor_1.run(300)
Motor_2.run(300)  
# # while True:
#     if SonicSens.distance() < 100:
#         leftright()
#         time.sleep(9)
    
#     degree = GyroSens.angle()
#     # print(degree)
#     if TouchSens.pressed() is True:
#         GyroSens.reset_angle(0)
#         Motor_1.stop()
#         Motor_2.stop()

#     elif degree <= -5:
#         Motor_1.run(300 + degree*4)
#     elif degree >= 5:
#         Motor_2.run(300-degree*4)
#     # else:
#     #     Motor_1.run(300)
#     #     Motor_2.run(300)


while True:

    

    