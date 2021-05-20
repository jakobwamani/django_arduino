os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pooltrack.settings')

django.setup()

from trackball.models import pool_table , action_table

#push arduino data into django


import mysql.connector
from mysql.connector import Error
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

        if s == "1": 
            #Get current time
            x = datetime.datetime.now()
            currenttime = x.strftime("%X")
            # print("Inactive_time")
            print(currenttime)
         
            start = timer()
        else:
            #Get current time
            c = datetime.datetime.now()
            currenttime = c.strftime("%X")
            # print("Inactive_time")
            print(currenttime)
            #do some stuff
            end = timer()
            print("Been Active for")
            motion_bit = timedelta(seconds=end-start)
            print(motion_bit)
            #put them inside an array
            
        #current date
        y = datetime.datetime.now()
        currentdate = y.strftime("%x")
        print(currentdate)

    #input into the database first start with the first table

    pool = pool_table.objects.create(pool_name="gwanzo",pool_location="kyenjojo",pub_date=currentdate)

    #first pull the unique raw

    # then input inside the the second table 

    pool_data = action_table.objects.create(pool_id=unique_row_id,x=m[0],y=m[1])

   
print(motion_bits)
