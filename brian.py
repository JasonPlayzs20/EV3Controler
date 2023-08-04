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
# def LineFollowL(color):
#     while True:
#         if ( ColourSens2.reflection() < 10):
#             Motor_1.run(300)
#             Motor_2.run(285)
#         else:
#             Motor_1.run(300)
#             Motor_2.run(300)
#         if (ColourSens1.reflection() > 69 and ColourSens1.reflection() < 73):
#             Motor_1.run(285)
#             Motor_2.run(300)
#         else:
#             Motor_1.run(300)
#             Motor_2.run(300)

#         if (ColourSens2.color() == color):
#             time.sleep(0.5)
#             Motor_1.stop()
#             Motor_2.stop()
#             break
#         if ColourSens2.reflection() < 10: 
#             Motor_1.stop()
#             Motor_2.stop()
#             break
# Create your objects here.
ev3 = EV3Brick()
Motor_1 = Motor(Port.B)
Motor_2 = Motor(Port.C)
leftArm = Motor(Port.A)
rightArm = Motor(Port.D)


SonicSens = UltrasonicSensor(Port.S1)
# GyroSens = GyroSensor(Port.S2)
ColourSens1 = ColorSensor(Port.S2)
ColourSens2 = ColorSensor(Port.S3)

dic = {"BLACK":9,
"TABLE" : 80,
"RED": 68,
"WHITE":98,
"GREEN":11}

def open(motor):
    motor.run(-100)

def close(motor):
    motor.run(100)

def openr(motor):
    motor.run(100)

def closer(motor):
    motor.run(-100)
    
def go():
    Motor_1.run(200)
    Motor_2.run(200)
    while True: 
        if (ColourSens1.reflection() < dic["TABLE"]-50):
            Motor_1.stop()
            Motor_2.stop()
            break

    
def pickUpL():
    open(leftArm)
    time.sleep(3)
    close(leftArm)
def releaceL():
    open(leftArm)
def pickUpR():
    openr(rightArm)
    time.sleep(2)
    closer(rightArm)
def releaceR():
    openr(rightArm)

def LineFollowR(color):
    while True:
        # if (ColourSens2.reflection() < 1):
        #     Motor_1.run(285)
        #     Motor_2.run(300)
        if ColourSens1.reflection() > dic["TABLE"]-2 and ColourSens1.reflection()< dic["TABLE"]+6 and ColourSens2.reflection() > dic["TABLE"]-2 and ColourSens2.reflection()< dic["TABLE"]+6:
            Motor_1.run(300)
            Motor_2.run(300) 
        elif (ColourSens2.color() == Color.BLACK):
            print(ColourSens2.reflection())
            Motor_1.run(280)
            Motor_2.run(300)
        elif (ColourSens2.reflection() > dic["TABLE"]-2 and ColourSens2.reflection() < dic["TABLE"]+5):
            Motor_1.run(300)
            Motor_2.run(285)
        if (ColourSens1.color() == color):
            time.sleep(0.5)
            Motor_1.stop()
            Motor_2.stop()
            break
        if ColourSens1.color() == Color.BLACK : 
            Motor_1.stop()
            Motor_2.stop()
            break

def LineFollowL(color):
    while True:
        # if (ColourSens2.reflection() < 1):
        #     Motor_1.run(285)
        #     Motor_2.run(300)
       # if ColourSens1.reflection() > dic["TABLE"]-2 and ColourSens1.reflection()< dic["TABLE"]+6 and ColourSens2.reflection() > dic["TABLE"]-2 and ColourSens2.reflection()< dic["TABLE"]+6:
            #Motor_1.run(300)
            #Motor_2.run(300) 
        if (ColourSens1.reflection() < dic["TABLE"]-50):
            print(ColourSens2.reflection())
            Motor_1.run(250)
            Motor_2.run(235)
        elif (ColourSens1.reflection() > dic["TABLE"]-50 and ColourSens1.reflection() < dic["TABLE"]+55):
            Motor_1.run(235)
            Motor_2.run(250)

        if (ColourSens1.color() == color or ColourSens2.color() == color):
            # Motor_1.run(300)
            # Motor_2.run(300)
            time.sleep(0.7)
            Motor_1.stop()
            Motor_2.stop()
            break
        if ColourSens2.reflection() < dic["TABLE"]-50: 
            Motor_1.stop()
            Motor_2.stop()
            break





def LineFollowRBG(color):
    while True:

        if (ColourSens2.reflection() < 10):
            Motor_1.run(205)
            Motor_2.run(250)
        else:
            Motor_1.run(250)
            Motor_2.run(205)

        if (ColourSens2.reflection() > dic[color]-1 and ColourSens2.reflection() < dic[color]+3):
            time.sleep(0.5)
            print("rgb stop")
            Motor_1.stop()
            Motor_2.stop()
            break
        if ColourSens1.color() == Color.BLACK and ColourSens2.reflection() < 10: 
            Motor_1.stop()
            Motor_2.stop()
            break

def turn(dir): 
    print("turn")
    Motor_1.run(-100)
    Motor_2.run(-100)
    time.sleep(1)

    if dir == "right": 
        Motor_1.run(100)
        Motor_2.run(-100) 
    else: 
        Motor_1.run(-100)
        Motor_2.run(100)
    
    time.sleep(1.8)
    Motor_1.stop()
    Motor_2.stop()
    

def ultra():
    
    while True:
        if (ColourSens1.reflection() < dic["TABLE"]-50):
            print(ColourSens2.reflection())
            Motor_1.run(300)
            Motor_2.run(275)
        elif (ColourSens1.reflection() > dic["TABLE"]-50 and ColourSens1.reflection() < dic["TABLE"]+55):
            Motor_1.run(275)
            Motor_2.run(300)
        if (SonicSens.distance() <= 80):
            Motor_1.stop()
            Motor_2.stop()
            break 
        

'''
releaceL()
releaceR()
LineFollowL(Color.RED)
go()
pickUpR()
time.sleep(3)
go()
turn("right")
LineFollowR(Color.RED)
releaceR()
go()
turn("right")
go()
turn("left")
LineFollowRBG("GREEN")
pickUpL()
time.sleep(3)
'''
releaceL()
releaceR()
LineFollowL(Color.RED)
pickUpR()
time.sleep(3)
LineFollowL(Color.RED)
turn("right")
LineFollowL(Color.RED)
releaceR()
# ev3.speaker.say("Thank you for choosing Brian delivery. Please rate us 5 stars")
ultra()#sonic
turn("right")
Motor_1.run(100)
Motor_2.run(100)
time.sleep(1)
Motor_1.stop()
Motor_2.stop()
pickUpL()
time.sleep(4)
go()
turn("right")
go()
turn("left")
go()
turn("right")


Motor_1.run(200)
Motor_2.run(180)
time.sleep(2.5)
Motor_1.stop()
Motor_2.stop()
releaceL()
ev3.speaker.say("Thank you for choosing Brian delivery. Please rate us 5 stars")


'''
go()
turn("right")
go()
turn("left")
LineFollowRBG("GREEN")
pickUpL()
time.sleep(3)
'''

#LineFollowL(Color.RED)