# Note: added a 330 ohm resistor on ground pin
# This circuit amounts to varying the brightness
# of the LED. duty_u16 is between 0 and 62355 an
# is the fraction of a cycle the LED is illuminated.
# The cycle frequency is controlled by the frequency
# setting [Hz]. You cannot set frequency = 1, but
# a value of 10 works. With a duty_u16 of 32768 (half
# a cycle) the LED appears to blink on and off.
# A high frequency fakes the dimming aspect. The sleep
# at the end of the loop I think must cycle the
# LED pssibly multiple times before loading new numbers.

from machine import Pin,PWM
import utime
import random
PWM(Pin(2)).deinit()
PWM(Pin(3)).deinit()
PWM(Pin(4)).deinit()
Led_R = PWM(Pin(2))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(4))

# Define the frequency
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)
if __name__ == "__main__":
    while True:
        # range of random numbers
        R=random.randint(0,65535)
        G=random.randint(0,65535)
        B=random.randint(0,65535)
        print(R,G,B)
        Led_R.duty_u16(R)
        Led_G.duty_u16(G)
        Led_B.duty_u16(B)
        utime.sleep_ms(1000)