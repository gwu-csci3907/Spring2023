"""
==== Blinking LEDs on ESP32 WROOM 32E microcontroller for IoT applications
==== Source code written by Prof. Kartik Bulusu
==== CS and MAE Department, SEAS GWU
==== Description:
======== ESP32 WROOM 32E microcontroller for IoT demonstration in CS3907   
==== Requirements:
============ The program requires Python 3.5.3 dependent interpreter and plug-ins:
============ MicroPython for ESP32
============ Latest and stable generic ESP32 firmware from https://micropython.org/download/esp32/
============ esptool.py plug-in 
======== It has been written exclusively for CS3907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/15/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
==== 2. Tested on using Python 3.5.3 on Raspberry Pi 3B+
==== 3. Modified on  using Python 3.10.6 on Macbook Pro using Thonny IDE
"""

from machine import Pin
from time import sleep
led = Pin(13, Pin.OUT)
# while True:
for _ in range(10):
    led.value(not led.value())
    sleep(0.5)
    print("Hello ESP32")
    
# led.on()
# led.off()

# led.value(1)
# led.value(0)

# led.value(True)
# led.value(False)
