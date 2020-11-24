# Fading the LED
# by Pranav Khatale
# 24 November 2020
import time
from machine import Pin, PWM

#Define a function to change duty cycle
def brightness(pwmLed, percentage):
     #The duty cycle is between 0 and 1023 inclusive.
     pwmLed.duty(int (percentage * 1023 / 100));

# Setup a GPIO Pin for output
myLed = Pin(12, Pin.OUT)
#Instantiate a PWM object
myLedPwm = PWM(myLed)


percentageVal = 100
delta = 5

for i in range(10):
    for j in range(20):
        brightness(myLedPwm, percentageVal)

        if percentageVal >= 100 or percentageVal <=0 :
            delta = -1 * delta
            percentageVal = percentageVal + delta
            time.sleep_ms(50)

            #deinitialize/stop the PWM
            myLedPwm.deinit()