import stepper
from enum import Enum


class HeadPosition(Enum):
    Straight = 1
    Left = 2
    Right = 3


control_pins = [32, 36, 38, 40]
head_position = HeadPosition.Straight


def turn_left():
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.ClockWise)
    head_position = HeadPosition.Left


def turn_right():
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.CounterClockWise)
    head_position = HeadPosition.Right
