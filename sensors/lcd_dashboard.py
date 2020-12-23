#!/usr/bin/python
from lcd_display import lcddriver
import requests
import time

my_lcd = lcddriver.lcd()

while True:

    try:
        response = requests.get("http://robopi:5003/api/v1/climate")
        response.raise_for_status()
        response = response.json()
        my_lcd.lcd_display_string(f"    {response['time']}", 1)
        my_lcd.lcd_display_string(f" T {response['temperature']}  H {response['humidity']}", 2)
        time.sleep(3)
    except KeyboardInterrupt:
        print("Key exit")
        my_lcd.lcd_clear()
        exit()
