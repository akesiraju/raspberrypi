import hand

control_pins = [7, 11, 13, 15]


def lift_up():
    hand.lift_up(control_pins)


def lift_down():
    hand.lift_down(control_pins)


def wiggle():
    hand.wiggle(control_pins)
