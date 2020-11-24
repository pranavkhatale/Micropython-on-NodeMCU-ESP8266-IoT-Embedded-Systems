# Getting Analog values from Potentiometer
# by Pranav Khatale
# 24 November 2020
from machine import Pin, ADC    # import Pin and ADC class
from time import sleep          # import sleep class

print('Potentiometer readings are shown below:')

pot = ADC(0)               # pot object


while True:
  pot_value = pot.read()        # read analod pin
  print('Analog Value:')
  print(pot_value)              # print ADC value
  sleep(0.25)
  

