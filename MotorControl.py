# -*- coding: utf-8 -*-
"""
@author: moore
"""

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_motorkit import MotorKit
from UltraSonic_Sensor import *

kit = MotorKit(i2c=board.I2C())
dist1 = getDist1()
dist2 = getDist2()

#forward
if(dist1 > 25 and dist2 > 25):
    kit.motor1.throttle = 0.5
    kit.motor1.throttle = 0.5
    time.sleep(1.0)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    
#back
if(dist1 <= 25 and dist2 <= 25):
    kit.motor1.throttle = -0.5
    kit.motor1.throttle = -0.5
    time.sleep(2.0)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

#right
if(dist1 <= 25):
    kit.motor1.throttle = -0.5
    kit.motor1.throttle = 0.5
    time.sleep(2.0)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    
#left
if(dist2 <= 25):
    kit.motor1.throttle = 0.5
    kit.motor1.throttle = -0.5
    time.sleep(2.0)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    
GPIO.cleanup()
