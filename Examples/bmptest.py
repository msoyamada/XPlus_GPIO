# Import all board pins.
import os

os.environ["BLINKA_FORCEBOARD"]="ROC-RK3328-CC"
os.environ["BLINKA_FORCECHIP"]="RK3328"
import time
import board
import digitalio
from adafruit_blinka.board.librecomputer.roc_rk3328_cc import *
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin


import busio

from PIL import Image, ImageDraw, ImageFont
# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(Pin((0,0)), Pin((0,1)))


import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, 0x76)

# OR Create sensor object, communicating over the board's default SPI bus
# spi = board.SPI()
# bmp_cs = digitalio.DigitalInOut(board.D10)
# bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)
