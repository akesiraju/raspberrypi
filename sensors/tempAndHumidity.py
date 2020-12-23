#!/usr/bin/python
import sys
import Adafruit_DHT
from lcd_display import lcddriver
from datetime import datetime
import time

my_lcd = lcddriver.lcd()


while True:

    try:
        # Using gpio4
        humidity, temperature = Adafruit_DHT.read_retry(11, 12)
        # print(f"Time: {datetime.now().strftime('%H:%M:%S')} Temp: {temperature} C, Humidity: {humidity}")
        my_lcd.lcd_display_string(f"    {datetime.now().strftime('%H:%M:%S')}", 1)
        my_lcd.lcd_display_string(f" T {temperature}  H {humidity}", 2)
        # print temperature
        # print humidity
        time.sleep(3)
    except KeyboardInterrupt:
        print("Key exit")
        my_lcd.lcd_clear()
        exit()
