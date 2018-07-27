import RPi.GPIO as GPIO
import time
import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')

class Steering():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(18, GPIO.OUT)
        self.p = GPIO.PWM(18,50)
        self.p.start(3.5)
        self.has_turned = False

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self._clear()

    def turn_left(self):
        self.logger.debug('turning left')
        self._set_duty_cycle(4.75)

    def turn_right(self):        
        self.logger.debug('turning right')
        self._set_duty_cycle(2.25)

    def turn_center(self):        
        self.logger.debug('turning center')
        self._set_duty_cycle(3.5)

    def _clear(self):        
        self.logger.debug('clearing')
        self.p.stop()

    def _set_duty_cycle(self, duty, time_secs = 0.1):
        self.logger.debug('setting duty cycle to duty %s for time %s' % (duty, time_secs))
        self.p.ChangeDutyCycle(duty)
        time.sleep(time_secs)
        self.logger.debug('end duty cycle')

# if __name__ == '__main__':
#     with Steering() as steer:
#         steer.turn_right()
#         steer.turn_left()
#         steer.turn_center()
