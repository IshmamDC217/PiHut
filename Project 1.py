# Project 1
## Using GPIO pink
from machine import Pin
# LED light up
##  Setting up a pin to use. Pin.OUT is to set the chosen pin as output
onboardLED = Pin(25, Pin.OUT)
## Boolean
onboardLED.value(1)

# Blink
from machine import Pin, Timer

def toggle_led(timer):
    onboardLED.toggle()

onboardLED = Pin(25, Pin.OUT)
timer = Timer()
timer.init(freq=1, mode=Timer.PERIODIC, callback=toggle_led)

# Blink according to Frequency
from machine import Pin, Timer

def toggle_led(timer):
    onboardLED.toggle()

onboardLED = Pin(25, Pin.OUT)
timer = Timer()
timer.init(freq=25, mode=Timer.PERIODIC, callback=toggle_led)

