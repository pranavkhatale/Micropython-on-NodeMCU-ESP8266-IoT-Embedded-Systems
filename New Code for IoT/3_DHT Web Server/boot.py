# MicroPython Web Server (Weather Station)
# This is boot.py file.
# The boot.py file contains the code that only needs to run once on boot.
# This includes importing libraries, network credentials, instantiating pins, connecting to your network, and other configurations.

# Import the necessary libraries to create a web server.
try:
  import usocket as socket
except:
  import socket
  
# Import the "Pin" class from the "machine" module and the "dht" module to read from the DHT11 sensor.
import network
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

# Add your network credentials in the below lines.
ssid = 'D-link'
password = 'pass@123'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# Initialize the sensor by creating a dht instance on GPIO 15.
sensor = dht.DHT11(Pin(15))
# End of Program.