# import mysql.connector
# from mysql.connector import Error
import datetime
import serial
import time
from time import time
from time import sleep
from time import time, ctime
from time import gmtime, strftime
from stopwatch import Stopwatch
from timeit import default_timer as timer
from datetime import timedelta
import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pooltrack.settings')

django.setup()

from trackball.models import pool_table , action_table 
from django.contrib.auth.models import User

#push arduino data into django

#Arduino Startingg.......
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
#Arduino Data
# t = time()
# ti= ctime(t)

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print ( ":" ,data)
        #change data variable from bytes to String
        # Now, let's decode/convert them into a string
        s = data.decode('UTF-8')
        print(s)
        motion_time = 0.0 
        stopwatch = Stopwatch() # Stopwatch keeps running

        #current date
        y = datetime.datetime.now()
        currentdate = y.strftime("%Y-%m-%d")
        print(currentdate)

        #first get the user
        unique_user = User.objects.get(username="off-duty-manager")
        unique_user_id = unique_user.id

        #a user has a pool table
        # pool = pool_table.objects.get(user_id = unique_user_id)


        unique_pool_table = pool_table.objects.get(user_id=unique_user_id)
        unique_pool_table_id = unique_pool_table.id

        if s == "1": 
            #Get current time
            x = datetime.datetime.now()
            currenttime = x.strftime("%X")
            # print("Inactive_time")
            print(currenttime)
         
            #date

            start = timer()

            #In that pool table there is action happening , The game is going on

            pool_data = action_table.objects.create(pool_table_id = unique_pool_table_id,date = currentdate,time = currenttime,status = s )

       
        else:
            #Get current time
            c = datetime.datetime.now()
            # currenttime = c.strftime("%X")
            currenttime = c.strftime("%X")
            # print("Inactive_time")
            print(currenttime)
            #do some stuff
            end = timer()
            # print("Been Active for")
            # motion_bit = timedelta(seconds=end-start)
            # print(motion_bit)
            #put them inside an array

            #In that pool table there is action happening , The game is going on

            pool_data = action_table.objects.create(pool_table_id = unique_pool_table_id,date = currentdate,time = currenttime,status = s )

            
      
       
        
# print(motion_bits)
