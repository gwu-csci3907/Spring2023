#!/usr/bin/env python3

# -----------------------------------------------------------------------------
#                 Sourced from Example Code for Qwiic Kit for Raspberry Pi
# -----------------------------------------------------------------------------
# Code reproduced by Prof. Kartik Bulusu to demonstrate MQTT protocols
# using the senseHAT
#
# Original code information:
# Qwiic Starter Kit Demo for Raspberry Pi
# Read data from the BME280, CCS811, and VCNL4040 proximity sensor. Then display
# the data on the screen, the Micro OLED, and send MQTT data to Cayenne.
# Original code by: Michelle Shorter @ SparkFun Electronics
# Original Creation Date: May 29, 2019
#
# For the hookup instructions and kit go to:
#      https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide
# 
# This code is beerware/beefware; if you see me (or any other SparkFun employee)
# at the local, and you've found our code helful, please buy us a beer/burger!
#
# Distributed as-is; no warranty is given
# -----------------------------------------------------------------------------

# =========== IMPORT MODULES THAT WORK WITH MQTT ========================

from __future__ import print_function, division
import paho.mqtt.client as mqtt
# import qwiic
import time
import sys

# =========== IMPORT MODULES THAT WORK WITH SENSE HAT ========================

from sense_hat import SenseHat
sense = SenseHat()

#These values are used to give BME280 and CCS811 some time to take samples
initialize=True
n=2


# =========== GET THE ORIENTATION DATA [Pitch, Yaw and Roll] =================

orientation_data = sense.get_orientation()

pitch = orientation_data['pitch']
yaw = orientation_data['yaw']
roll = orientation_data['roll']

# =========== GET COMPASS DATA [X, Y and Z] ==================================

compass_data = sense.get_compass_raw()

m_x = compass_data['x']
m_y = compass_data['y']
m_z = compass_data['z']

# =========== GET ACCELEROMETER DATA [AX, AY and AZ] =========================

accelerometer_data = sense.get_accelerometer_raw()

a_x = accelerometer_data['x']
a_y = accelerometer_data['y']
a_z = accelerometer_data['z']

# =========== GET GRYOSCOPE DATA [GX, GY and GZ] =============================

gyroscope_data = sense.get_gyroscope_raw()

g_x = gyroscope_data['x']
g_y = gyroscope_data['y']
g_z = gyroscope_data['z']

# =========== MQTT Cayenne setup  ========================
# You will need your own username, password and clientid
# To setup a Cayenne account go to https://mydevices.com/cayenne/signup/

username = "adf69130-ae1f-11ed-b0e7-e768b61d6137"
password = "4cddbe14f0fd456d240ece96284bc2fdeb5354ed"
clientid = "536073a0-ae9a-11ed-b0e7-e768b61d6137"
mqttc=mqtt.Client(client_id = clientid)
mqttc.username_pw_set(username, password = password)
mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=60)
mqttc.loop_start()

# ========== Used for debugging SenseHat
try:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    pitch = orientation_data['pitch']
    yaw = orientation_data['yaw']
    roll = orientation_data['roll']

except Exception as e:
    print(e)

# ========== set MQTT topics (we are not setting topics for everything) ==========
topic_bme_temp = "v1/" + username + "/things/" + clientid + "/data/1"
topic_bme_pressure = "v1/" + username + "/things/" + clientid + "/data/2"
topic_bme_hum = "v1/" + username + "/things/" + clientid + "/data/3"

#topic_bme_pitch = "v1/" + username + "/things/" + clientid + "/data/4"
#topic_bme_yaw = "v1/" + username + "/things/" + clientid + "/data/5"
#topic_bme_roll = "v1/" + username + "/things/" + clientid + "/data/6"

# ========== Loop runs until we force an exit or something breaks
while True:
    try:
        if initialize==True:
            print ("Initializing: BME280 and CCS811 are taking samples before printing and publishing data!")
            print (" ")
        else:
            #print ("Finished initializing")
            n=1 #set n back to 1 to read sensor data once in loop
        for n in range (0,n):
            
            tempc = sense.get_temperature()
            pressure = sense.get_pressure()
            humidity = sense.get_humidity()
#            pitch = orientation_data['pitch']
#            yaw = orientation_data['yaw']
#            roll = orientation_data['roll']
            #print ("n = ", n) #used for debugging for loop
            
            # ========== Give some time for the BME280 and CCS811 to initialize when starting up
            if initialize==True:
                time.sleep(10)
                initialize=False
        
        #printing time and some variables to the screen
        #https://docs.python.org/3/library/time.html
        #print (time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())) #24-hour time 
        print (time.strftime("%a %b %d %Y %I:%M:%S%p", time.localtime())) #12-hour time
        
        print ("Temperature %.1f C" %tempc)
        print ("Pressure %.2f Pa" %pressure)
        print ("Humidity %.1f" %humidity)
        
        print (" ") #blank line for easier readability
        
        # ========== publishing data to Cayenne (we are not publishing everything)
        mqttc.publish (topic_bme_temp, payload = tempc, retain = True)
        mqttc.publish (topic_bme_hum, payload = humidity, retain = True)
        mqttc.publish (topic_bme_pressure, payload = pressure, retain = True)
#        mqttc.publish (topic_bme_pitch, payload = pitch, retain = True)
#        mqttc.publish (topic_bme_yaw, payload = yaw, retain = True)
#        mqttc.publish (topic_bme_roll, payload = roll, retain = True)
        
        # ========== delay (number of seconds) so we are not constantly displaying data and overwhelming devices
        time.sleep(5)
        
        
    # ========== if we break things or exit then exit cleanly
    except (EOFError, SystemExit, KeyboardInterrupt):
        mqttc.disconnect()
        sys.exit()
