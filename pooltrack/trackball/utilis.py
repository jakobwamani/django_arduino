import matplotlib.pyplot as plt 
import base64
from io import BytesIO
from .models import action_table
# from trackball.models import pool_table , action_table 

def get_graph():
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffer.close()
	return graph

def get_plot():
	plt.switch_backend('AGG')
	plt.figures(figsize=(10,5))
	plt.title('sales of items')
	plt.plot(y)
	plt.xticks(rotation=45)
	plt.xlabel('time')
	plt.ylabel('status')
	plt.tight_layout()
	graph = get_graph()
	return graph

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import mysql.connector
# from mysql.connector import Error
import datetime
import time
from time import sleep
from time import time, ctime
from time import gmtime, strftime
from datetime import timedelta

# To Calculate the hours of a specific date 
# I need to get the info from the database 
# They have turned out to be tuples

#i will use those hours my x axis

# try:

#Get current date
y = datetime.datetime.now()
currentdate = y.strftime("%Y-%m-%d")
print(currentdate)

# pool_data = action_table.objects.filter(date = currentdate).values_list('date', 'time','status')
pool_data = action_table.objects.filter(date = currentdate)

#plot
# x_axis = [x.time for x in pool_data]
y_axis = [y.status for y in pool_data]


plt.plot(y_axis)
plt.xlabel('time')
plt.ylabel('status')
plt.show()





