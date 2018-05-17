#Imports
import bme680
import time
import datetime
import sqlite3
import os
import mysql.connector
from mysql.connector import errorcode

#Operating Ranges
def testTemperature(temp):
    if  -40 < temp and temp < 185:
        return True
    else:
        return False
def testPressure(pressure):
    if 300 < pressure and pressure < 1100:
        return True
    else:
        return False
def testHumidity(humidity):
    if 0 < humidity and humidity < 100:
        return True
    else:
        return False


#Main Function
def main():
    #Variables
    repeat = 11 #Number of times you want while loop to repeat
    wait_period = 300 #Seconds you want to wait between each reading
    count = 0 #Keep 0, incriment each time you take a reading
    
    #Create Sensor
    sensor = bme680.BME680(i2c_addr=0x77)
    
    #Database
    # Creates or opens a file called mydb with a SQLite3 DB
    # db = sqlite3.connect("/home/pi/Pimoroni/bme680/examples/testDB.db")
    db = mysql.connector.connect(user = 'sensored',
                                 password = 'stevens2014',
                                 host = 'sensored.cdrs74k0clf3.us-east-1.rds.amazonaws.com',
                                 database = 'SensorEdAWS'
                                 )
    cursor = db.cursor()
    #Using MacAddress.py find the unique mac adress of the Raspberry Pi Board to identify table name.
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS b827ebb798b6(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, dateNow varchar(20), timeNow varchar(20), temperature FLOAT,
                           pressure FLOAT, humidity FLOAT, gas FLOAT)
        ''')
    except errorcode as e:
        print("Error: " + str(e))
    
    # These calibration data can safely be commented
    # out, if desired.
    """
    print("Calibration data:")
    for name in dir(sensor.calibration_data):
        if not name.startswith('_'):
            value = getattr(sensor.calibration_data, name)
        if isinstance(value, int):
            print("{}: {}".format(name, value))
    # These oversampling settings can be tweaked to 
    # change the balance between accuracy and noise in
    # the data.
    """

    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

    print("\n\nInitial reading:")
    for name in dir(sensor.data):
        value = getattr(sensor.data, name)

        if not name.startswith('_'):
            print("{}: {}".format(name, value))

    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    # Up to 10 heater profiles can be configured, each
    # with their own temperature and duration.
    # sensor.set_gas_heater_profile(200, 150, nb_profile=1)
    # sensor.select_gas_heater_profile(1)

    print("\n\nPolling:")
    try:
        while(repeat > count):
            if sensor.get_sensor_data():
                dateNow = time.strftime("%Y-%m-%d")
                timeNow = time.strftime("%H:%M:%S")
                temperatureCelcius = float("{0:.2f}".format(sensor.data.temperature))
                temperature = (temperatureCelcius * (9/5)) + 32
                pressure = float("{0:.2f}".format(sensor.data.pressure))
                humidity = float("{0:.2f}".format(sensor.data.humidity))
                gas = float("{0:.2f}".format(sensor.data.gas_resistance))
                saveToDB = ("INSERT INTO b827ebb798b6"
                               "(dateNow, timeNow, temperature, pressure, humidity, gas) "
                               "VALUES(%(dateNow)s, %(timeNow)s, %(temperature)s, %(pressure)s, %(humidity)s, %(gas)s)")
                dataObject = {
                "dateNow" : dateNow,
                "timeNow" : timeNow,
                "temperature" : temperature,
                "pressure" : pressure,
                "humidity" : humidity,
                "gas" : gas
                }
                cursor.execute(saveToDB, dataObject)
                print('Date      : ' + str(dateNow))
                print('Time      : ' + str(timeNow)) 
                print('Temp      : ' + str(temperature) + 'F')
                print('Pressure  : ' + str(pressure) + 'hPa')
                print('Humidity  : ' + str(humidity) + '%RH')
                print('Gas       : ' + str(gas) + 'Ohms')
                #print('Database Updated')
                #Increase incrimenter
                count += 1
                #Tell Board to wait 'wait_peroid' amount of secionds before moving on
                time.sleep(wait_period)

        #Update Changes And Close Databse
        db.commit()    
        db.close()

    except KeyboardInterrupt:
        pass
    
#RUN MAIN FUNCTION
if __name__ == '__main__':
    main()
