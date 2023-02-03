#!/bin/bash
#File: LED_examples/run_on_boot.sh

# Absolute path to Virtual Environment python interpreter
PYTHON=/home/pi/Desktop/Spring2023/LED_examples/venv/bin/python

# Absolute path to Python script
SCRIPT=//home/pi/Desktop/Spring2023/LED_examples/LED_1.py

# Absolute path to output log file
LOG=/home/pi/Desktop/Spring2023/LED_examples/LED_1.log

echo -e "\n####### STARTUP $(date) ######\n" >> $LOG

$PYTHON $SCRIPT >> $LOG 2>&1
