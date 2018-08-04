import RPi.GPIO as GPIO
from steering import Steering
import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')


class Car():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        GPIO.setmode(GPIO.BCM)
        self.steer = Steering()
        self.brakes = False
        self.has_turned = False

        # motor driver
        self.input1 = 20
        self.input2 = 16
        self.enable1 = 21  # always disable after finishing and\or in catch

        # set GPIO direction (IN / OUT)

        # we send instructions to motor driver IC
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)
        # this will determine if signal should be sent to output pins
        GPIO.setup(self.enable1, GPIO.OUT)

    def apply_brakes(self):
        self.brakes = True
        GPIO.output(self.enable1, GPIO.LOW)

        return 'Applying Brakes'

    def turn(self, angle):
        self.steer.turn(angle)

        return 'Turned ' + str(angle)

    def reverse(self):
        if self.brakes:
            self.logger.debug('disabling brakes')
            GPIO.output(self.enable1, GPIO.HIGH)
            self.brakes = False
        
        #Log('move start')

        GPIO.output(self.enable1, GPIO.HIGH)
        # if input1 and input2 are swapped a regular motor will go in reverse.
        GPIO.output(self.input1, GPIO.HIGH)
        # but lego will not as it has different pin for reverse. so we should disable this signal and enable that , creepy
        GPIO.output(self.input2, GPIO.LOW)

        return 'Driving Reverse'

    def forward(self):
        #Log('move start')
        # if input1 and input2 are swapped we go in reverse.

        if self.brakes:
            self.logger.debug('disabling brakes')
            GPIO.output(self.enable1, GPIO.HIGH)
            self.brakes = False

        GPIO.output(self.enable1, GPIO.HIGH)

        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)

        return 'Driving Forward'

    def clear(self):
        self.steer.stop()
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.enable1, GPIO.LOW)
        GPIO.cleanup()

        return 'Engine Off'
