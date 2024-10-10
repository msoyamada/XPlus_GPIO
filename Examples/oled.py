# Import all board pins.
import os

os.environ["BLINKA_FORCEBOARD"]="ROC-RK3328-CC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

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

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

display.fill(0)

display.show()

image = Image.new("1", (128, 32))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((20, 0 + 10), "Hello", font=font, fill=255)
draw.text((20, 0 + 18), "world " , font=font, fill=255)

display.image(image)
display.show()
