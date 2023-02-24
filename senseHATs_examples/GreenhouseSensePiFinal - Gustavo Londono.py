# CS1010-Fall2022
# Final Project by Gustavo Londono, Logan Kim and Joshua Aravind

#----------Import and configure SenseHat----------#
from sense_hat import SenseHat
from matplotlib import pyplot as plt
import os.path
import time
import csv

sen = SenseHat()
#Logan Kim

#Declaring Variables
timeElapsed = 0
tempList = []
pressList = []
humList = []
timeList = []
#Joshua Arvind

#Setting how long the Pi will collect data for taken from user input
#This while loop houses a try-except that ensures the value passed through is an int
def userInput():
    global timeLimit
    sen.clear()
    while True:
        
        try:
            timeLimit = int(input('Enter how long would you like the Pi to collect data for (in seconds) '))
        except ValueError:
            print('A valid Integer, please.')
            continue
        if type(timeLimit) == int:
            break
        else:
            print('A valid Integer, please.') 
#Gustavo Londono 


#Function for conversion from Celsius to Fahrenheit
def ctof(c):
    result = (c*(9/5)) + 32

    return round(result, 1)
#joshua Arvind

#Assign the message
def updateDisplay():
    msg = "Temp = %s F, Pressure = %s mbar, Humidity = %s" % (temp, press, hum)
    sen.show_message(msg, scroll_speed = 0.05) 
#Joshua Arvind

    
#Function for the creation of the subplots
def plot(timeIn, tempX, pressX, humX):
    
    #initialize the graph
    fig, graph = plt.subplots(3, 1, figsize = (10, 20), constrained_layout=True)
    graph[0].plot(timeIn, tempX, color='r', label='Temperature')
    graph[1].plot(timeIn, pressX, color='b', label='Pressure')
    graph[2].plot(timeIn, humX, color='g', label='Humidity')
    
    #Make everything Fancy
    graph[0].set_xlabel('Time (s)', fontsize = 12)
    graph[0].set_ylabel('Temperature (F)', fontsize = 12)
    graph[1].set_xlabel('Time (s)', fontsize = 12)
    graph[1].set_ylabel('Pressure (mbar)', fontsize = 12)
    graph[2].set_xlabel('Time (s)', fontsize = 12)
    graph[2].set_ylabel('Humidity', fontsize = 12)
    
    #Message that shows this funciton is underway
    sen.show_message('Printing Data', scroll_speed = 0.05)
    
    #Show the graph
    time.sleep(1)
    plt.show()
#Gustavo Londono
    
    
#Function to gather environmental data
def gatherData():
    
    #Declare global variables
    global timeElapsed
    global temp
    global hum
    global press
    global start_time
    global last_second
    
    #Open csv file and prepare for writing
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Time Elapsed (s)','Temperature (F)', 'Pressure (mbar)', 'Humidity'])
     
    
        #Message on LED Display
        sen.show_message('Collecting Data', scroll_speed = 0.03)
        #Establishes the start time 
        start_time = time.time()
        #Logs the most recent second passed
        last_second = 0
    
    
        while timeElapsed < timeLimit:
            timeElapsed = time.time()- start_time
            secondsElapsed = int(timeElapsed)
            sen.clear()
            
        
            if last_second != secondsElapsed:    
                #Gather Environment Data   
                temp = sen.get_temperature()
                press = sen.get_pressure()
                hum = sen.get_humidity()
        
                #Round up the values and convert temp to F
                temp = ctof(temp)
                press = round(press, 1)
                hum = round(hum, 1)
    
                #Appending the data into arrays
                tempList.append(temp)
                pressList.append(press)
                humList.append(hum)
                timeList.append(secondsElapsed)
            
                #write data to csv file
                print(csvfile.closed)
                csvwriter.writerow([secondsElapsed, temp, press, hum])
            
                #Print data to the console
                print(tempList)
                print(pressList)
                print(humList)
                print(timeList)
                #Change the display
                sen.clear()
        
        
            last_second = secondsElapsed
#Gustavo Londono, Logan Kim, Joshua Arvind

def file():
    global csvfile
    global csvwriter
    global filename
    
    i = 0
    if os.path.exists('test0.csv'):
        while os.path.exists('test%s.csv' % i):
            i += 1
            filename = 'test%s.csv' % i
            print(filename)
    else:
        filename = 'test0.csv'
#Gustavo Londono
        
    
#|----Main Function----|

userInput()
file()
gatherData()
plot(timeList, tempList, pressList, humList)
updateDisplay()
#Gustavo Londono and Logan Kim
    
