#!/bin/bash

#Activate the ve
source /home/ubuntu/.venvs/tangibleai/bin/activate
echo "I have reached the environment.........."
#get Vivian to start collecting the data
/home/ubuntu/.venvs/tangibleai/bin/python  /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py
echo "Collecting data now..............."

#Vivian gets the csv file
/home/ubuntu/.venvs/tangibleai/bin/python  /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py
echo "making a csv............"



