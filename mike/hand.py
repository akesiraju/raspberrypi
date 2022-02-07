import stepper
import time


def lift_up(control_pins):
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.ClockWise)


def lift_down(control_pins):
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.CounterClockWise)


def wiggle(control_pins):
    stepper.rotate(control_pins, angle=15, direction=stepper.Direction.CounterClockWise)
    time.sleep(0.1)
    stepper.rotate(control_pins, angle=15, direction=stepper.Direction.ClockWise)
    time.sleep(0.1)
    stepper.rotate(control_pins, angle=15, direction=stepper.Direction.CounterClockWise)
    time.sleep(0.1)
    stepper.rotate(control_pins, angle=15, direction=stepper.Direction.ClockWise)
    time.sleep(0.1)
