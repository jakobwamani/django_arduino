#!/bin/bash
#Activate the env
source  /home/ubuntu/.venvs/tangibleai/bin/activate
echo "Env activated..............."
#after all that we start to collect the data
echo "starting to collect data now...................."
/home/ubuntu/.venvs/tangibleai/bin/python   /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py


