## Day #4: Exploring the World of Analogue

### Overview
On Day 4 of our exciting journey, we delve into the realm of analog signals with our Raspberry Pi Pico. This exploration contrasts the binary nature of digital signals, as we embrace the versatility and gradation of analog inputs. It's a day to appreciate the subtleties that analog components, like potentiometers, bring to our projects.

### Box #4 Contents
- 1x 10K Potentiometer (variable resistor)
- 1x Mini breadboard
- Additional jumper wires

### Today's Project
Our focus today is constructing a circuit that integrates the potentiometer with our Raspberry Pi Pico. We'll engage in activities that demonstrate how analog signals provide a wider range of values, suitable for various applications, especially in comparison to the binary world of digital signals.

#### Understanding the Potentiometer
- **What Is It?** A potentiometer is a three-legged variable resistor. Unlike the fixed resistors used previously, it allows for adjusting resistance from 0 to 10,000 ohms.
- **How It Works:** Turning the knob changes the resistance, which in turn varies the voltage across the potentiometer. This varying voltage can be read by the Raspberry Pi Pico’s ADC (Analog to Digital Converter) pins.

#### Constructing the Circuit
1. Ensure the Pico is unplugged before starting.
2. Fit the potentiometer on the breadboard.
3. Connect the right pin of the potentiometer to the 3V3(OUT) pin on the Pico, the middle pin to GPIO 27, and the left pin to a GND lane.

### Activities Overview
1. **Printing Analog Values:** 
   - This basic activity involves reading the potentiometer's value and printing it, helping us understand how analog values are represented in our code.

2. **Control LED Flashes with Analog Values:** 
   - Here, we use the potentiometer’s readings to control the frequency of LED flashes, demonstrating how analog inputs can influence digital outputs.

3. **Light LEDs Depending on the Potentiometer Value:** 
   - This activity uses conditional statements to light different LEDs based on the potentiometer’s analog reading.

4. **LED Fader using PWM:** 
   - A more advanced application where we explore Pulse Width Modulation (PWM) to fade an LED in and out, controlled by the potentiometer.

#### ADC Pins and PWM
- **ADC Pins:** GPIO26, 27, and 28 are ADC capable. They convert the analog signal from the potentiometer into a digital form for the Pico to use.
- **PWM:** PWM allows control over the brightness of an LED by rapidly switching it on and off. The duty cycle and frequency of the PWM signal determine the perceived brightness.
