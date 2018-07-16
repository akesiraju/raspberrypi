# Return the distance to the block infront
# Libraries

import RPi.GPIO as GPIO
import time
#import keyboard
import sys


class Car():
    def __init__(self):

        self.turntime = 0.2
        self.drivetime = 0.75

        self.prev_key=0
        self.brakes = False
        self.isturning = False
        self.angle = 100
        self.turningRadius=20
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        # make right turn by deafault the first time
        self.left = True

        # ultra sonic controls, trigger and echo
        self.trigger = 23
        self.echo = 24

        # servo motor data
        self.servo = 18

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

        GPIO.setup(self.servo, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo, 50)
        self.pwm.start(0)

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def Log(self, msg):
        print(msg)
        #pass

    def distance(self):
        GPIO.output(self.trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger, GPIO.LOW)
        startTime = time.time()
        stopTime = time.time()

        while GPIO.input(self.echo) == 0:
            startTime = time.time()

        while GPIO.input(self.echo) == 1:
            stopTime = time.time()

        elapsed = stopTime - startTime
        dist = (elapsed * 34300) / 2

        self.Log("distance = " + str(dist))

        return dist

    def getDistance(self):
        while True:
            self.distance()
            time.sleep(1)

    # Set servo motor angle
    def SetAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.servo, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(duty)
        #time.sleep(1.0)
        GPIO.output(self.servo, GPIO.LOW)


    # Turn the servomotor left
    def TurnLeft(self):
        self.SetAngle(self.angle + self.turningRadius)
        self.isturning = True
        #time.sleep(3.0)
        #SetAngle(90)


    # Turn the servo motor right
    def TurnRight(self):
        self. SetAngle(self.angle - self.turningRadius)
        self.isturning = True
        #time.sleep(3.0)
        #SetAngle(90)


    # Turn servo motor
    def Turn(self):
        self.Log(self.left)

        if self.left == True:
            self.TurnRight()
            self.left = False
        else:
            self.TurnLeft()
            self.left = True


    # drive forward
    def  straight(self):
        if self.isturning == True:
            self.SetAngle(self.angle)
            self.isturning = False
        else:
            self.Log('no turning')

    def back(self):    
        self.straight()
        #Log('move start')

        GPIO.output(self.enable1, GPIO.HIGH)
        # if input1 and input2 are swapped a regular motor will go in reverse.
        GPIO.output(self.input1, GPIO.HIGH)
        # but lego will not as it has different pin for reverse. so we should disable this signal and enable that , creepy
        GPIO.output(self.input2, GPIO.LOW)

        # time.sleep(2)

        # GPIO.output(enable1, GPIO.LOW)


    def front(self):
        #Log('move start')
        # if input1 and input2 are swapped we go in reverse.        
        
        self.straight()
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)

        GPIO.output(self.enable1, GPIO.HIGH)

        # time.sleep(2)

        # GPIO.output(enable1, GPIO.LOW)
    def clear(self):
        self.pwm.stop()
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.enable1, GPIO.LOW)
        GPIO.cleanup()


    def move(self, signal):
        if signal == 259:
            if self.brakes == True:
                GPIO.output(self.enable1, GPIO.HIGH)
                self.brakes = False
            self.front()

        if signal == 260:
            self.TurnLeft()

        if signal == 261:
            self.TurnRight()

        if signal == 258:
            self.back()

        if signal == 32:
            self.brakes = True
            GPIO.output(self.enable1, GPIO.LOW)

        if signal == 27:
            self.clear()
        
        return signal

