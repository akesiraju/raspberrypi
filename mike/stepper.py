import RPi.GPIO as GPIO
import time
from enum import Enum


class Direction(Enum):
    ClockWise = 1
    CounterClockWise = 2


def rotate(control_pins, angle: int = 360, direction=Direction.ClockWise):
    if direction == Direction.CounterClockWise:
        control_pins = control_pins[::-1]

    GPIO.setmode(GPIO.BOARD)

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

        halfstep_seq = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]

    steps = int(angle * 512 / 360)

    for i in range(steps):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    GPIO.cleanup()
