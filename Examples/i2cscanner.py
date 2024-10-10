import os

os.environ["BLINKA_FORCEBOARD"]="ROC-RK3328-CC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

import time
import board
import digitalio
from adafruit_blinka.board.librecomputer.roc_rk3328_cc import *
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin


import busio
#i2c= board.I2C()
# To use default I2C bus (most boards)
#i2c = busio.I2C(Pin((1,10)), Pin((1,9)))  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# To create I2C bus on specific pins
i2c = busio.I2C(Pin((0,0)), Pin((0,1)))
# i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()
