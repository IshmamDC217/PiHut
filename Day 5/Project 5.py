from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

C = 523
D = 587
E = 659
F = 698
G = 784
A = 880
B = 988
C_high = 1047

beat = 0.4

volume = 10000

def play(note, duration):
    buzzer.duty_u16(volume) 
    buzzer.freq(note)       
    time.sleep(duration)    
    buzzer.duty_u16(0)       
    time.sleep(0.05)        

melody = [
    (E, beat), (E, beat), (E, beat * 2),
    (E, beat), (E, beat), (E, beat * 2),
    (E, beat), (G, beat), (C, beat), (D, beat), (E, beat * 4),
    (F, beat), (F, beat), (F, beat * 1.5), (F, beat * 0.5),
    (F, beat), (E, beat), (E, beat), (E, beat * 1.5), (E, beat * 0.5),
    (E, beat), (D, beat), (D, beat), (E, beat), (D, beat * 2), (G, beat * 2)
]

for note, duration in melody:
    play(note, duration)

buzzer.duty_u16(0)
