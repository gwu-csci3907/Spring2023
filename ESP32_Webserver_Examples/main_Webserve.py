"""
==== ESP32 Access Point generator toward IoT applications
==== Source code written by Prof. Kartik Bulusu (1) and Adellar Irankunda (2)
==== CS and MAE Department, SEAS GWU
==== Undergraduate student, Physics Department, GWU
==== Description:
======== ESP32 Webserver can be accessed using the Access Point IP address to
======== activate an LED using a html front that has ON / OFF buttons
==== Requirements:
============ The program requires Micropython v 1.14 and dependent libraries:
============ machine, socket, network, esp, gcand other imported libraries
============ The progrem requires a companion boot.py that creates the access point credentials within it
======== It has been written exclusively for CS3907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/07/2023 using MicroPython 1.14 on Raspberry Pi 3B+ and Thonny IDE
==== 2. Tested on 03/23/2023 using MicroPython 1.14 on Raspberry Pi 3B+
==== 3. Modified on 03/24/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
"""


import socket
from machine import Pin
import network

#use the builtin LED
led = Pin(13, Pin.OUT)

#def do_connect1():
ap = network.WLAN(network.AP_IF)
ap.active(True)

def landing():
    if led.value() == 1:
        gpio_state="ON"
    else:
        gpio_state="OFF"
  
    page_contents = """<html>
    <head>
    <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head>
    <body>
    <h1>ESP Web Server</h1> 
    <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
    <p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
    </body>
    </html>"""
    return page_contents

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    #handle incoming connections and print local addresses
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))

    request = conn.recv(1024)
    request = str(request)

    #optionally print out the client's request'
    # print('Content = %s' % request)

    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')

    if led_on == 6:
        print('LED ON')
        led.value(1)
    if led_off == 6:
        print('LED OFF')
        led.value(0)

    #render our html based page
    response = landing()

    #if we made it this far, send the 200 code letting client know request was processed
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')

    #send page
    conn.sendall(response)
    conn.close()