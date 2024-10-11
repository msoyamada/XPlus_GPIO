import os

os.environ["BLINKA_FORCEBOARD"]="ROC-RK3328-CC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

import time
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin


pin = Pin((3,3))
pinled = Pin((1,10))

button = digitalio.DigitalInOut(pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(pinled)
led.direction = digitalio.Direction.OUTPUT



while True:
    led.value = button.value
    #print(button.value)
    time.sleep(0.1)
