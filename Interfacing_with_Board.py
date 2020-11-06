# Interfacing with NodeMCU ESP8266 12-E using Micropython in Thonny IDE.
# This file is compulsorily saved as "main.py" on NodeMCU as it runs this program ones powered up.
# by Pranav Khatale
# 06 November 2020

import time     # importing time library.
import machine  # importing machine i.e NodeMCU ESP8266 Datafiles.

# Defining the pins as Input or Output.
# Assigning Pin D0 or GPIO pin 16 as the name LED1 & declaring LED1 pin as an output.
LED1 = machine.Pin(16,machine.Pin.OUT)

# Assigning Pin D1 or GPIO pin 5 as the name LED2 & declaring LED2 pin as an output.
LED2 = machine.Pin(5,machine.Pin.OUT)

# Assigning Pin D2 or GPIO pin 4 as the name Relay1 & declaring LED3 pin as an output.
Relay1 = machine.Pin(4,machine.Pin.OUT)

# Assigning Pin D3 or GPIO pin 0 as the name Relay2 & declaring LED4 pin as an output.
Relay2 = machine.Pin(0,machine.Pin.OUT)

# The program written below runs forever.
while True:
    LED1.off()       # turning LED1 ON.
    time.sleep(1)    # delay of 1 seconds.
    
    LED1.on()        # turning LED1 OFF. 
    time.sleep(1)    # delay of 1 seconds.
    
    LED2.off()       # turning LED2 ON.
    time.sleep(1)    # delay of 1 seconds.
    
    LED2.on()        # turning LED2 OFF. 
    time.sleep(1)    # delay of 1 seconds.

    Relay1.off()     # turning Relay1 ON.
    time.sleep(1)    # delay of 1 seconds.
    
    Relay1.on()      # turning Relay1 OFF. 
    time.sleep(1)    # delay of 1 seconds.
    
    Relay2.off()     # turning Relay2 ON.
    time.sleep(1)    # delay of 1 seconds.
    
    Relay2.on()      # turning Relay2 OFF. 
    time.sleep(1)    # delay of 1 seconds.

