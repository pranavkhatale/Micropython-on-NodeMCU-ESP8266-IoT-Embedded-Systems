# Interfacing DHT11 Sensor with NodeMCU ESP8266 12-E using Micropython in Thonny IDE.
# by Pranav Khatale
# 06 November 2020

from machine import Pin     # Import the Pin class from the machine module to define pins
from time import sleep      # Iimport the sleep method from the time module to add delays.
import dht                  # Import the dht module to import the functions to read from the DHT sensor.

# Defining a dht object called sensor that refers to the sensor’s data pin.
sensor = dht.DHT11(Pin(15)) # Declaring GPIO pin 15 or D8 as DHT11 Sensor pin.

while True:
  try: # We're trying to get temperature and humidity values.
    sleep(1)          # Adding a delay of 1 seconds because the DHT11's maximum sampling rate is 1 seconds.                           
    sensor.measure()  # Using the measure() method on the sensor object.
    temp = sensor.temperature()  # Reading the temperature.
    hum = sensor.humidity()      # Reading the humidity.
    temp_f = temp * (9/5) + 32.0 # Converting the temperature to Fahrenheit degrees.
    
    # Printing all the readings on the MicroPython shell.
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    # In case there is an error getting the readings, the except statement runs and an error message is printed
  except OSError as e: 
    print('Failed to read sensor.')
