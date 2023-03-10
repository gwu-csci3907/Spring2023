"""
Source code written by Kartik Bulusu
Tested on Python 3.10.6 on Macbook Pro using Thonny IDE 
Reference: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
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

V = []
T = []

app = Flask(__name__)

@app.route('/')

def notdash():
#     for i in range(0,10):
#         V.append(random.randint(0, 100))
#         T.append(i)
#         rawData = ({'Voltage' : V, 'Time': T})
#         df = pd.DataFrame(rawData)
#         time.sleep(0.5)
# #         print(df)
#         fig = px.bar(df, x='Time', y='Voltage', barmode='group')
#         graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    data = {
        'time': [],
        'Voltage': [],
    }        
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    
    for i in range(20):
#         time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        data['Voltage'].append(random.randint(0, 100))
        data['time'].append(i)
        
        fig.append_trace({
            'x': data['time'],
            'y': data['Voltage'],
            'name': 'Voltage',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
#         time.sleep(0.5)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('notdash.html', graphJSON=graphJSON)
    

if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", debug=True) 