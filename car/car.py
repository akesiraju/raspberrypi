import RPi.GPIO as GPIO
import steering

class Car():
    def __init__(self):

        self.steer = steering.Steering()      
        
        self.brakes = False
       
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)     

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

    def Log(self, msg):
        print(msg)
        #pass     

    def back(self):    
        if self.steer.has_turned:    
            self.steer.turn_center()
        #Log('move start')

        GPIO.output(self.enable1, GPIO.HIGH)
        # if input1 and input2 are swapped a regular motor will go in reverse.
        GPIO.output(self.input1, GPIO.HIGH)
        # but lego will not as it has different pin for reverse. so we should disable this signal and enable that , creepy
        GPIO.output(self.input2, GPIO.LOW)


    def front(self):
        #Log('move start')
        # if input1 and input2 are swapped we go in reverse.        
        
        if self.steer.has_turned:    
            self.steer.turn_center()
    
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)

        GPIO.output(self.enable1, GPIO.HIGH)

        # time.sleep(2)

        # GPIO.output(enable1, GPIO.LOW)
    def clear(self):        
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.enable1, GPIO.LOW)
        self.steer.clear()
        GPIO.cleanup()


    def move(self, signal):
        if signal == 258:
            if self.brakes == True:
                GPIO.output(self.enable1, GPIO.HIGH)
                self.brakes = False
            self.front()

        if signal == 260:
            self.steer.turn_left()

        if signal == 261:
            self.steer.turn_right()

        if signal == 259:
            self.back()

        if signal == 32:
            self.brakes = True
            GPIO.output(self.enable1, GPIO.LOW)

        if signal == 27:
            self.clear()
        
        return signal

