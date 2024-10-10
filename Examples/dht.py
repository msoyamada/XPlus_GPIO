import os

os.environ["BLINKA_FORCEBOARD"]="GENERIC_LINUX_PC"
os.environ["BLINKA_FORCECHIP"]="RK3328"

import time
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
import adafruit_dht

pin = Pin((3,3))


dht_device =  adafruit_dht.DHT11(pin)

while True:
	try:
	    temp= dht_device.temperature
	    hum= dht_device.humidity
	    print(f'Temperature {temp} C,  Humidity  {hum} %')
	except RuntimeError as error:
	        # Errors happen fairly often, DHT's are hard to read, just keep going
	        print(error.args[0])
	        time.sleep(2.0)
	        continue
	except Exception as error:
	        dhtDevice.exit()
	        raise error

	time.sleep(5)
