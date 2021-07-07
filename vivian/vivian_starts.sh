#!/bin/bash

#Activate the ve
source /home/jay/venvs/tangibleai/bin/activate
echo "I have reached the environment"
#get Vivian to start collecting the data
# /home/jay/venvs/tangibleai/bin/python  /home/jay/code/django_arduino/vivian/insert_data_to_database.py
echo "Collecting data now"

#Vivian gets the csv file
/home/jay/venvs/tangibleai/bin/python  /home/jay/code/django_arduino/vivian/insert_data_to_database.py




