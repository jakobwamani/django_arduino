import sqlite3 as sql
import os
import csv
from sqlite3 import Error
import pandas as pd

try:

  # Connect to database
  conn=sql.connect('db.sqlite3')

 # To view table data in table format
  print ("******Employee Table Data*******")
  cur = conn.cursor()
  cur.execute('''SELECT * FROM bit_game_track''')
  rows = cur.fetchall()
   
  for row in rows:
      print(row)

 # Export data into CSV file
  print ("Exporting data into CSV............")
  # cursor = conn.cursor()
  # cursor.execute("select * from bit_game_track")
  # with open("motion_data.csv", "w") as csv_file:
  #     csv_writer = csv.writer(csv_file, delimiter="\t")
  #     csv_writer.writerow([i[0] for i in cursor.description])
  #     csv_writer.writerows(cursor)
  db_df = pd.read_sql_query("SELECT * FROM bit_game_track", conn)
  db_df.to_csv('motion_data.csv', index=False)

  dirpath = os.getcwd() + "/motion_data.csv"
  print ("Data exported Successfully into {}".format(dirpath))

except Error as e:
  print(e)

# Close database connection
finally:
  conn.close()