# Imports
from machine import Pin
import time

# Project 3
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)

def blink(led, count=1, on_duration=0.5, off_duration=0.5):
    """Blink an LED a specified number of times."""
    for _ in range(count):
        led.value(1)
        time.sleep(on_duration)
        led.value(0)
        if _ < count - 1:
            time.sleep(off_duration)

while True:
    
    time.sleep(0.2)
        
    if button1.value() == 1 and button2.value() == 1: # Both
        print("Buttons 1 and 2 pressed")
        blink(red, count=3, on_duration=0.5, off_duration=0.2)
        green.value(1) 
        time.sleep(1)
        green.value(0)

    elif button1.value() == 1: # If button 1 is pressed
        
        print("Button 1 pressed")
        green.value(1) # amber LED on
        red.value(0) # red LED off

    else: # If no buttons are being pressed
        
        red.value(1) # red LED on
        amber.value(0) # amber LED off
        green.value(0) # green LED off
