#!/bin/bash

#Activate the ve
source /home/ubuntu/.venvs/tangibleai/bin/activate
echo "I have reached the environment.........."
#get Vivian to start collecting the data

#Vivian gets the csv file
/home/ubuntu/.venvs/tangibleai/bin/python  /home/ubuntu/.code/django_arduino/vivian/get_database_info_to_csv.py
echo "making a csv............"


#Vivian saves thats data to heroku git
/usr/bin/git  status

#Vivian adds that status to git
/usr/bin/git add .

#Vivian commits that status
/usr/bin/git commit -am "Add_info"

#Vivian pushes all that to heroku
/usr/bin/git push heroku master
