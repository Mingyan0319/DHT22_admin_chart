#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import Adafruit_DHT 

db = MySQLdb.connect(host="localhost",
    user="root", passwd="pass1234",
    db="mypj", charset="utf8")
cursor = db.cursor()

DHT_SENSOR = Adafruit_DHT.DHT22 
DHT_PIN = 4  

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

print("Temp={0:0.2f}*C  Humidity={1:0.2f}%".format(temperature, humidity))

cursor.execute('INSERT INTO myapp_dht22 (temp, humidity) '
        'VALUES ("%s", "%s");',(temperature,humidity))
db.commit()

db.close()
