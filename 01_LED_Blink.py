# Blinking Built-in LED on NodeMCU ESP8266 12-E using Micropython program in Thonny IDE.
# by Pranav Khatale
# 05 November 2020

import time     # importing time library.
import machine  # importing machine i.e NodeMCU ESP8266 Datafiles.

#Built-in LED is connected to GPIO pin 2 of NodeMCU ESP8266 12-E, declaring pin 2 as Output.
pin1 = machine.Pin(2,machine.Pin.OUT) 

while True:
    pin1.on()       # turning LED OFF.
    time.sleep(1)   # delay of 1 seconds.
    pin1.off()      # turning LED ON. 
    time.sleep(1)   # delay of 1 seconds.
