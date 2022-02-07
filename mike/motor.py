# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)


def run(enable_pin, high_pin, low_pin):
    print("run")

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(high_pin, GPIO.OUT)
    GPIO.setup(low_pin, GPIO.OUT)

    print("move start")

    GPIO.output(enable_pin, GPIO.HIGH)
    GPIO.output(high_pin, GPIO.HIGH)
    GPIO.output(low_pin, GPIO.LOW)


def stop(enable_pin, high_pin, low_pin):
    print("stop")

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(high_pin, GPIO.OUT)
    GPIO.setup(low_pin, GPIO.OUT)

    GPIO.output(enable_pin, GPIO.LOW)
    GPIO.output(high_pin, GPIO.LOW)
    GPIO.output(low_pin, GPIO.LOW)

    GPIO.cleanup()
