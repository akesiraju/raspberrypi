import RPi.GPIO as GPIO
from steering import Steering
import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')


class Car():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        GPIO.setmode(GPIO.BCM) 
        
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

    def back(self):    
        if self.has_turned:    
            with Steering() as steer:
                steer.turn_center()
        #Log('move start')

        GPIO.output(self.enable1, GPIO.HIGH)
        # if input1 and input2 are swapped a regular motor will go in reverse.
        GPIO.output(self.input1, GPIO.HIGH)
        # but lego will not as it has different pin for reverse. so we should disable this signal and enable that , creepy
        GPIO.output(self.input2, GPIO.LOW)


    def front(self):
        #Log('move start')
        # if input1 and input2 are swapped we go in reverse.        
        
        if self.has_turned:    
            with Steering() as steer:
                steer.turn_center()
    
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)

        GPIO.output(self.enable1, GPIO.HIGH)

        # time.sleep(2)

        # GPIO.output(enable1, GPIO.LOW)
    def clear(self):        
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.enable1, GPIO.LOW)
        GPIO.cleanup()


    def move(self, signal):
        if signal == 258:            
            self.logger.debug('going forward')

            if self.brakes == True:                
                self.logger.debug('disabling brakes')
                GPIO.output(self.enable1, GPIO.HIGH)
                self.brakes = False
            self.front()

        if signal == 260:
            self.logger.debug('turning left')
            with Steering() as steer:
                steer.turn_left()
            self.has_turned = True

        if signal == 261:
            self.logger.debug('turning right')
            with Steering() as steer:
                steer.turn_right()
            self.has_turned = True

        if signal == 259:            
            self.logger.debug('going back')
            self.back()

        if signal == 32:            
            self.logger.debug('applying brakes')
            self.brakes = True
            GPIO.output(self.enable1, GPIO.LOW)

        if signal == 27:            
            self.logger.debug('clearing')
            self.clear()
        
        return signal

