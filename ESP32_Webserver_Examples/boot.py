"""
==== Source code written by Prof. Kartik Bulusu (1) and Adellar Irankunda (2)
==== CS and MAE Department, SEAS GWU
==== Undergraduate student, Physics Department, GWU
==== Description:
======== boot.py to control ESP32 that creates a Webserver Access Point 
==== Requirements:
============ The program requires Micropython v 1.14 and dependent libraries:
============ It has been written exclusively for CS3907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/07/2023 using MicroPython 1.14 on Raspberry Pi 3B+ and Thonny IDE
==== 2. Tested on 03/23/2023 using MicroPython 1.14 on Raspberry Pi 3B+
==== 3. Modified on 03/24/2023 using MicroPython 1.14 on Raspberry Pi 3B+
"""

try:
    import usocket as socket
except:
    import socket
    
#import webrepl
#webrepl.start()


import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ESP32_CS3907D' # SHOULD BE CHANGED FOR EACH ESP32 USED in CLASS
password = 'PASSWORD123456789' # CAN STAY THE SAME FOR IN-CLASS DEMO

ap = network.WLAN(network.AP_IF)
ap.active(True)

#Activate our station
ap.config(essid=ssid, password=password)

while ap.active() == False:
    pass

print('Connection successful')
print(ap.ifconfig())

