# Import all board pins.
import os

os.environ["BLINKA_FORCEBOARD"]="ROC-RK3328-CC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

import board
import digitalio
from adafruit_blinka.board.librecomputer.roc_rk3328_cc import *
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

import time
import busio

from PIL import Image, ImageDraw, ImageFont
# Import the SSD1306 module.
import adafruit_ssd1306


import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus


# Create the I2C interface.
i2c = busio.I2C(Pin((0,0)), Pin((0,1)))

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, 0x76)
bmp280.sea_level_pressure = 1013.25

display.fill(0)

display.show()

while (True):
    image = Image.new("1", (128, 32))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((2, 0 + 2), f'Temp {bmp280.temperature:.2f} C', font=font, fill=255)
    draw.text((2, 0 + 10), f'Pres {bmp280.pressure:.2f} hPa' , font=font, fill=255)
    draw.text((2, 0 + 18), f'Alt {bmp280.altitude:.2f} m' , font=font, fill=255)
    display.fill(0)
    display.image(image)
    display.show()
    time.sleep(5)
