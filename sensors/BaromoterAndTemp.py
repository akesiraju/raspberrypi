import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
import time

#DOes not work yet

sensor = BMP085.BMP085(busnum=2)

print sensor

GPIO.cleanup()