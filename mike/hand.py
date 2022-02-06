import stepper


def lift_up(control_pins):
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.ClockWise)


def lift_down(control_pins):
    stepper.rotate(control_pins, angle=90, direction=stepper.Direction.CounterClockWise)
