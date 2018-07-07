import RPi.GPIO as GPIO
import time

#When there is light, we get a signal on 21

pin = 21
light = 20
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN)
GPIO.setup(light, GPIO.OUT)

while True:
    if GPIO.input(pin):
        print("contact")
        GPIO.output(light, GPIO.HIGH)
    else:
        print("no contact")
        GPIO.output(light, GPIO.LOW)
    time.sleep(0.3)

GPIO.cleanup()