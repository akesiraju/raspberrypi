#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def dance(pin, speed):
    GPIO.setup(pin,GPIO.OUT)
    print ("pin", pin, "on")

    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1/speed)

    print ("pin", pin, "off")
    GPIO.output(pin,GPIO.LOW)

def main():
    """ main """

    for y in range(1,2):
        for x in [13,16,23,25,26]:
            dance(x,10)

if __name__ == "__main__":
    main()