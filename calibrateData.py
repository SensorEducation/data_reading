#Calibrate Data

#Imports
from random import randint
import mysql.connector
from mysql.connector import errorcode

#Variables
temp_data_1 = []
temp_data_2 = []
temp_avg_diff = 0
pressure_data_1 = []
pressure_data_2 = []
pressure_avg_diff = 0
humidity_data_1 = []
humidity_data_2 = []
humidity_avg_diff = 0
gas_data_1 = []
gas_data_2 = []
gas_avg_diff = 0

'''
BOX
'''
#Connect to the database file by specifying the path as the parameter
db = mysql.connector.connect(user = 'sensored',
                                 password = 'stevens2014',
                                 host = 'sensored.cdrs74k0clf3.us-east-1.rds.amazonaws.com',
                                 database = 'SensorEdAWS'
                                 )

#Assign the curser to manage the database
cursor = db.cursor()

#Retrieve Data
cursor.execute('''SELECT dateNow, timeNow, temperature, pressure, humidity, gas FROM b827ebb798b6''')

#Declare a variable that will acquire all the data using cursor.fethchall()
all_rows = cursor.fetchall()


for row in all_rows:
    temp_data_1.append(row[2])
    pressure_data_1.append(row[3])
    humidity_data_1.append(row[4])
    gas_data_1.append(row[5])

db.commit()
db.close()

'''
NOT BOX
'''
#Connect to the database file by specifying the path as the parameter
db = mysql.connector.connect(user = 'sensored',
                                 password = 'stevens2014',
                                 host = 'sensored.cdrs74k0clf3.us-east-1.rds.amazonaws.com',
                                 database = 'SensorEdAWS'
                                 )

#Assign the curser to manage the database
cursor = db.cursor()

#Retrieve Data
cursor.execute('''SELECT dateNow, timeNow, temperature, pressure, humidity, gas FROM b827eb06efa4''')

#Declare a variable that will acquire all the data using cursor.fethchall()
all_rows = cursor.fetchall()


for row in all_rows:
    temp_data_2.append(row[2])
    pressure_data_2.append(row[3])
    humidity_data_2.append(row[4])
    gas_data_2.append(row[5])

db.commit()
db.close()

'''
ITERATE OVER
'''
count = 0
max_count = 100
while count < max_count:
    temp_avg_diff += temp_data_1[count] - temp_data_2[count]
    pressure_avg_diff += pressure_data_1[count] - pressure_data_2[count]
    humidity_avg_diff += humidity_data_1[count] - humidity_data_2[count]
    gas_avg_diff += gas_data_1[count] - gas_data_2[count]
    count += 1

temp_avg_diff = temp_avg_diff / max_count
pressure_avg_diff = pressure_avg_diff / max_count
humidity_avg_diff = humidity_avg_diff / max_count
gas_avg_diff = gas_avg_diff / max_count

print("Average Temperature Difference: " + str(temp_avg_diff))
print("Average Pressure Difference: " + str(pressure_avg_diff))
print("Average Humidity Difference: " + str(humidity_avg_diff))
print("Average Gas Difference: " + str(gas_avg_diff))

'''
#Temperature
count = 0
while count < 100:
    temp_data_1.append(randint(0, 90))
    temp_data_2.append(randint(0, 90))
    count += 1

count = 0
while count < 100:
    temp_avg_diff += (temp_data_1[count] - temp_data_2[count])
    count += 1

temp_avg_diff = temp_avg_diff / 100

print("Average Temperature Difference: " + str(temp_avg_diff))

#Pressure
count = 0
while count < 100:
    pressure_data_1.append(randint(0, 90))
    pressure_data_2.append(randint(0, 90))
    count += 1

count = 0
while count < 100:
    pressure_avg_diff += (pressure_data_1[count] - pressure_data_2[count])
    count += 1
pressure_avg_diff = pressure_avg_diff / 100

print("Average Pressure Difference: " + str(pressure_avg_diff))

#Humidity
count = 0
while count < 100:
    humidity_data_1.append(randint(0, 90))
    humidity_data_2.append(randint(0, 90))
    count += 1

count = 0
while count < 100:
    humidity_avg_diff += (humidity_data_1[count] - humidity_data_2[count])
    count += 1

humidity_avg_diff = humidity_avg_diff / 100

print("Average Humidity Difference: " + str(humidity_avg_diff))

#Gas
count = 0
while count < 100:
    gas_data_1.append(randint(0, 90))
    gas_data_2.append(randint(0, 90))
    count += 1

count = 0
while count < 100:
    gas_avg_diff += (gas_data_1[count] - gas_data_2[count])
    count += 1

gas_avg_diff = gas_avg_diff / 100

print("Average Gas Difference: " + str(gas_avg_diff))
'''


