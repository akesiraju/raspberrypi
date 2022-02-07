import motor

forward_pin = 37
reverse_pin = 31
enable_pin = 35


def walk():
    motor.run(enable_pin, forward_pin, reverse_pin)


def reverse():
    motor.run(enable_pin, reverse_pin, forward_pin)


def stop():
    motor.stop(enable_pin, forward_pin, reverse_pin)
