import RPi.GPIO as GPIO
import time

pin = 21
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)

for x in range(1,10):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)

GPIO.cleanup()