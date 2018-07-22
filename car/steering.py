import RPi.GPIO as GPIO
import time

class Steering():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(18, GPIO.OUT)
        self.p = GPIO.PWM(18,50)
        self.p.start(3.5)
        self.has_turned = False

    def turn_left(self):
        self._set_duty_cycle(4.5)
        self.has_turned = True

    def turn_right(self):
        self._set_duty_cycle(2.5)
        self.has_turned = True

    def turn_center(self):
        self._set_duty_cycle(3.5)
        self.has_turned = False

    def clear(self):
        self.has_turned = False
        self.p.stop()
        GPIO.cleanup()

    def _set_duty_cycle(self, duty, time_secs = 1):
        self.p.ChangeDutyCycle(duty)
        time.sleep(time_secs)
