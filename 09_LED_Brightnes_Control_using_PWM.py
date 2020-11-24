# LED Brightness control using PWM
# by Pranav Khatale
# 24 November 2020
import time
from machine import Pin, PWM

#Define a function to change duty cycle
def brightness(pwmLed, percentage):
     #Value of duty cycle is between 0 and 1023 inclusive.
     pwmLed.duty(int (percentage * 1023 / 100));

# Setup a GPIO Pin 12 for output
myLed = Pin(12, Pin.OUT)
#Instantiate a PWM object
myLedPwm = PWM(myLed)
while True:
    
    #Full brightness - 100% duty cycle
    brightness(myLedPwm, 100)
    #pause
    time.sleep_ms(2000)

    #Half brightness - 50% duty cycle
    brightness(myLedPwm, 50)
    #pause
    time.sleep_ms(2000)

    #One third brightness - 33% duty cycle
    brightness(myLedPwm, 33)
    #pause
    time.sleep_ms(2000)

    #deinitialize/stop the PWM
    myLedPwm.deinit()