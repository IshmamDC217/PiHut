from machine import Pin
import time

# Button names and GPIO pin numbers
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)  # Red
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)   # Green
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)   # Amber

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
        time.sleep(off_duration)

def traffic_light_sequence():
    """Simulate traffic light sequence."""
    red.value(1)
    time.sleep(1)
    red.value(0)
    amber.value(1)
    time.sleep(1)
    amber.value(0)
    green.value(1)
    time.sleep(1)
    green.value(0)

while True:
    time.sleep(0.2)  # Delay

    # Check each button and log if pressed
    if button1.value() == 1:
        print("Button 1 (Red) pressed")
        red.value(1)  # Red on
    else:
        red.value(0)  # Red off

    if button2.value() == 1:
        print("Button 2 (Green) pressed")
        green.value(1)  # Green on
    else:
        green.value(0)  # Green off

    if button3.value() == 1:
        print("Button 3 (Amber) pressed")
        amber.value(1)  # Amber on
    else:
        amber.value(0)  # Amber off

    # Traffic light sequence for simultaneous button press
    if button1.value() == 1 and button2.value() == 1 and button3.value() == 1:
        print("All three buttons pressed, initiating traffic light sequence")
        traffic_light_sequence()
