"""
==== flask app for senseHat-based IoT applications
==== Source code written by Prof. Kartik Bulusu
==== CS and MAE Department, SEAS GWU
==== Description:
======== flask API implementation for IoT demonstration in CS3907   
======== This program incorporates the RaspberryPi SenseHat sensors and flask library
============ SenseHat documentation: https://www.raspberrypi.com/documentation/accessories/sense-hat.html
==== Requirements:
============ The program requires Python 3.5.3 dependent libraries:
============ flask, pandas, plotly, json, datetime and other imported libraries
============ The progrem requires a html-code that embeds plotly.js within it
======== It has been written exclusively for CS1010, CS3907 & APSC1001 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/07/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
==== 2. Tested on 03/08/2023 on Python 3.5.3 on Raspberry Pi 3B+
==== 3. Modified on 03/08/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
"""

#----------Import and configure SenseHat----------#
from sense_hat import SenseHat
import os.path
import csv
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

# =========== IMPORT MODULES THAT WORK WITH SENSE HAT ========================

from sense_hat import SenseHat
import time

sense = SenseHat()
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()
        
t = round(t,1)
p = round(p,1)
h = round(h,1)
msg = "Temp = %s C, Pressure = %s mbar, Humidity =%s" % (t, p, h)
sense.show_message(msg, scroll_speed=0.05)
     
app = Flask(__name__)

@app.route('/')

def notdash():
    global data
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
        
    t = round(t,1)
    p = round(p,1)
    h = round(h,1)
    
    msg = "Pressure = %s mbar, Temp = %s C, Humidity =%s" % (p, t, h)
        
    sense.show_message(msg, scroll_speed=0.05)
    
    data = {
        'timeT': [],
        'Temperature': [],
        'Pressure': [],
        'Humidity': []
    }
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=3, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    
    for i in range(20):
        timeT = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        data['Pressure'].append(p)
        data['Temperature'].append(t)
        data['Humidity'].append(h)
        data['timeT'].append(timeT)
        
        fig.append_trace({
            'x': data['timeT'],
            'y': data['Pressure'],
#             'name': 'Voltage',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        
        fig.append_trace({
            'x': data['timeT'],
            'y': data['Temperature'],
#             'text': data['time'],
#             'name': 'Longitude vs Latitude',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 2, 1)
        
        fig.append_trace({
            'x': data['timeT'],
            'y': data['Humidity'],
#             'text': data['time'],
#             'name': 'Longitude vs Latitude',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 3, 1)
        
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    

    
    return render_template('notdash.html', graphJSON=graphJSON)

def json_Data():
    global data
    with open("sample.json", "a") as outfile:
        json.dump(data, outfile)
        
if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", debug=True)
#     json_Data()
