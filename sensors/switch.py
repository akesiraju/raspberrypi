import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18,True)
#time.sleep(20)
#while True:
input_state = GPIO.input(18)
if input_state == False:
    print('Button Pressed')
    time.sleep(0.2)
GPIO.cleanup()
