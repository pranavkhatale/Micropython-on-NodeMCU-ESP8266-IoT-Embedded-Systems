# Control Relay Module with MicroPython Web Server.
# This is boot.py file.

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

# Insert your network credentials in the following variables.
ssid = 'Snehal'
password = '91705796'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# ESP8266 GPIO 4
relay = Pin(4, Pin.OUT)

# As you got the IP address of the NodeMCU in shell, paste it in browser & control the Relay.
# End of Program.