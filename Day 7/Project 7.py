# Project 6
from machine import Pin, PWM
import time

# Set up the LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set PWM duty to 0% at program start
buzzer.duty_u16(0)

# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Warm up/settle PIR sensor
print("Warming up...")
time.sleep(10)  # Delay to allow the sensor to settle
print("Sensor ready!")

# Define the note frequencies (in Hz)
C4 = 261
E5 = 659
G4_sharp = 415
D5_sharp = 622
F5_sharp = 740
A5 = 880
G5_sharp = 830
B5 = 988
C6 = 1047
B5_flat = 932
E6 = 1319
G5 = 784
A5_flat = 831
A4 = 440
E4 = 329
C5 = 523
B4 = 494
D5 = 587  # Frequency for D5

# Fur Elise melody
melody = [
    (E5, 0.15), (D5_sharp, 0.15), (E5, 0.15), (D5_sharp, 0.15), (E5, 0.15), (B4, 0.15), (D5, 0.15), (C5, 0.15),
    (A4, 0.3), (0, 0.15), (C4, 0.15), (E4, 0.15), (A4, 0.15), (B4, 0.3), (0, 0.15),
    (E4, 0.15), (G4_sharp, 0.15), (B4, 0.15), (C5, 0.3), (0, 0.15), (E4, 0.15), (E5, 0.15), (D5_sharp, 0.15), 
    (E5, 0.15), (D5_sharp, 0.15), (E5, 0.15), (B4, 0.15), (D5, 0.15), (C5, 0.15), 
    (A4, 0.3), (0, 0.15), (C4, 0.15), (E4, 0.15), (A4, 0.15), (B4, 0.3), (0, 0.15),
    (E4, 0.15), (C5, 0.15), (B4, 0.15), (A4, 0.3)
]

def play(note, duration):
    if note == 0:  # Rest
        buzzer.duty_u16(0)
    else:
        buzzer.duty_u16(10000)  # Volume up
        buzzer.freq(note)       # Set frequency
    time.sleep(duration)        # Play note or rest for duration


def alarm():  # Our alarm function
    for note, duration in melody:
        play(note, duration)
        red.value(not red.value())  # Toggle Red LED
        amber.value(not amber.value())  # Toggle Amber LED
        green.value(not green.value())  # Toggle Green LED

while True:  # Run forever
    time.sleep(0.01)  # Delay to stop unnecessary program speed
    
    if pir.value() == 1:  # If PIR detects movement
        print("Movement detected!")
        alarm()  # Call our function
        print("Sensor active")  # Let us know that the sensor is active again

