import os

os.environ["BLINKA_FORCEBOARD"]="GENERIC_LINUX_PC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

import time
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

pin = Pin((1,10))  # (x,y) = 32*x + 10*y  -> 1*32 + 10 = 42 (GPIO 42)

print("hello blinky!")

led = digitalio.DigitalInOut(pin)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
