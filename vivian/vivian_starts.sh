#!/bin/bash

#Activate the ve
source /home/ubuntu/.venvs/tangibleai/bin/activate
echo "I have reached the environment.........."
#get Vivian to start collecting the data

echo "making a csv............"
#Vivian gets the csv file
/home/ubuntu/.venvs/tangibleai/bin/python  /home/ubuntu/.code/django_arduino/vivian/get_database_info_to_csv.py

#Go into the visuals directory
cd /home/ubuntu/.code/django_arduino/vivian/visuals


echo "Working on visuals now"

#Vivian saves thats data to heroku git
/usr/bin/git  status

#Vivian adds that status to git
/usr/bin/git add .

#Vivian commits that status
/usr/bin/git commit -am "Add_info"

#Vivian pushes all that to heroku
/usr/bin/git push heroku  master

#Leave that directory
cd ..

#Back to root directory

echo "Back to roots"

#Save all this to github

/usr/bin/git status
/usr/bin/git commit -am "more_data"
/usr/bin/git push origin vivian
#expect check
set user "jakobwamani"
set pass "headphone@1"

spawn /home/ubuntu/.code/django_arduino/vivian/vivian_starts.sh

expect "Username for 'https://github.com':"
send "$user"
expect "Password for 'https://github.com': "
send "$pass"

echo "Collecting data now...................."
#Vivian starts collecting data
/home/ubuntu/.venvs/tangibleai/bin/python  /home/ubuntu/.code/django_arduino/vivian/insert_data_to_database.py


