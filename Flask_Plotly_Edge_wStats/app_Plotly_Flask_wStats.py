"""
==== flask app for random number plots toward IoT applications
==== Source code written by Prof. Kartik Bulusu
==== CS and MAE Department, SEAS GWU
==== Description:
======== flask API implementation for IoT demonstration in CS3907   
==== Requirements:
============ The program requires Python 3.5.3 dependent libraries:
============ flask, pandas, plotly, json, datetime and other imported libraries
============ The progrem requires a html-code that embeds plotly.js within it
======== It has been written exclusively for CS3907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/07/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
==== 2. Tested on 03/08/2023 on Python 3.5.3 on Raspberry Pi 3B+
==== 3. Modified on 03/08/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
==== Reference: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
"""

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
import logging

# ======== Initialize Logging ===========

# Global logging configuration
logging.basicConfig(level=logging.WARNING)  

# Logger for this module
logger = logging.getLogger('main')

# Debugging for this file.
logger.setLevel(logging.INFO)


# ======== Initialize flask app ===========
app = Flask(__name__)

@app.route('/')

# ======== Create function to gather data and render to html-frontend ===========
def notdash():
    global data
    data = {
        'timeT': [],
        'Voltage': []
    }
    
    # ======================================================================    
    # ===== Create the graph with subplots with layout and margins =========
    # ======================================================================
    fig = plotly.tools.make_subplots(rows=3, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 40, 'r': 20, 'b': 40, 't': 20
    }
    
    for i in range(20):
        
        timeT = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        data['Voltage'].append(random.randint(0, 100))
        data['timeT'].append(timeT)
        
        # ======================================================================    
        # ===== Create traces for plotly =======================================
        # ======================================================================
        fig.append_trace({
            'x': data['timeT'],
            'y': data['Voltage'],
#             'name': 'Voltage',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
        
        fig.append_trace({
            'x': data['timeT'],
            'y': data['Voltage'],
#             'text': data['time'],
#             'name': 'Voltage',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 2, 1)
                
    # ======================================================================    
    # ===== Overlay trace-2 with mean and standard deviation lines =========
    # ======================================================================
    fig.append_trace({
        'x': data['timeT'],
        'y': np.mean(data['Voltage'])*np.ones(20),
#             'text': data['time'],
#             'name': 'Longitude vs Latitude',
        'mode': 'lines',
        'type': 'scatter'
        }, 2, 1)
    
    fig.append_trace({
        'x': data['timeT'],
        'y': (np.mean(data['Voltage']) + np.std(data['Voltage']))*np.ones(20),
        'mode': 'lines',
        'type': 'scatter',
        }, 2, 1)
    
    fig.append_trace({
        'x': data['timeT'],
        'y': (np.mean(data['Voltage']) - np.std(data['Voltage']))*np.ones(20),
        'mode': 'lines',
        'type': 'scatter'
        }, 2, 1)
    
    # ======================================================================    
    # ===== trace-3 with moving average data ===============================
    # ======================================================================
    fig.append_trace({
        'x': data['timeT'],
        'y': np.convolve(data['Voltage'], np.ones(3)/3, mode='same'),
        'mode': 'lines',
        'type': 'scatter'
        }, 3, 1)

    # ======================================================================    
    # ===== Serializing fig json object ====================================
    # ===== Writing data into a json-file ==================================
    # ====================================================================== 
#     print(data)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    

    # ======================================================================    
    # ===== Serializing raw data of Voltage and timeT into a json object ===
    # ===== Writing data into a json-file ==================================
    # ====================================================================== 
    json_object = json.dumps(data, sort_keys=True, default=str) 
#     print(json_object)
    with open("sample.json", "a") as outfile:
        json.dump(json_object, outfile)
    
    # ======================================================================    
    # ===== Rendering data to the html frontend ============================
    # ====================================================================== 
    return render_template('notdash.html', graphJSON=graphJSON)

            
if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", debug=True)
