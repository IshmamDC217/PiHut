from machine import Pin
import utime

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)

# Keeping pin 20 on
led3.high()

while True:
    led1.high()
    led2.low()
    utime.sleep(0.5)
    led1.low()
    led2.high()
    utime.sleep(0.5)
