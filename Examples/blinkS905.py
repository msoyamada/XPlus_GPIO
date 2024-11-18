import os
os.environ["BLINKA_FORCEBOARD"]="GENERIC_LINUX_PC"
os.environ["BLINKA_FORCECHIP"]="S905X"


import time
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
#from adafruit_blinka.microcontroller.generic_agnostic_board.pin import *
#from adafruit_blinka.microcontroller.amlogic.s905 import Pin

print(Pin)

pin = Pin((0,0))

print("hello blinky!")

led = digitalio.DigitalInOut(pin)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
