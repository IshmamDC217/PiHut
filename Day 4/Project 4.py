from machine import ADC, Pin
import time

# Function to map the ADC value to a smaller range, using float division
def map_range(value, in_min, in_max, out_min, out_max):
    return round((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    adc_value = potentiometer.read_u16()  # Read the potentiometer value
    mapped_value = map_range(adc_value, 0, 65535, 0, 10)  # Map the ADC value to 0-10 range
    print("ADC Reading:", adc_value, "Mapped Value:", mapped_value)

    time.sleep(0.1)  # Short delay

    # Adjust the thresholds based on the mapped value
    if mapped_value <= 3:
        red.value(1)
        amber.value(0)
        green.value(0)
    elif 3 < mapped_value <= 7:
        red.value(0)
        amber.value(1)
        green.value(0)
    elif mapped_value > 7:
        red.value(0)
        amber.value(0)
        green.value(1)
