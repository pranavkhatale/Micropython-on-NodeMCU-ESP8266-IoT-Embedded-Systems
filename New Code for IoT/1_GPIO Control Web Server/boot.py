# MicroPython Web Server – Control GPIO Connected Outputs using Micropython Framework.
# This is boot.py file & uses "sockets" and the "Python socket API".

# Import the socket library.
try:
  import usocket as socket
except:
  import socket

# Import the "Pin" class from the "machine" module to be able to interact with the GPIOs.
from machine import Pin

# Import the network library, it helps to connect the NodeMCU to a Wi-Fi network.
import network

# Turn off vendor OS debugging messages.
import esp
esp.osdebug(None)

# Run a garbage collector
# A garbage collector is a form of automatic memory management.
# This is a way to reclaim memory occupied by objects that are no longer in used by the program.
# This is useful to save space in the flash memory.
import gc
gc.collect()

# Below variables hold your network credentials: Replace it with your own network credentials.
ssid = 'D-Link'
password = 'pass@123'

# Set the NodeMCU as a Wi-Fi station.
station = network.WLAN(network.STA_IF)

# Activate the station.
station.active(True)

# NodeMCU connects to your Wi-Fi router using the SSID and password defined earlier.
station.connect(ssid, password)

# To ensure that the code doesn’t proceed while the ESP is not connected to your network.
while station.isconnected() == False:
  pass

# Successful connection, prints network interface parameters like the NodeMCU IP address.
# Uses the ifconfig() method on the station object.
print('Connection successful')
print(station.ifconfig())

# Create a Pin object called "led" that is an output.
#LED1 i.e GPIO 16
led = Pin(16, Pin.OUT)

# As you got the IP address of the NodeMCU in shell, paste it in browser & control the GPIO's.
# End of program.