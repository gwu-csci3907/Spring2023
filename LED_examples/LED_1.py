"""
==== Prof. Kartik V. Bulusu
==== CS and MAE Department, SEAS GWU
==== Description
======== This program is for blinking an LED wired to Raspberry PI
======== It has been written exclusively for students of CS3907(IoT and Edge Computing Applications) 
======== and CS1010(Computer Science Orientation) courses in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup([11,12], GPIO.OUT)

for i in range(0,5):
    
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
    
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
    print(i)
    
GPIO.cleanup()
